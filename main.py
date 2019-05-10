from flask import Flask, request, redirect, render_template, flash, session

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'


def is_email(string):
    if string:
        bad_chars = "!#$ %^&*()+|}{:~-=[]"    
        for char in bad_chars:
            if char in string:
                return False  
    
        atsign_index = string.find('@')
        atsign_present = atsign_index >= 0
        if not atsign_present:
            return False
        else:
            domain_dot_index = string.find('.', atsign_index)
            domain_dot_present = domain_dot_index >= 0
            return domain_dot_present
    else:
        return False

def is_valid_password(string):
    if len(string) > 20 or len(string) < 3:
        return False
    bad_chars = "!@#$ %^&*()+|}{:~-=[]"    
    for char in bad_chars:
        if char in string:
            return False  
    return True          

def is_valid_username(string):
    if len(string) > 20 or len(string) < 3:
        return False
    else:
        return True    


@app.route("/welcome", methods=["GET"])
def welcome():
    username = session["username"]
    return render_template("welcome.html", username=username)
    if "username" not in session:
        return redirect("/")    

@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        verify = request.form["verify"]
        username = request.form["username"]
        error_counter = 0

        if email and not is_email(email):
            flash("You must enter a valid email.", "email_error") 
            error_counter += 1  
        if password != verify:
            flash("Passwords do not match.", "password_error")
            error_counter += 1    
        if not is_valid_password(password):
            flash("You must enter a valid password. Must be 3-20 characters long and cannot contain spaces.", "password_error")
            error_counter += 1  
        if email and not is_valid_username(username):
            flash("You must enter a valid username. Must be 3-20 characters long.", "username_error")
            error_counter += 1  
        # if not email and not is_valid_username(username):
        #     flash("You must enter a valid username. Must be 3-20 characters long.", "username_error")
        #     error_counter += 1  
        if error_counter != 0:
            return render_template("signup.html", error_counter=error_counter)

        else:
            session["username"] = username
            return redirect("/welcome")
        
    else: 
        return render_template("signup.html")


app.run()