import webapp2
import cgi
import re

info_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
</head>
<body>
<form action = "input" method = "post">
    <label>
        Username:
        <input type = "text" name = "uname"/>
        %(error_uname)s
    </label>
    <p>
    <label>
        Password:
        <input type = "password" name = "pwd"/>
        %(error_pwd)s
    </label>
    </p>
    <p>
    <label>
        Verify Password:
        <input type = "password" name = "vpwd"/>
        %(error_pwd_mismatch)s
    </label>
    </p>
    <p>
    <label>
        Email:
        <input type = "text" name = "email"/>
        %(error_email)s
    </label>
    </p>
    <input type = "submit"/>
</form>
</body>
</html>
"""
uname_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_uname(uname):
    return uname and uname_re.match(uname)

pwd_re = re.compile(r"^.{3,20}$")
def valid_pwd(pwd):
    return pwd and pwd_re.match(pwd)

email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return email and email_re.match(email)

class Index(webapp2.RequestHandler):

    def get(self):
        self.response.write(info_form)

    def post(self,error = ""):
        uname = str(self.request.get("uname"))
        pwd = str(self.request.get("pwd"))
        vpwd = str(self.request.get("vpwd"))
        email = str(self.request.get("email"))

        errors = {"error_uname": "Invalid username",
                  "error_pwd": "Invalid password",
                  "error_pwd_mismatch": "Passwords do no match",
                  "error_email": "Invalid email"}

        check_uname = valid_uname(uname)
        if not valid_uname(uname):
            info_form % errors["error_uname"]

        check_pwd = valid_pwd(pwd)
        elif not valid_pwd(pwd):
            info_form % errors["error_pwd"]
        elif pwd != vpwd:
            info_form % errors["error_pwd_mismatch"]

        check_email = valid_email(email)
        elif not valid_email(email):
            info_form % errors["error_email"]

        self.response.write(info_form)

        if valid_uname(uname) and valid_pwd(pwd) and valid_email(email):
            welcome = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Welcome %(uname)s/title>
            </head>
            <body>
            <h1>Welcome %(uname)s</h1>
            </body>
            </html>
            """


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
