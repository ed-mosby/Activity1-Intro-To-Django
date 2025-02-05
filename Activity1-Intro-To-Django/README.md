# Intro to Django

## Student Information
- **Full Name:** Edgar Villaraza Jr.
- **USN:** 18003229400
- **Course Code:** ITE6200

## Project Description
This is a basic Django project that serves as an introduction to the Django framework. It includes:
- A simple homepage displaying the student's name and a short bio.
- Basic Django structure (views, templates, URL routing).

## How to Run the Project
1. Install Django using:
   ```
   pip install django
   ```
2. Navigate to the project directory:
   ```
   cd simple_django_portfolio
   ```
3. Run the Django development server:
   ```
   python manage.py runserver
   ```
4. Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## How to Upload to GitHub
1. **Create a GitHub Repository**  
   - Go to [GitHub](https://github.com/) and log in.  
   - Click the **+** sign in the top-right corner and select **New Repository**.  
   - Enter a repository name (e.g., `Intro-to-Django`).  
   - Set it as **public** or **private** and click **Create repository**.

2. **Upload the Project**  
   - Open your **terminal** or **Git Bash** and run these commands:

   ```sh
   cd path/to/extracted_folder  # Navigate to the project folder
   git init  # Initialize Git
   git add .  # Add all project files
   git commit -m "Initial commit"  # Create a commit
   git branch -M main  # Set the main branch
   git remote add origin YOUR_REPO_URL  # Connect to GitHub repository
   git push -u origin main  # Upload files to GitHub
   ```
   Replace `YOUR_REPO_URL` with your actual GitHub repository link.

3. **Verify on GitHub**  
   - Go to your repository on GitHub and refresh the page.  
   - Your project files should now be uploaded! 🎉

## Notes
- If you encounter errors, ensure you have [Git installed](https://git-scm.com/downloads).
- To stop the Django server, press `CTRL + C` in the terminal.
