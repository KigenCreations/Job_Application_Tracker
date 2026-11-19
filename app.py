from flask import Flask, render_template, request, redirect, url_for
# render_template(): send the records to companies.html
# request: read information submitted thru a form
# redirect: send the browser to another page after saving
# url_for: generates the correct url for a flask route
from database import get_db_connection

import json
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

@app.route('/companies')
def companies():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT company_id, company_name, industry, city, state
            FROM companies
            ORDER BY company_name
        """)

        company_list = cursor.fetchall()

    finally:
        cursor.close()
        connection.close()

    return render_template('companies.html', companies=company_list)

# Add a new company to the database
@app.route('/companies/add', methods=['POST'])
def add_company():
    company_name = request.form.get('company_name', '').strip()
    industry = request.form.get('industry', '').strip()
    website = request.form.get('website', '').strip()
    city = request.form.get('city', '').strip()
    state = request.form.get('state', '').strip()
    notes = request.form.get('notes', '').strip()

    if not company_name:
        return "Company name is required.", 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO companies
                (company_name, industry, website, city, state, notes)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (company_name, industry, website, city, state, notes))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('companies'))

# Delete an existing company
@app.route('/companies/delete/<int:company_id>', methods=['POST'])
def delete_company(company_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM companies WHERE company_id = %s",
            (company_id,)
        )
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('companies'))

# Edit an existing company
@app.route('/companies/edit/<int:company_id>', methods=['GET', 'POST'])
def edit_company(company_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        if request.method == 'POST':
            # Read the updated information from the form
            company_name = request.form.get('company_name', '').strip()
            industry = request.form.get('industry', '').strip()
            website = request.form.get('website', '').strip()
            city = request.form.get('city', '').strip()
            state = request.form.get('state', '').strip()
            notes = request.form.get('notes', '').strip()

            if not company_name:
                return "Company name is required.", 400

            # Update the existing company
            cursor.execute("""
                UPDATE companies
                SET company_name = %s,
                    industry = %s,
                    website = %s,
                    city = %s,
                    state = %s,
                    notes = %s
                WHERE company_id = %s
            """, (company_name, industry, website,
                  city, state, notes, company_id))

            connection.commit()
            return redirect(url_for('companies'))

        # GET request: retrieve the company's existing information
        cursor.execute(
            "SELECT * FROM companies WHERE company_id = %s",
            (company_id,)
        )
        company = cursor.fetchone()

        if company is None:
            return "Company not found.", 404

        return render_template('edit_company.html', company=company)

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

# Display all jobs with their company names
@app.route('/jobs')
def jobs():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                j.job_id,
                j.job_title,
                c.company_name,
                j.job_type,
                j.salary_min,
                j.salary_max,
                j.is_active
            FROM jobs AS j
            JOIN companies AS c
                ON j.company_id = c.company_id
            ORDER BY j.job_title
        """)

        job_list = cursor.fetchall()

        # Retrieve companies for the Add Job dropdown
        cursor.execute("""
                       SELECT company_id, company_name
                       FROM companies
                       ORDER BY company_name
                       """)

        company_list = cursor.fetchall()

    finally:
        cursor.close()
        connection.close()

    return render_template(
        'jobs.html',
        jobs=job_list,
        companies=company_list
    )

# Add a new job to the database
@app.route('/jobs/add', methods=['POST'])
def add_job():
    import json

    # Read information submitted by the form
    company_id = request.form.get('company_id')
    job_title = request.form.get('job_title', '').strip()
    job_type = request.form.get('job_type') or None
    salary_min = request.form.get('salary_min') or None
    salary_max = request.form.get('salary_max') or None
    date_posted = request.form.get('date_posted') or None
    job_url = request.form.get('job_url', '').strip()
    job_description = request.form.get('job_description', '').strip()
    requirements = request.form.get('requirements', '').strip()
    is_active = 1 if request.form.get('is_active') else 0

    # Check required fields
    if not company_id or not job_title:
        return "Company and job title are required.", 400

    # Convert comma-separated skills into JSON
    if requirements:
        skills = [
            skill.strip()
            for skill in requirements.split(',')
            if skill.strip()
        ]

        requirements = json.dumps({"skills": skills})
    else:
        requirements = None

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO jobs (
                company_id, job_title, job_type,
                salary_min, salary_max, date_posted,
                job_url, job_description, requirements, is_active
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            company_id, job_title, job_type,
            salary_min, salary_max, date_posted,
            job_url, job_description, requirements, is_active
        ))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('jobs'))

