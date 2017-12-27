import webapp2

gurjot="""
<html>
<h1>Form</h1>
<form method="post" action="/gurjot">
    <input name="q">
    <input type="submit" name="submit">
</form>
<html>
"""

fool="""
<h1 style="color:blue;">Gurjot Singh Joshi</h1>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(gurjot)

class test(webapp2.RequestHandler):
    def post(self):
                #self.response.write(fool)
                self.response.headers['Content-Type']='text/plain'
                self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/', MainPage),('/gurjot',test)], debug=True)
