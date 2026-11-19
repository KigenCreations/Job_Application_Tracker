# CareerTrack
### Job Application Tracking System

CareerTrack is a web-based job application tracking system developed for the COP 4751 Advanced Database Management course at Florida International University (FIU).

The application helps users organize and manage their job search in one place. Users can track companies, job opportunities, applications, and professional contacts through a simple web interface.

CareerTrack also includes a Job Match feature that compares a user's skills with the skills required for available job opportunities.

The project was developed using Python, Flask, MySQL, HTML, and CSS. It demonstrates database relationships, CRUD operations (Create, Read, Update, Delete), and the connection between a web application and a relational database.


## Main Features

CareerTrack includes six main sections:

### 1. Dashboard
- Displays an overview of the job tracking system.
- Shows summary statistics for companies, jobs, applications, and contacts.
- Provides a quick view of application activity.

### 2. Companies
- Add, view, edit, and delete company records.
- Store company information for organizing job opportunities.

### 3. Jobs
- Add, view, edit, and delete job listings.
- Connect job opportunities to companies.
- Track job details, requirements, salary ranges, and posting dates.

### 4. Applications
- Add, view, edit, and delete job applications.
- Track application dates, statuses, and resume versions.
- Associate applications with existing job listings.

### 5. Contacts
- Add, view, edit, and delete professional contacts.
- Store contact information, job titles, and notes.
- Associate contacts with companies.

### 6. Job Match
- Enter skills to compare against job requirements.
- Calculate skill match percentages.
- Display matching skills and job opportunities.


## Technologies Used

CareerTrack was developed using the following technologies:

- **Python:** Main programming language used for the backend.
- **Flask:** Web framework used to handle routes, requests, and communication between the frontend and backend.
- **MySQL:** Relational database used to store and manage application data.
- **MySQL Connector/Python:** Connects the Flask application to the MySQL database.
- **HTML:** Structures the website pages and forms.
- **CSS:** Controls the website's appearance, layout, and styling.
- **Jinja2:** Flask's template engine, used to display dynamic data in HTML pages.
- **python-dotenv:** Loads environment variables for database configuration.

### Development Tools

- **PyCharm:** Used to write, organize, run, and debug the Python application.
- **MySQL Workbench:** Used to create, manage, and verify database records.
- **Git and GitHub:** Used for version control and project submission.
- **Canva:** Used to prepare visual elements for the website.


## Installation and Setup Instructions

Follow these steps to install and run CareerTrack locally.

### 1. Prerequisites

Make sure the following software is installed:

- Python 3
- MySQL Server
- MySQL Workbench (recommended)
- Git

### 2. Download the Project from GitHub

- Open the CareerTrack GitHub repository.
- Click the green Code button.
- Select Download ZIP.
- Save the ZIP file to your computer.
- Extract (unzip) the downloaded file.

Open the downloaded project folder:


### 3. Open the Project in PyCharm

- Open PyCharm.
- Select File > Open.
- Locate the extracted Job_Application_Tracker-main folder.
- Select the folder and open it as a project.

### 4. Set Up the Python Virtual Environment

When the project opens, PyCharm may display a message indicating that no Python interpreter is configured.

- Open requirements.txt.
- Click Create a virtual environment using requirements.txt when prompted.
- PyCharm will create a .venv folder and install the required Python packages.

### Alternative: Manual Installation

If PyCharm does not offer automatic setup, configure a Python interpreter and virtual environment first. Then open the PyCharm terminal and run:

```bash
python -m pip install -r requirements.txt
```
### 3. Install Python Dependencies

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Set Up the MySQL Database

1. Open MySQL Workbench and connect to your local MySQL Server.
2. Open the included `schema.sql` file.
3. Execute the SQL script to create the database and its tables.
4. Confirm that the `job_tracker` database contains the following tables:
   - companies
   - jobs
   - applications
   - contacts

### 5. Configure Environment Variables

Create a file named `.env` in the project's main directory.

Add your local MySQL connection settings:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_MYSQL_PASSWORD
DB_NAME=job_tracker
```

Replace `YOUR_MYSQL_PASSWORD` with your own MySQL password.

The `.env` file contains private database credentials and should not be uploaded to GitHub.

### 6. Run the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

http://127.0.0.1:5000

You should now be able to access CareerTrack and its main features.

## Project Demonstration Video

Watch the CareerTrack final project demonstration here:

[CareerTrack Video Demonstration]
https://youtu.be/_xAJMnbDN7M 





