# Delete a job from the database
@app.route('/jobs/delete/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM jobs WHERE job_id = %s",
            (job_id,)
        )
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('jobs'))


# Edit an existing job
@app.route('/jobs/edit/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    import json

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        if request.method == 'POST':
            # Read updated values from the form
            company_id = request.form.get('company_id')
            job_title = request.form.get('job_title', '').strip()
            job_type = request.form.get('job_type') or None
            salary_min = request.form.get('salary_min') or None
            salary_max = request.form.get('salary_max') or None
            date_posted = request.form.get('date_posted') or None
            job_url = request.form.get('job_url', '').strip()
            job_description = request.form.get('job_description', '').strip()
            requirements = request.form.get('requirements', '').strip()
            is_active = 1 if request.form.get('is_active') else 0

            if not company_id or not job_title:
                return "Company and job title are required.", 400

            # Validate JSON before saving
            if requirements:
                try:
                    requirements = json.dumps(json.loads(requirements))
                except json.JSONDecodeError:
                    return "Requirements must contain valid JSON.", 400
            else:
                requirements = None

            # Update the selected job
            cursor.execute("""
                UPDATE jobs
                SET company_id = %s,
                    job_title = %s,
                    job_type = %s,
                    salary_min = %s,
                    salary_max = %s,
                    date_posted = %s,
                    job_url = %s,
                    job_description = %s,
                    requirements = %s,
                    is_active = %s
                WHERE job_id = %s
            """, (
                company_id, job_title, job_type,
                salary_min, salary_max, date_posted,
                job_url, job_description, requirements,
                is_active, job_id
            ))

            connection.commit()
            return redirect(url_for('jobs'))

        # GET: Retrieve the job's existing information
        cursor.execute(
            "SELECT * FROM jobs WHERE job_id = %s",
            (job_id,)
        )
        job = cursor.fetchone()

        if job is None:
            return "Job not found.", 404

        # Retrieve companies for the dropdown
        cursor.execute("""
            SELECT company_id, company_name
            FROM companies
            ORDER BY company_name
        """)
        company_list = cursor.fetchall()

        # Format JSON for display in the textarea
        if job['requirements'] is not None:
            if isinstance(job['requirements'], (dict, list)):
                job['requirements'] = json.dumps(
                    job['requirements'], indent=2
                )

        return render_template(
            'edit_job.html',
            job=job,
            companies=company_list
        )

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

# Display all job applications
@app.route('/applications')
def applications():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Join applications with jobs and companies
        cursor.execute("""
            SELECT
                a.application_id,
                a.job_id,
                a.application_date,
                a.status,
                a.resume_version,
                a.cover_letter_sent,
                j.job_title,
                c.company_name
            FROM applications AS a
            JOIN jobs AS j
                ON a.job_id = j.job_id
            JOIN companies AS c
                ON j.company_id = c.company_id
            ORDER BY a.application_date DESC
        """)

        application_list = cursor.fetchall()

        # Retrieve jobs for the Add Application dropdown
        cursor.execute("""
                       SELECT j.job_id,
                              j.job_title,
                              c.company_name
                       FROM jobs AS j
                                JOIN companies AS c
                                     ON j.company_id = c.company_id
                       ORDER BY c.company_name, j.job_title
                       """)

        job_list = cursor.fetchall()

    finally:
        cursor.close()
        connection.close()

    return render_template(
        'applications.html',
        applications=application_list,
        jobs=job_list
    )

# Add a new job application
@app.route('/applications/add', methods=['POST'])
def add_application():

    # Read information from the HTML form
    job_id = request.form.get('job_id')
    application_date = request.form.get('application_date')
    status = request.form.get('status', 'Applied')
    resume_version = request.form.get('resume_version', '').strip()
    cover_letter_sent = 1 if request.form.get('cover_letter_sent') else 0

    # Validate required information
    if not job_id or not application_date:
        return "Job and application date are required.", 400

    allowed_statuses = (
        'Applied', 'Screening', 'Interview',
        'Offer', 'Rejected', 'Withdrawn'
    )

    if status not in allowed_statuses:
        return "Invalid application status.", 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO applications (
                job_id,
                application_date,
                status,
                resume_version,
                cover_letter_sent
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            job_id,
            application_date,
            status,
            resume_version,
            cover_letter_sent
        ))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('applications'))

