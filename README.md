# Django Blog App

The idea was to build a basic blogging platform.

It was made using Python 3.8.1 and Django 3.0.5<br/>
For Database, I've used PostgreSQL.<br/>
Bootstrap 4 alongside with CSS used for primary styling.

## Features

### Blog

- User can create new blog post
- User can manage(Update/Delete) his/her own post
- Create/Update post uses rich text editor tinyMCE
- Comments for post available with Disqus
- Pagination and Read More button available
- Post filter by User

### Users

- Anyone can open account with email address
- User can add/update profile pictures
- Can change name and add Bio
- Password reset available.

## Prerequisites

```
asgiref==3.2.7
autopep8==1.5.2
Django==3.0.5
django-cleanup==4.0.0
django-crispy-forms==1.9.0
django-tinymce==3.0.2
Pillow==7.1.2
psycopg2==2.8.5
pycodestyle==2.5.0
python-decouple==3.3
pytz==2019.3
sqlparse==0.3.1

```

\*Note: You can ignore "psycopg2==2.8.5" if you want to use SQLite for database instead of PostgreSQL.<br/> Later I'll show how you'll replace PostgreSQL with SQLite.

## Installation

If you want to test my project or do whatever you want, here's a little guide:

### Cloning Repository

First clone this repository using git clone into your local machine:

```
$ git clone https://github.com/rsupanta/django-blog.git
```

### Setting up Project Environment

I have used "pipenv" virtual environment in my project.<br/>
Install "pipenv" if you haven't had it yet.

```
$ pip install pipenv
```

Then open Command-line in the root of the project directory where the Pipfile is located.<br/>

Run this command:

```
pipenv install
```

This usually installs all dependencies.<br/>
Then run:

```
pipenv shell
```

This will activate the environment.<br/>
Check all dependencies by run:

```
pip freeze
```

If automate installation misses any package, then install that specific package manually using

```
pipenv install (package name)
```

\*If you want to use "virtualenv" instead of "pipenv", I've already included "requirements.txt".<br/>
So all you have to do is make a virtualenv with python 3.8.1 and run this command:

```
$ pip install -r requirments.txt
```

<!-- Run the Test -->

### Modifying 'settings.py'

I have used environment variable to hide my credentials in
django-blog>settings.py <br/>
So you have to replace those with your own.<br/>
If you want to use the environment variable, simply create a ".env" file in root of project directory where "manage.py" is located and add this lines below:

```
SECRET_KEY =Your own generated key
DB_NAME = Postgres DB Name
DB_USER = Postgres User
DB_PASSWORD = Postgres DB password
DB_HOST = Postgres DB Host
DB_PORT = Postgres DB Port
EMAIL_HOST_USER = Email address
EMAIL_HOST_PASSWORD = Generated app key
```

You can generate Django 'SECRET_KEY ' by a simple google search.<br/>
You can ignore Postgres DB variables if you want to stick with default SQLite<br/>
I'm using Gmail for mailing.<br/>
Generate a Gmail app password and put it here.<br/>

\*If you want to use SQLite, replace this portion in "settings.py":

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```

with this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### Migrations

You need to migrate the whole project.<br/>
Run commands below one by one:

```
$ python manage.py migrate
$ python manage.py makemigrations blog
$ python manage.py makemigrations users
$ python manage.py migrate
```

### Django Admin

Now it's time to create a superuser.<br/>
Run this command:

```
$ python manage.py createsuperuser
```

Enter your desired username and press enter.

You will then be prompted for your desired email address.

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

### The Final Step

Finally, you're at the bottom!<br/>
After Superuser created successfully, run Django-server:

```
$ python manage.py runserver
```

If everything above goes well, you'll see this:

```
Django version 3.0.5, using settings 'django-blog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Go to the web browser, visit http://localhost:8000/ and start testing the app.<br/>

Admin panel available at http://localhost:8000/admin/ login using superuser credentials that you've created earlier.

### Thanks for your time.
