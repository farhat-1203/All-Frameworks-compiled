# integrating html file with Flask application
# Jinja 2 template engine is used to integrate the HTML file with the Flask application.


from flask import Flask, render_template

app = Flask(__name__)  

@app.route('/')
def welcome():
    return "<html><H1>Hello World! This is the home page of the Flask application</H1></html>."

@app.route('/index')    
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)



# the render_template() function is used to redirect to that particular html file
# which is present in the templates folder of the Flask application. (templates folder is created in the same directory where the main.py file is present)
# in this case, it is index.html file present in the templates folder and so the server will be redirected to this index.html file


