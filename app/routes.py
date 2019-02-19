from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Mij"}

    posts = [
        {
            "author": {"username": "Jo"},
            "body": "Good day today"
        },
        {
            "author": {"username": "Mitch"},
            "body": "United are the shit"
        },
        {
            "author": {"username": "Jock"},
            "body": "Cats have 7 not 9 lives. And I can prove it"
        }
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember me={}".format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)