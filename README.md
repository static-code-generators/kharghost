# kharghost

A blogging platform, á la [ghost](https://github.com/tryghost/Ghost)

### Running instructions

Create a virtualenv
`virtualenv venv`

Activate it
`source venv\bin\activate`

Clone the repo, cd into it, and install requirements
`pip install -r requirements.txt`

Make migrations and runserver <br>
`python manage.py makemigrations blog` <br>
`python manage.py migrate` <br>
`python manage.py runserver` <br>
