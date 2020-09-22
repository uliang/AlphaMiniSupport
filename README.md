# AlphaMiniSupport
Simple interface to modify messages for usage in an Alphamini service robot by [UBITECH](https://www.ubitech.eu/).

## Deploying to Azure
A complete deployment solution will include provisioning of: 

1. An Azure Web Service instance. 
2. Azure storage account to serve static files 
3. Postgres database. 

You will need to supply environment variables STATIC_URL, DB_NAME, DB_HOST, DB_PORT, DB_PASSWORD and DB_USER. 

Once Azure has the web application container running, the following steps need to be executed 

```bash
# source code is located in this directory
cd site/wwwroot

# Activate Ant Environment
source /antenv/bin/activate

/antenv/bin/python manage.py migrate
/antenv/bin/python manage.py createsuperuser
```

Now navigate to `<app-name>.azurewebsites.net/admin` and login. Complete the deployment by creating users, permission groups and generating API tokens for applications 
which consume the message api. 

## Consuming the message API
The Alphamini robot can get the message by making a GET request to `<app-name>.azurewebsites.net/api/v1/messages/1` and including the `Authenticate: Bearer <API-token>`
header.

## Updating the message
Staff users can navigate to the home site and login to access a form where the message can be updated. 
