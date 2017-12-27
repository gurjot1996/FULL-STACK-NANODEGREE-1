import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s,quote=True)
    
def valid_day(day):
    if day and day.isdigit():
        day = int(day)
    if day > 0 and day <=31:
        return day


months = ['January','February','March','April','May','June',
         'July','August','September','October','November','December']
def valid_month(month):
    cmonth=month.capitalize()
    month_abbvs = {}; 
    if cmonth in months:
        return cmonth
    else:    
        for m in months:
           month_abbvs[m[:3].lower()]=m
        if month in month_abbvs:
            return month_abbvs[month]


def valid_year(year):
    if year and year.isdigit():
        year=int(year)
    if year>0 and year<=2050:
        return year

thanks="""
<h1>Thanks for submitting the form your birthday has been successfully inputted</h1>
<img src="https://www.bettys.co.uk/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/o/soft-iced-happy-birthday-cake-2000117_4.jpg" width="500px" height="500px">
"""

gurjot="""
<html>
<head>
<title>happy birthday</title>
    <style>
        .form{
        display:grid;
        grid-template-columns:repeat(6,1fr);
        grid-auto-rows:100px;
        }
        .day{
        grid-column:1/3;
        }
        .month{
        grid-column:3/5;
        }
        .year{
        grid-column:5/7;
        }
        .error{
        color:red;
        }
        label,input{
            margin:0px 2px 1px 10px;
            }
    </style>
</head>
<h1 style="font-weight:bold;font-Size:80;color:red">Is It your Birthday Today?</h1>
<form class="form" method="post">
    <div class="day">
    <label>
        Day:
        <input type="text" name="day" value="%(dayinput)s">
    </label>
    </div>
    <div class="month">
    <label>
        Month:
        <input type="text" name="month" value="%(monthinput)s">
    </label>
    </div>
    <div class="year">
    <label>
        Year:
        <input type="number" name="year" min="-9999" max="9999" value="%(yearinput)s">
    </label>
    </div>   
    <div class="error">%(error)s</div>
    <input type="submit" name="submit">
</form>
"""
class thankshandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(thanks)

class mainpage(webapp2.RequestHandler):
    def write_form(self,error="",day="",month="",year=""):
        self.response.out.write(gurjot % {"error":error,"dayinput":escape_html(day),"monthinput":escape_html(month),"yearinput":escape_html(year)})
   
    def get(self):
        self.write_form();
   
    def post(self):
        user_day=valid_day(self.request.get('day'))
        user_month=valid_month(self.request.get('month'))
        user_year=valid_year(self.request.get('year'))
                 
        if not(user_month and user_year and user_day):
            self.write_form("error occured",self.request.get('day'),self.request.get('month'),self.request.get('year'))
        else:
            self.redirect('/thanks')

app=webapp2.WSGIApplication([('/',mainpage),('/thanks',thankshandler)],debug=True)
