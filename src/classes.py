import sys
import calendar
args = sys.argv[1:]

# User provides a month and year
try:
    if len(args) == 2:
        month = int(args[0])
        year = int(args[1])
    # User provides only a month
    elif len(args) == 1:
        month = int(args[0])
        year = datetime.now().year
    # User provides no args
    elif len(args) == 0:
        now = datetime.now()
        month = now.month
        year = now.year
    # User provides incorrect arguments
    else:
        print("Incorrect arguments")
        exit()
except:
    print("ERROR: Must be in the format '14_cal.py month [year]'")

tc = calendar.TextCalendar()
tc.prmonth(year, month)
