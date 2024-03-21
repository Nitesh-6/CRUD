BASIC CRUD 
This project is a simple Django application that demonstrates basic CRUD (Create, Retrive, Update, Delete) operations using a form and a model.

Getting Started
Dependencies
Python 3.x
Django 3.x
Installing
Clone the repository:

git clone https://github.com/Nitesh-6/CRUD.git
Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate (on Linux/macOS)
venv\Scripts\activate (on Windows)
Install the required packages:

pip install -r requirements.txt
Perform the initial database migration:

python manage.py migrate
Run the development server:

python manage.py runserver
Access the application at http://127.0.0.1:8000/

Project Structure
models.py: Defines the Details model, which stores user details.

forms.py: Defines the MyForm form, which is used to create and update Details objects.
views.py: Contains the views for the application, implementing the CRUD operations.
templates: Contains the HTML templates used in the application.
Usage
Create Record: A user with the First Name 'first name', Last Name 'last name', username 'unique_username', city 'your city', state 'your state', pincode 'pincode' will be created if it doesn't exist.

Get User: Display all user objects.

Process Data: Create or update a Details object using the provided form.

Get Details: Display all Details objects.

Delete Record: Delete a Details object by its ID.

Update Content: Update a Details object by its ID.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

Contact
Sai Nitesh - sainitesh6@gmail.com

Project Link: https://github.com/Nitesh-6/CRUD
