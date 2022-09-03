import pytz
import datetime

for tz in pytz.all_timezones:
    x = datetime.datetime.now(pytz.timezone(tz))
    
    print(f"{tz} time : {x} ")

