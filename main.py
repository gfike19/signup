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
        <input type = "text" name = "uname" value = "%(error_uname)s"/>
    </label>
    <p>
    <label>
        Password:
        <input type = "password" name = "pwd" value = "%(error_pwd)s"/>
    </label>
    </p>
    <p>
    <label>
        Verify Password:
        <input type = "password" name = "vpwd" value = "%(error_pwd_mismatch)s"/>
    </label>
    </p>
    <p>
    <label>
        Email:
        <input type = "text" name = "email" value = "%(error_email)s"/>
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

    def write_form(self,info_form, uname = "", pwd = "", vpwd = "", email = ""):
        self.response.write(info_form % {"error_uname": "Invalid username",
                  "error_pwd": "Invalid password",
                  "error_pwd_mismatch": "Passwords do no match",
                  "error_email": "Invalid email"})

    def get(self):
        self.write_form(info_form)

    def post(self):
        uname = str(self.request.get("uname"))
        pwd = str(self.request.get("pwd"))
        vpwd = str(self.request.get("vpwd"))
        email = str(self.request.get("email"))

        check_uname = valid_uname(uname)
        if not valid_uname(uname):
            info_form % ["error_uname"] = "Invalid username"

        check_pwd = valid_pwd(pwd)
        if not valid_pwd(pwd):
            info_form % ["error_pwd"] = "Invalid password"
        if pwd != vpwd:
            info_form % ["error_pwd_mismatch"] = "Passwords do not match"

        check_email = valid_email(email)
        if not valid_email(email):
            info_form % ["error_email"] = "Invalid email"

        else:
            self.write_form(uname, pwd, vpwd, email)

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

            self.response.write(welcome % uname)


app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
