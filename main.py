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
    </label>
    <p>
    <label>
        Password:
        <input type = "password" name = "pwd"/>
    </label>
    </p>
    <p>
    <label>
        Verify Password:
        <input type = "password" name = "vpwd"/>
    </label>
    </p>
    <p>
    <label>
        Email:
        <input type = "text" name = "email"/>
    </label>
    </p>
    <input type = "submit"/>
</form>
</body>
</html>
"""
error = ""
#<div>%(error)s</div>

class Index(webapp2.RequestHandler):



    # def write_form(self):
    #     self.response.out.write(info_form)

        #%{"error": error})

    def get(self):
        self.response.write(info_form)

    def post(self):
        uname = str(self.request.get("uname"))
        pwd = str(self.request.get("pwd"))
        vpwd = str(self.request.get("vpwd"))
        email = str(self.request.get("email"))

        inputs = dict(uname = username,
                     pwd = pwd,
                     vpwd = vpwd,
                      email = email)

        uname_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        def valid_uname(uname):
            return uname_re.match(uname)

        pwd_re = re.compile(r"^.{3,20}$")
        def valid_pwd(pwd):
            return pwd_re.match(pwd)

        email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        def valid_email(email):
            return email_re.match(email)

        check_uname = valid_uname(uname)
        if not valid_uname(uname):
            inputs["error_uname"] = "Invalid username"
            # self.write_form("<br>Invalid username<br>")

        check_pwd = valid_pwd(pwd)
        if not valid_pwd(pwd):
            inputs["error_pwd"]= "Invalid password<br>"
            # self.write_form("<br>Invalid password<br>")
        elif pwd != vpwd:
            intputs["error_pwd_mismatch"]="Passwords do not match"
            # self.write_form("<br>Passwords do not match<br>")

        check_email = valid_email(email)
        if valid_email(email):
            inputs["error_email"] = "Invalid email address"
            # self.write_form("<br>Invalid email address<br>")

    # self.write_form()
        # self.response.write(info_form + error)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
