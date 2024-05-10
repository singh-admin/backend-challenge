# Project Setup Instructions

## Requirements
To run this project locally, ensure you have the following installed on your system:
- Python (version 3.9)
- Virtualenv 

## Setup Instructions
Follow these steps to set up and run the project locally:

1. Clone the repository:
   git clone <https://github.com/singh-admin/backend-challenge.git>
   cd backend-challenge

2. Create a virtual environment.
   python -m viryualenv env

3. Activate the virtual environment:
   env\Scripts\activate

4. Install project dependencies:
   pip install -r requirements.txt

5. change directory:
   cd Assignment

6. Apply database migrations:
   python manage.py migrate

7. Run the development server:
   python manage.py runserver

  
Note: Created 2 users with the `python manage.py shell` command with the `is_staff` flag set to `True` 
credential: 
username: singh
password: 1234

username: singh2
password: 0000

# Test CRUD Operations For Task Model.

# POST
1. POST: Create a new task
   http://127.0.0.1:8000/tasks/  Post

2. include Authorization.(Type: Basic Auth)
   username: singh
   password: 1234

3. Request Body (JSON)
   {
    "title": "Task 1",
    "description": "task created"
   }

# GET
1. GET: Retrieve tasks
   http://127.0.0.1:8000/tasks/

   # Custom filter retrieving only user-related objects for tasks
   http://127.0.0.1:8000/tasks/my-tasks/

2. include Authorization.(Type: Basic Auth)
   username: singh
   password: 1234

# PUT
1. PUT: Update an existing task (replace <task-id> with the actual task ID)
   http://127.0.0.1:8000/tasks/3/

2. include Authorization.(Type: Basic Auth)
   username: singh
   password: 1234

3. Request Body (JSON)
   {
    "title": "Task 1",
    "description": "task updated"
   }

# DELETE
1. DELETE: Delete an existing task (replace <task-id> with the actual task ID)
   http://127.0.0.1:8000/tasks/4/

2. include Authorization.(Type: Basic Auth)
   username: singh
   password: 1234



# Test CRUD Operations For Labels Model.

# POST
1. POST: Create a new Label
   http://127.0.0.1:8000/labels/  Post

2. include Authorization.(Type: Basic Auth)
   username: singh
   password: 1234

3. Request Body (JSON)
   {
    "name": "python",
    "owner": 1
   }

# GET
1. GET: Retrieve labels
   http://127.0.0.1:8000/labels/

   # Custom filter retrieving only user-related objects for labels.
   http://127.0.0.1:8000/labels/my-labels/

2. include Authorization.(Type: Basic Auth)
   username: singh
   password: 1234

# PUT
1. PUT: Update an existing labels (replace <label-id> with the actual label ID)
   http://127.0.0.1:8000/labels/2/

2. include Authorization.(Type: Basic Auth)
   username: singh
   password: 1234

3. Request Body (JSON)
   {
    "name": "python_django",
    "owner": 2
   }

# DELETE
1. DELETE: Delete an existing label (replace <label-id> with the actual label ID)
   http://127.0.0.1:8000/labels/2/

2. include Authorization.(Type: Basic Auth)
   username: singh
   password: 1234



# Note: Test the models.
  python manage.py test tasks.tests.test_models

