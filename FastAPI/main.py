# import necessary modules and libraries
from fastapi import FastAPI
import uvicorn  # ASGI server to run FastAPI application

# create FastAPI application object (named "app")
app = FastAPI()  

# function to return the response for root endpoint
@app.get("/")  # define a GET endpoint at the root URL
def index():
    return {"message": "Hello, World! This is the home page of the FastAPI application."}  

# fine another endpoint named /Welcome that returns a welcome message
@app.get("/Welcome")  # define another GET endpoint at /Welcome
def welcome():
    return {"message": "Welcome to the FastAPI application!"}


# entry point of the application (to run any .py file)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# To run the FastAPI application, use the following command in the terminal:
# uvicorn main:app --reload  
# Here, 'main' is the name of the Python file (main.py) and 'app' is the FastAPI application object.
# the name will change based on the filename and the app name that is created in that file.
# The --reload flag enables auto-reload for code changes during development. (just like debug=True in Flask)

# fastapi also provides an automatic interactive API documentation at /docs and /redoc endpoints.
# i have personally found swagger UI (/docs) more user-friendly.
# other way round, u can access any html file using FastAPI's this method called /docs since swagger UI is basically an HTML file.
# For example, if the FastAPI application is running locally, you can access it at:
# http://127.0.0.1:8000
# and according to the above code, the docs will be at:
# http://127.0.0.1:8000/docs


"""
FastAPI as the name itself suggests is a fast framework compared to Flask and Django. (and it somewhere falls between these two in terms of features)
unlike in flask where u have to define routes using decorators, 
in FastAPI u can define routes using function decorators as well as using path operations.
one more major difference is that FastAPI is built on ASGI (Asynchronous Server Gateway Interface)
whereas Flask is built on WSGI (Web Server Gateway Interface).
the simple difference between ASGI and WSGI is that ASGI supports asynchronous programming that means it can handle multiple requests at the same time
whereas WSGI is synchronous and can handle only one request at a time.
like for example, if a request takes time to process in WSGI, the server will be blocked until the request is completed.
but in ASGI, the server can handle other requests while waiting for the long request to complete.
one real world example of this is when u have to fetch data from a database or an external API;
in such cases, FastAPI can handle other requests while waiting for the database or API response,
whereas Flask will be blocked until the response is received.
this makes our FastAPI applications more efficient and faster compared to Flask applications ....!
"""