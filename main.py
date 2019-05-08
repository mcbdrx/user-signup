from flask import Flask, request, redirect, render_template, flash
app = Flask(__name__)
app.config["DEBUG"] = True

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
    
# TODO fix error message
@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        verify = request.form["verify"]

        if not is_email(email) or not email:
            flash("You must enter a valid email.")
            return redirect("/")
        if password != verify:
            flash("Password verify did not match password.")
            return redirect("/")
        if not password or not verify:
            flash("You must enter a password.")
            return redirect("/")
        if not is_valid_password(password):
            flash("Your password must be 3-20 characters in length and must not contain any of these characters: '!@#$%^&*()+|}{:~-=[]'")
            return redirect("/")
        else:
            return render_template("signup.html")

    return render_template("signup.html")


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

app.run()