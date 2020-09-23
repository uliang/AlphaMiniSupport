# AlphaMiniSupport
Simple interface to modify messages for usage in an Alphamini service robot by [UBITECH](https://www.ubitech.eu/).

## Deploying to localhost
Steps to deploy to localhost. 

Please prepare

1. A python virtual environment and activate it. Python version is at least 3.8. 
2. Clone this repository and `cd` into the cloned directory. 
3. Run `pip install -r requirements.txt`
4. You will need to generate a secret key and use it to set the SECRET_KEY environment variable. 

The application uses sqlite3 which is a simple disk based database solution. It comes with python so no additional installation is required. 

Execute the following steps.

```bash
# Build database tables
python manage.py migrate

# Create root user
python manage.py createsuperuser

gunicorn -b 0.0.0.0 AlphaMiniSupport.wsgi
```

Ensure that both the Alphamini robot and host machine are located on the same WiFi network. 

Let `<ip-add>` denote the IP address of the host machine.

Now navigate to `<ip-add>:8000/admin` and login with root credentials created with the `createsuperuser` command earlier. Complete the deployment by creating users, permission groups and generating API tokens for applications 
which consume the message api. 

## Consuming the message API
The Alphamini robot can get the message by making a GET request to `<ip-add>:8000/api/v1/messages/1` and including the `Authenticate: Bearer <API-token>`
header.

## Updating the message
Staff users can navigate to the home site at `<ip-add>:8000/` and login to access a form where the message can be updated. 
