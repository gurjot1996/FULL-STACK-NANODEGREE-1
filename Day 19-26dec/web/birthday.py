import webapp2

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
        <input type="text" name="day">
    </label>
    </div>

    <div class="month">
    <label>
        Month:
        <input type="text" name="month">
    </label>
    </div>
    
    <div class="year">
    <label>
        Year:
        <input type="number" name="year" min="-9999" max="9999" >
    </label>
    </div>   
    <input type="submit" name="submit">
</form>

"""

class mainpage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(gurjot)
    def post(self):
        user_day=valid_day(self.request.get('day'))
        user_month=valid_month(self.request.get('month'))
        user_year=valid_year(self.request.get('year'))
        if not(user_month and user_year and user_day):
            self.response.out.write(gurjot)
        else:
            self.response.out.write('<b>that is a  valid date</b>')



app=webapp2.WSGIApplication([('/',mainpage)],debug=True)