# Delete an existing job application
@app.route('/applications/delete/<int:application_id>', methods=['POST'])
def delete_application(application_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            DELETE FROM applications
            WHERE application_id = %s
        """, (application_id,))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('applications'))

# Edit an existing job application
@app.route('/applications/edit/<int:application_id>', methods=['GET', 'POST'])
def edit_application(application_id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        if request.method == 'POST':
            job_id = request.form.get('job_id')
            application_date = request.form.get('application_date')
            status = request.form.get('status')
            resume_version = request.form.get('resume_version', '').strip()
            cover_letter_sent = 1 if request.form.get('cover_letter_sent') else 0

            allowed_statuses = (
                'Applied', 'Screening', 'Interview',
                'Offer', 'Rejected', 'Withdrawn'
            )

            if not job_id or not application_date or status not in allowed_statuses:
                return "Invalid application information.", 400

            cursor.execute("""
                UPDATE applications
                SET job_id = %s,
                    application_date = %s,
                    status = %s,
                    resume_version = %s,
                    cover_letter_sent = %s
                WHERE application_id = %s
            """, (
                job_id,
                application_date,
                status,
                resume_version,
                cover_letter_sent,
                application_id
            ))

            connection.commit()
            return redirect(url_for('applications'))

        # GET: Retrieve the selected application
        cursor.execute("""
            SELECT *
            FROM applications
            WHERE application_id = %s
        """, (application_id,))

        application = cursor.fetchone()

        if application is None:
            return "Application not found.", 404

        # Retrieve jobs for the dropdown
        cursor.execute("""
            SELECT j.job_id, j.job_title, c.company_name
            FROM jobs AS j
            JOIN companies AS c
                ON j.company_id = c.company_id
            ORDER BY c.company_name, j.job_title
        """)

        job_list = cursor.fetchall()

        return render_template(
            'edit_application.html',
            application=application,
            jobs=job_list
        )

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

# Display all contacts
@app.route('/contacts')
def contacts():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                ct.contact_id,
                ct.contact_name,
                ct.title,
                ct.email,
                ct.phone,
                ct.linkedin_url,
                c.company_name
            FROM contacts AS ct
            JOIN companies AS c
                ON ct.company_id = c.company_id
            ORDER BY ct.contact_name ASC
        """)

        contact_list = cursor.fetchall()

        # Retrieve companies for the Add Contact dropdown
        cursor.execute("""
                       SELECT company_id, company_name
                       FROM companies
                       ORDER BY company_name ASC
                       """)

        company_list = cursor.fetchall()

    finally:
        cursor.close()
        connection.close()

    return render_template(
        'contacts.html',
        contacts=contact_list,
        companies=company_list
    )

# Add a new contact
@app.route('/contacts/add', methods=['POST'])
def add_contact():

    # Read information from the HTML form
    company_id = request.form.get('company_id')
    contact_name = request.form.get('contact_name', '').strip()
    title = request.form.get('title', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
    linkedin_url = request.form.get('linkedin_url', '').strip()
    notes = request.form.get('notes', '').strip()

    # Validate required information
    if not company_id or not contact_name:
        return "Company and contact name are required.", 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO contacts (
                company_id,
                contact_name,
                title,
                email,
                phone,
                linkedin_url,
                notes
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            company_id,
            contact_name,
            title,
            email,
            phone,
            linkedin_url,
            notes
        ))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('contacts'))


