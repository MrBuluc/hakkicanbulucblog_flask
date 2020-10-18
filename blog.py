from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.handlers.sha2_crypt import sha256_crypt

# User Register Form


class RegisterForm(Form):
    name = StringField(label="İsim Soyisim", validators=[
                       validators.Length(min=4, max=25)])
    username = StringField(label="Kullanıcı Adı", validators=[
                           validators.Length(min=5, max=35)])
    email = StringField(label="Email Adresi", validators=[validators.Email(
        message="Lütfen Geçerli Bir Email Adresi Girin...")])
    password = PasswordField(label="Parola", validators=[
        validators.DataRequired(message="Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname="confirm",
                           message="Parolanız Uyuşmuyor...")
    ])
    confirm = PasswordField(label="Parola Doğrula")


app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "hakkicanbulucblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"


mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/article/<string:id>")
def detail(id):
    return "Article ID: " + id


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        
        return redirect(location=url_for("index"))
    else:

        return render_template("register.html", form=form)


if(__name__ == "__main__"):
    app.run(debug=True)
