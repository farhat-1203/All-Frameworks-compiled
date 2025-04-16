# basic structure of any Flask application. ***
# WSGI application (Web Server Gateway Interface) is the basic structure of any Flask application.
# Import the Flask class from the flask module
from flask import Flask

'''
Creates an instance of the Flask class,
which is the WSGI application.
(Basic UI for the web application)
'''
app = Flask(__name__)   # wsgi application


@app.route('/')  # decorator to tell Flask what URL should trigger the function
# function to return the response
def welcome():
    return 'Hello World! This is the home page of the Flask application.'

@app.route('/index')
def index():
    return 'This is the index page of the Flask application.'

# this shows that we can create multiple routes in a single application.

#entry point of the application (to run any .py file)
if __name__ == '__main__':
    app.run(debug=True)  # run the application in debug mode
 
   # debug=True allows the server to automatically restart when the code changes, 
   # enabling the developer to see the changes in real-time just by refreshing the window and not by restarting the server each time.

   # for example, if any changes are made in the function welcome(), 
    # then the server will automatically restart when the code changes,
    # and the changes will be reflected in the browser just by refreshing the window.

