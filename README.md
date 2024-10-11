# API
In order to start using this app, you will need to create a virtual environment, git clone the project:

```
$ git clone https://github.com/Darius254/API
```

And then run the following command to install the dependencies:

```
$ pip install -r requirements.txt
```
Then make migrations by running:

```
$ python manage.py makemigrations
```

Also migrate the project:

```
$ python manage.py migrate
```
Now, you should create a superuser so that you can add the images and products from the admin panel:

```
$ python manage.py createsuperuser
```
Now enter you desired username, password and email for logging in as admin.
And finally run the project by running:

```
$ python manage.py runserver
```
 