# Delete an existing contact
@app.route('/contacts/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            DELETE FROM contacts
            WHERE contact_id = %s
        """, (contact_id,))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('contacts'))

# Edit an existing contact
@app.route('/contacts/edit/<int:contact_id>', methods=['GET', 'POST'])
def edit_contact(contact_id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        if request.method == 'POST':
            company_id = request.form.get('company_id')
            contact_name = request.form.get('contact_name', '').strip()
            title = request.form.get('title', '').strip()
            email = request.form.get('email', '').strip()
            phone = request.form.get('phone', '').strip()
            linkedin_url = request.form.get('linkedin_url', '').strip()
            notes = request.form.get('notes', '').strip()

            if not company_id or not contact_name:
                return "Company and contact name are required.", 400

            cursor.execute("""
                UPDATE contacts
                SET company_id = %s,
                    contact_name = %s,
                    title = %s,
                    email = %s,
                    phone = %s,
                    linkedin_url = %s,
                    notes = %s
                WHERE contact_id = %s
            """, (
                company_id,
                contact_name,
                title,
                email,
                phone,
                linkedin_url,
                notes,
                contact_id
            ))

            connection.commit()
            return redirect(url_for('contacts'))

        # GET: Retrieve the selected contact
        cursor.execute("""
            SELECT *
            FROM contacts
            WHERE contact_id = %s
        """, (contact_id,))

        contact = cursor.fetchone()

        if contact is None:
            return "Contact not found.", 404

        # Retrieve companies for the dropdown
        cursor.execute("""
            SELECT company_id, company_name
            FROM companies
            ORDER BY company_name ASC
        """)

        company_list = cursor.fetchall()

        return render_template(
            'edit_contact.html',
            contact=contact,
            companies=company_list
        )

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

# Dashboard
@app.route('/dashboard')
def dashboard():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # Count all companies
        cursor.execute("SELECT COUNT(*) AS total FROM companies")
        total_companies = cursor.fetchone()['total']

        # Count all jobs
        cursor.execute("SELECT COUNT(*) AS total FROM jobs")
        total_jobs = cursor.fetchone()['total']

        # Count all applications
        cursor.execute("SELECT COUNT(*) AS total FROM applications")
        total_applications = cursor.fetchone()['total']

        # Count all contacts
        cursor.execute("SELECT COUNT(*) AS total FROM contacts")
        total_contacts = cursor.fetchone()['total']

        # Count applications by status
        cursor.execute("""
            SELECT status, COUNT(*) AS total
            FROM applications
            GROUP BY status
            ORDER BY status
        """)
        application_statuses = cursor.fetchall()

    finally:
        cursor.close()
        connection.close()

    return render_template(
        'dashboard.html',
        total_companies=total_companies,
        total_jobs=total_jobs,
        total_applications=total_applications,
        total_contacts=total_contacts,
        application_statuses=application_statuses
    )

# Job Match
@app.route('/job-match', methods=['GET', 'POST'])
def job_match():

    matches = []
    entered_skills = ''

    if request.method == 'POST':
        entered_skills = request.form.get('skills', '')

        # Convert user skills into a set
        user_skills = {
            skill.strip().lower()
            for skill in entered_skills.split(',')
            if skill.strip()
        }

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute("""
                SELECT
                    j.job_id,
                    j.job_title,
                    j.requirements,
                    c.company_name
                FROM jobs AS j
                JOIN companies AS c
                    ON j.company_id = c.company_id
                WHERE j.requirements IS NOT NULL
            """)

            jobs = cursor.fetchall()

            for job in jobs:
                requirements = job['requirements']

                # Convert JSON text into a Python dictionary
                if isinstance(requirements, str):
                    requirements = json.loads(requirements)

                if not isinstance(requirements, dict):
                    continue

                required_skills = {
                    skill.strip().lower()
                    for skill in requirements.get('skills', requirements.get('required_skills', []))
                    if isinstance(skill, str)
                }

                if not required_skills:
                    continue

                matched_skills = user_skills.intersection(required_skills)

                score = round(
                    len(matched_skills) / len(required_skills) * 100
                )

                matches.append({
                    'job_title': job['job_title'],
                    'company_name': job['company_name'],
                    'score': score,
                    'matched_skills': sorted(matched_skills),
                    'required_skills': sorted(required_skills)
                })

            # Highest matching score first
            matches.sort(key=lambda item: item['score'], reverse=True)

        finally:
            cursor.close()
            connection.close()

    return render_template(
        'job_match.html',
        matches=matches,
        entered_skills=entered_skills
    )






















































if __name__ == '__main__':
    app.run(debug=True)

