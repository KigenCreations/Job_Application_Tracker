# AI Usage Documentation

## Tools Used

### ChatGPT (OpenAI)

I used ChatGPT throughout the development of CareerTrack as a guide, debugging assistant, and learning tool. I mainly used it when I got stuck, needed help understanding Python functions, Flask routes, SQL queries, or wanted something explained in simpler terms.

I also used ChatGPT to help organize my notes and break down complicated code into smaller steps so I could better understand what each function was doing.

A good portion of the assistance involved HTML and CSS. I wanted the website to have a specific design, but getting everything to look consistent was more difficult than expected. There was a lot of back and forth trying different CSS rules, fixing layouts, adjusting buttons, and figuring out why some changes were not working.

Some suggestions worked immediately, while others created new problems or conflicted with existing CSS. I had to go back, review the code, remove unnecessary rules, and test things again. It was definitely a trial-and-error process.

### Canva

I used Canva as a graphic design tool to create and prepare visual elements for the website. This helped me add a more personal look to CareerTrack instead of relying only on basic text and colors.

### Grammarly

I used Grammarly to help review grammar, spelling, sentence structure, and clarity in my written documentation. It was mainly used to improve how I explained things, rather than for programming.

### How I Used These Tools

My main purpose for using these tools was to support my learning and help me complete the project when I ran into problems.

Instead of only asking for finished code, I often asked for explanations, troubleshooting steps, and guidance on where changes needed to be made. I worked through the suggestions in PyCharm, tested the application in my browser, and returned with errors or screenshots whenever something did not work.

I also used AI assistance to help understand what I was building, not just how to make it work. Breaking down functions into everyday language was especially helpful when reviewing the Python and database portions of the project.


## Key Prompts

Throughout the project, I used ChatGPT to ask questions, understand code, and troubleshoot problems. Most of my prompts were conversational, and I often followed up with screenshots, code, or error messages.

Some examples of the types of prompts I used include:

- Understanding the code: "Can you explain what this function does in simple terms?" and "Can we break this down step by step so I understand what is happening?"

- Flask and MySQL: Asking for help understanding how Flask routes connect to the database, how information moves between Python and HTML, and how to troubleshoot problems when something does not work.

- HTML and CSS: "Why is this not working?" and "Can we make all the pages look the same?" I also asked for help fixing form layouts, dropdown menus, calendar icons, and buttons.

- Debugging: "Something is not adding up, because it is not working." I shared my existing code so we could identify conflicting CSS rules instead of continuing to add more changes.

- Website design: Asking how to apply my chosen neon color scheme, create consistent two-column forms, and make Edit and Delete buttons match across the different pages.

- Documentation and notes: Asking for explanations in everyday language, help organizing information, and guidance on documenting my work.

Many prompts were followed by additional questions because the first suggestion did not always solve the problem. I used that back-and-forth process to test changes, understand errors, and make adjustments to the application.


## What Worked Well

One of the most helpful things about using ChatGPT was being able to ask questions without needing to understand all the technical terms first. When I had trouble understanding a Python function, SQL query, or Flask route, I could ask for an explanation in simple English. Breaking things into smaller steps made it easier to follow what the code was supposed to do.

The step-by-step guidance was especially useful when working with the database and connecting it to the website. Instead of trying to understand the entire application at once, I could focus on one function, test it, and then move to the next. I also used these explanations to take notes and review what I had learned.

Another thing that worked was using screenshots and sharing my actual code when something went wrong. This was particularly helpful with CSS, although it took several attempts to get things right.

For example, I wanted all the Edit and Delete buttons to match across the website. What seemed like a simple design change turned into several rounds of troubleshooting. We kept adjusting the CSS, but the buttons still looked different. At one point, I literally said, "Something is not adding up, because it is not working." Eventually, reviewing the existing CSS and HTML helped identify conflicting rules and missing classes.

The dropdown menus were another adventure. I wanted neon pink arrows, but the first CSS approach made them disappear. I ended up using my own image instead. Even then, the image worked when opened directly in the browser but did not appear inside the dropdown. This helped me understand how CSS rules can override each other.

I also found the visual design assistance useful. I had a specific retro-inspired color scheme in mind, and the guidance helped me apply it across the different pages. Canva was useful for preparing the graphics, while Grammarly helped me review the wording in my documentation.

Overall, what worked best was the combination of explanations, testing, screenshots, and repeated adjustments. Not every suggestion worked immediately, but the process helped me understand more about debugging and how the different parts of a web application work together.


## What I Modified

One of the biggest adjustments I made was how I approached building the application. Instead of trying to complete everything at once, I worked on each page individually using a repeated process: create, test, fix, and test again.

I started with the basic functionality of each section, then gradually added features such as viewing, adding, editing, and deleting records. Testing each feature before moving forward helped me understand how the different parts of the application were connected.

There were several instances where updating one file caused errors because another file had not been updated to match. For example, I would make changes to an edit_xxxxx.html template but forget that the corresponding route in app.py also needed changes, or vice versa. The page might look correct, but the function would not work as expected.

These situations helped me understand the relationship between Flask routes, HTML templates, and the MySQL database. I learned that a change in one part of the application can affect another, even when the files are completely separate.

I also reviewed and adjusted suggested code to match my existing database tables, field names, and application structure. When something did not work, I would share the error, review the explanation, make corrections, and test again.

For the visual design, I made smaller adjustments to the suggested HTML and CSS until the pages matched what I wanted. I did not keep every suggestion, especially when it caused conflicts with existing styles.

Overall, I modified both the code and my development approach as I progressed. Building CareerTrack one section at a time helped me understand how the application worked instead of just focusing on getting a finished result.


## Lessons Learned

One of the biggest things I learned from this project was the importance of testing as I go. Building CareerTrack one section at a time helped me understand how Python, Flask, HTML, and MySQL work together. I learned that just because a page displays correctly does not necessarily mean the backend is working.

Something that really helped was keeping MySQL Workbench open alongside PyCharm. Whenever I added, edited, or deleted information through the website, I could check the database directly to confirm that the changes were actually being saved. This helped me understand how data moves between the website, the Python code, and the database. It also made troubleshooting easier because I could identify whether a problem was happening on the webpage or in the database.

Another important lesson was learning when to stop adding code and start cleaning it up. This was especially true with CSS. At first, when a style did not work, I would comment out the unwanted code and add another rule somewhere else. Eventually, I had so many old rules, overrides, and commented sections that it became difficult to tell which styles were actually being used.

I learned that keeping every failed attempt is not always helpful. Sometimes I needed to delete the unnecessary code instead of leaving behind a graveyard of dead CSS and continuing to build on top of it. Cleaning up the stylesheet made it easier to understand, maintain, and troubleshoot.

I also learned that AI suggestions are not always correct, even when they sound confident. There were times when a suggested fix worked immediately, but there were also times when it created another problem. This taught me to test the code, question the results, and provide more context when asking for help.

Using ChatGPT to explain functions in simple terms was especially helpful. I realized that understanding why something works is more useful than just knowing what code to copy. Taking notes and asking follow-up questions helped me become more comfortable reading and modifying the application.

Finally, I learned that programming involves a lot more trial and error than I expected. Sometimes fixing one thing breaks another, and sometimes the solution is simply removing something that should not have been there in the first place.

Overall, this project helped me become more comfortable with debugging, working across multiple files, and checking my own work. AI was a useful learning tool, but I still needed to make decisions, test suggestions, recognize mistakes, and understand the results.

















