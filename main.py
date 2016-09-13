import webapp2
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
        <strong>Username:</strong>
        <input type = "text" name = "uname" value = "%(uname)s" required/>
        <div style = "color: red; display: inline;">%(error_uname)s</div>
    </label>
    <p>
    <label>
        <strong>Password: </strong>
        <input type = "password" name = "pwd" required/>
        <div style = "color: red; display: inline;">%(error_pwd)s</div>
    </label>
    </p>
    <p>
    <label>
        <strong>Verify Password: </strong>
        <input type = "password" name = "vpwd" required/>
        <div style = "color: red; display: inline;">%(error_vpwd)s</div>
    </label>
    </p>
    <p>
    <label>
        <strong>Email:</strong> (Optional)
        <input type = "text" name = "email"/>
        <div style = "color: red; display: inline;">%(error_email)s</div>
    </label>
    </p>
    <input type = "submit"/>
</form>
</body>
</html>
"""

welcome = """
<!DOCTYPE html>
<html>
<head>
<title>Welcome %(uname)s!</title>
</head>
<body>
<h3>Welcome %(uname)s!</h3>
</body>
</html>
"""
uname_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_uname(uname):
    return uname_re.match(uname)

pwd_re = re.compile(r"^.{3,20}$")
def valid_pwd(pwd):
    return pwd_re.match(pwd)

email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return email_re.match(email)

class Index(webapp2.RequestHandler):

    def write_form(self, error_uname = "", error_pwd = "", error_vpwd = "", error_email = "", uname = "", pwd = "", vpwd = "", email = ""):
        self.response.write(info_form % {"error_uname" : error_uname,
        "error_pwd" : error_pwd,
        "error_vpwd" : error_vpwd,
        "error_email" : error_email,
        "uname":uname,
        "pwd":pwd,
        "vpwd":vpwd,
        "email":email})

    def get(self):
        self.write_form()

class ValidateForm(webapp2.RequestHandler):

    def write_form(self, error_uname = "", error_pwd = "", error_vpwd = "", error_email = "",  uname = "", pwd = "", vpwd = "", email = ""):
        self.response.write(info_form %{"error_uname" : error_uname,
        "error_pwd":error_pwd,
        "error_vpwd":error_vpwd,
        "error_email":error_email,
        "uname":uname,
        "pwd":pwd,
        "vpwd":vpwd,
        "email":email})

    def post(self):
        uname = self.request.get("uname")
        pwd = self.request.get("pwd")
        vpwd = self.request.get("vpwd")
        email = self.request.get("email")

        error_uname = ""
        error_pwd = ""
        error_vpwd = ""
        error_email = ""
        error_count = 0

        if not valid_uname(uname):
            error_uname = "Invalid username"
            error_count += 1


        elif not valid_pwd(pwd):
            error_pwd = "Invalid password"
            error_count += 1

        elif vpwd != pwd:
            error_vpwd = "Passwords do not match"
            error_count += 1

        elif email:
            error_email = ""
            if not valid_email(email):
                error_email = "Invalid email"
                error_count += 1

        if error_count > 0:
            self.write_form(error_uname, error_pwd, error_vpwd, error_email)

        if valid_uname(uname) and valid_pwd(pwd) and vpwd == pwd:
            str_uname = str(uname)
            self.response.out.write(welcome % {"uname":uname})


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/input', ValidateForm)
], debug=True)
