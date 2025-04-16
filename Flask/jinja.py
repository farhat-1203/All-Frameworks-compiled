# Jinja 2 Template Engine
# Building URLs dynamically in Flask
# Variable Rules


from flask import Flask, render_template, request
from flask import redirect, url_for
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/index')  
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}! Your form has been submitted successfully."
    return render_template('form.html')

# Variable Rules
@app.route('/userName/<string:name>')
def userName(name):
    return f"Hello {name}!"
# Here, the URL rule is /userName/<name>, where <name> is a variable part of the URL. 
# The function user() accepts the name as an argument and returns the message Hello <name>!.
# The string ensures that the variable part of the URL is a string and not an integer.


@app.route('/userAge/<int:age>')
def userAge(age):
    return "Your age is " +str(age)
# Here, the URL rule is /userAge/<age>, where <age> is a variable part of the URL.
# The function userAge() accepts the age as an argument and returns the message Your age is <age>!.
# The int converter is used to convert the variable part of the URL to an integer.
# +str(age) is used to concatenate the string with the integer value.


@app.route('/userVote/<int:age>')
def userVote(age):
    res=""
    if age>=18:
        res= "Eligible to vote."
    else:
        res= "Not eligible to vote."
    return render_template('vote.html',result=res)
# Here, the URL rule is /userVote/<age>, where <age> is a variable part of the URL.
# The function userVote() accepts the age as an argument and checks if the age is greater than or equal to 18.
# If the age is greater than or equal to 18, it returns the message You are eligible to vote.
# If the age is less than 18, it returns the message You are not eligible to vote.
# The float converter is used to convert the variable part of the URL to a float.
# render_template() is used to render the vote.html file and pass the age as a parameter to the template.   

'''
3 ways to read the data from the backend to the html page:
1. Using the expression {{ }}: It is used to display the data (print the output) on the HTML page.
2. Using the statement {% %}: It is used to execute the statements on the HTML page. (conditon, loop, etc.) 
3. Using the filter {{ | }}: It is used to format the data before displaying it on the HTML page.
4. Using the comments {# #}: It is used to write the comments in the HTML page.

'''

@app.route('/VoteElgb/<int:age>')
def userVoteElgb(age):
    res=""
    if age>=18:
        res= "Eligible to vote."
    else:
        res= "Not eligible to vote."
    exp = {"age":age,"result":res}
    return render_template('vote1.html',results =exp)

@app.route('/uservote/<int:age>')
def uservote(age):
    return render_template('vote.html',result=age)

@app.route('/check_vote/<int:age>')
def check_vote(age):
    if age >= 18:
        return redirect(url_for('userVoteElgb', age=age))
    else:
        return redirect(url_for('userVoteElgb', age=age))

# Here, the URL rule is /check_vote/<age>, where <age> is a variable part of the URL.
# The function check_vote() accepts the age as an argument and checks if the age is greater than or equal to 18.
# If the age is greater than or equal to 18, it redirects to the userVoteElgb() function with the age as a parameter.
# If the age is less than 18, it redirects to the userVoteElgb() function with the age as a parameter.
# redirect() is used to redirect to the userVoteElgb() function based on the condition.
# url_for() is used to generate the URL for the userVoteElgb() function based on the condition.


# Simple bhasha mein samjho:
# redirect() function koi bhi specific URL pe redirect karne ke liye use hota hai (jo already created hai), aur url_for() function kisi specific function ke liye URL generate karne ke liye use hota hai.
# Is case mein, agar age 18 se zyada ya barabar hai, toh userVoteElgb() function mein age ke saath redirect karta hai.
# Agar age 18 se kam hai, toh userVoteElgb() function mein age ke saath redirect karta hai. 
# redirect() function ko use karke kisi specific URL pe redirect karne ke liye use kiya jata hai, aur url_for() function ko use karke kisi specific function ke liye URL generate karne ke liye use kiya jata hai.
# This is known as building URLs dynamically.


if __name__=="__main__":
    app.run(debug=True)