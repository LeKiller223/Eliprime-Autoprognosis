# Car Engine Diagnostic Website

This is a Django web application for diagnosing car engine issues and providing suggested actions based on the symptoms provided by the user.

## Features

- Allows users to submit engine symptoms for diagnosis.
- Provides diagnostic result and suggested actions.
- Responsive and user-friendly interface.

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap

## Installation

1. if the file is extracted in the download folder:
- open cmd 
- cd Downloads
- cd eli
- venv\Script\activate.bat
- cd eliprime_project
- pip install -r requirements.txt

2. Run the development server:
- python manage.py runserver

3. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Navigate to the homepage.
2. Click on "Get Started" to submit engine symptoms for diagnosis.
3. Fill out the form with the required information.
4. Click on "Submit" to see the diagnostic result and suggested actions.

4. Access the application admin in your web browser at `http://localhost:8000/admin`.
 - but before you have to create a user user
   
   python manage.py createsuperuser

   then follow the prompt to create your credntials.
   after that then you admin dashboard at `http://localhost:8000/admin`.

