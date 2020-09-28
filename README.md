# AlphaMiniSupport
Simple interface to modify messages for usage in an Alphamini service robot by [UBITECH](https://www.ubitech.eu/).

## Deploying to server
Steps to deploy to server. (Note that we are assuming a server running a Linux OS)


1. Please install a [Postgres](https://www.postgresql.org/download/) database, [Apache Web Server](https://httpd.apache.org/download.cgi) and [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/installation.html) package. The
database is required to create users, store the message and login sessions. Apache is the web server and mod_wsgi is
required for Apache to interface with this (Python) application. 
1. Once the database is created, you will need to create a database in Postgres along with users with read-write acess to this newly created database. You might require superuser privileges
to your database for this operation. Note down the
database __hostname__ (usually _localhost_), database __name__, __username__ and __password__. By default, postgres uses port 5432. If you deploy postgres on a different port, then note this number down as well.  
1. Install python version >= 3.8. 
2. Download this repository and `cd` into the project directory. 
3. Create a python virtual environment in this directory. 
    - Install the `virtualenv` package using `pip install virtualenv`  . 
    - Create the virtual enviroment with `virtualenv <myenv>` where `<myenv>` is a name of your choosing. 
    - Activate the environment with `source myenv/bin/activate`
3. Run `pip install -r requirements.txt`
4. You will need to generate a secret key and use it to set the SECRET_KEY environment variable. For 
convience use this command 

    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

    Copy the output of this command and paste it in 

    ```bash
    export SECRET_KEY=<pasted key>
    ```

5. Execute the following steps. Let `mydomain.com` be the domain name of the server hosting the application.

    ```bash
    # Export host ip address 
    export ALLOWED_HOSTS='mydomain.com'

    # Export database information 
    export DB_HOST=<database-server-name>
    export DB_NAME=<database-name>
    export DB_USER=<database user>
    export DB_PASSWORD=<database user password>
    export DB_PORT=5432

    # Alias python (optional step if the below doesn't work)
    alias python=myenv/bin/python 

    # Build database tables
    python manage.py migrate

    # Create root user
    python manage.py createsuperuser
    ```

5. Further instructions on how to configure Apache and `mod_wsgi` are found here.

    a. Installing and activating  `mod_wsgi`. Go [here](https://modwsgi.readthedocs.io/en/develop/). 

    b. Configure Apache server `http.conf` file. Go [here](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/)

    c. Configure Apache server to serve application static files. Instructions [here](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/#serving-files). The path to static files for this application are `./static`. 

6. Activate the Apache server. 

## Creating users, permissions and user tokens
Now navigate to `http://<mydomain.com>/admin` and login with root credentials created with the `createsuperuser` command earlier. Complete the deployment by creating users, permission groups and generating API tokens for applications 
which consume the message api. 

It is suggested to create an application only user with view permissions only. Associate an access token to this user. The robot will need this
access token to read the message. You will need to 
pass this token to whomever is writing the code for the Alpha mini robot. 

## Consuming the message API
The Alphamini robot can get the message by making a GET request to `http://mydomain.com/api/v1/messages/1` and including the `Authenticate: Bearer <API-token>`
header.

## Updating the message
Staff users can navigate to the home site at `http://mydomain.com/` and login to access a form where the message can be updated. 
