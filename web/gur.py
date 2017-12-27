import webapp2

gurjot="""
<html>
<h1>Form</h1>
<form >
    <input type="radio"  name="q" value="gurjot">Gurjot
    <input type="radio"   name="q" value="ron">Ron
    <input type="radio" name="q" value="joshi">Joshi
    <input type="submit" name="submit">
</form>
<html>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(gurjot)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
