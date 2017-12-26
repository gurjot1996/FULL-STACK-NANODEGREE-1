months = ['January','February','March','April','May','June',
         'July','August','September','October','November','December']
        
def valid_month(month):
    cmonth=month.capitalize()
    month_abbvs = {}; 
    if cmonth in months:
        print cmonth
    else:    
        for m in months:
           month_abbvs[m[:3].lower()]=m
        if month in month_abbvs:
            print(month_abbvs[month])
        else:
            print('wrong')


valid_month('def');
