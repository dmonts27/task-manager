# Task Manager

## Description
This is a Flask-based Task Manager web application that allows users to add, view, and delete tasks. It features a simple and user-friendly interface built with HTML, CSS, and JavaScript. The app stores tasks in a MySQL database.

## Features
- Add new tasks to the list.
- View all tasks in a list.
- Delete tasks from the list.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Database**: MySQL
- **Version Control**: Git, GitHub

## Installation and Setup Instructions

### Prerequisites:
- **Python 3.x** installed on your machine.
- **MySQL** installed and running.

### Setup:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/dmonts27/task-manager.git

### Create and activate a virtual environment: On Windows:
- python -m venv venv
- venv\Scripts\activate

### Install the required dependencies:
- pip install -r requirements.txt

### Set up the MySQL database:
- Create a MySQL database (e.g., task_manager_db).
- Update the database configuration in app.py or config.py with your MySQL credentials.

### Run the application:
- python app.py

### Access the app:
- Open your web browser and go to http://127.0.0.1:5000/ to view the Task Manager app.

### Project Structure:
- app.py: Main Flask application.
- config.py: Contains the MySQL database configuration.
- static/: Contains static files like CSS.
- templates/: Contains HTML templates.
- requirements.txt: Python dependencies.
