# Instructions for running

## First Time Setup
1. You need to have poetry installed. Install using `python -m pip install poetry`
2. After poetry is installed, run the command `poetry shell`.
3. After the shell has been initialized, run `poetry install` to install all the dependencies.
4. After the dependencies are installed, run `python manage.py makemigrations` followed by `python manage.py migrate`
5. After the migration has finished use, `python manage.py createsuperuser` to create an admin user.
6. After creating the user, run the server using command `python manage.py runserver`.
7. Then go to `localhost:8000/admin`. Login using the credentials you just created!
8. After logging in, click the `Users` tab on the sidebar. Then click on your username.  Then click on `Additional Info` and tick the `Is Company` and untick the `Is User` checkbox.
9. That's it you are done!

## Running steps
1. Use `python manage.py runserver` to run the server.
2. The site will be hosted on `localhost:8000`.

## Approving the Job Listing
1. Click on Job Listing on the left sidebar
2. Click on the Job you wanna approve. Then go to Salary and Approval and check the `Is Approved` checkbox and save.
3. That's it, you are done!