# kharghost

A blogging platform, á la [ghost](https://github.com/tryghost/Ghost)

### Running instructions

(Prerequisites: Python 3)

Create a virtualenv  
`virtualenv -p /usr/bin/python3 venv`

Activate it  
`source venv/bin/activate`

Clone the repo, cd into it, and install requirements  
`pip install -r requirements.txt`

Copy the local_settings file if you want to run the server locally  
`cp local_setttings_sample.py local_settings.py`

Make migrations (delete any existing db.sqlite3 file before)  
`python manage.py makemigrations blog`  
`python manage.py migrate`  

Create an admin user  
`python manage.py createsuperuser`

Run the server and achieve glory  
`python manage.py runserver`  

Go to `localhost:8000/admin` and login with your credentials  
Create users for blog authors, and start bloggin' away :)
