from flask import Flask, request, redirect, render_template, flash, session

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'


def is_email(string):
    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present

def is_valid_password(string):
    if len(string) > 20 or len(string) < 3:
        return False
    bad_chars = "!@#$ %^&*()+|}{:~-=[]"    
    for char in bad_chars:
        if char in string:
            return False  
    else:
        return True          

def is_valid_username(string):
    if len(string) > 20 or len(string) < 3:
        return False
    else:
        return True    


@app.route("/welcome", methods=["GET"])
def welcome():
    user = session["username"]
    return render_template("welcome.html", user=user)

@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        verify = request.form["verify"]
        username = request.form["username"]

        if not email and not password and not verify and not username:
            flash("You must enter a username and password.", "error")    
        if email and not is_email(email):
            flash("You must enter a valid email.", "email_error")   
        if password != verify:
            flash("Passwords do not match.", "password_error")    
        if not is_valid_password(password):
            flash("You must enter a valid password. Must be 3-20 characters long and cannot contain spaces.", "password_error")
        if email and not is_valid_username(username):
            flash("You must enter a valid username. Must be 3-20 characters long.", "username_error")
        if not email and not is_valid_username(username):
            flash("You must enter a valid username. Must be 3-20 characters long.", "username_error")
        else:
            user = session["username"]
            return redirect("welcome.html", user=user)

    return render_template("signup.html")


app.run()