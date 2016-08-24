import webapp2

class Index(webapp2.RequestHandler):
    def get(self):
        info_form = """
        <form action = "input" method = post>

            <label>
                Username:
                <input = "text" name = "uname"/>
            </label>

            <label>
                Password:
                <input = "text" name = "pwd"/>
            </label>

            <label>
                
            </label>

        </form>
        """

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
