---OZQ online shopping application for ESOFT HND assignment---

very simple web application made using mainly fastAPI framework. features includes users can register,login
browser products, add them to carts and post feedback

-- Features --

-JWT- based authetication ( 5 hours per session (300 minutes) session time can be changed by changing 
variable ACESS_TOKEN_EXPIRE_MINUTES variable  in app/oauth2.py
-password hashing using bycrypt
-simple REST APIs uses POST, GET
-Jinja2 templates for front end
-PostgresSQL for database SQLAlchemy for ORM
-Oauth2 Password requestform for login

--- requirements---

-python 3.9 +
-postgreSQL

--- How to setup ---

--database--

1. Install PostgreSQL from https://www.postgresql.org/download/ and make sure the PostgreSQL
is running on the default port (5432).(open pgadmin4 right click server > properties > connection
2. create database named "ozqdatabase" in that server use username - "postgres" and password - "0000"

- if you are using different SQL client and not postgreSQL-
1. makesure SQL alchemy supports it and install supporting driver library
2. change the connection string on main/database.py to match your SQL client, server and database

-- setting up python --

1. set up a python environment (optionaal)
2. run "pip install requirements.txt" in terminal

-- launch the application--

1. run "uvicorn app.main:app" in cmd
2. ctrl click the http looks something like this http://127.0.0.1:8000. it will open this on web browser
3. in browser navigate to http://127.0.0.1:8000/home


--- Documentation ---

5. to acess swagger docs navigate to http://127.0.0.1:8000/docs
6. to acess ReDocs navigate to  navigate to http://127.0.0.1:8000/redoc




