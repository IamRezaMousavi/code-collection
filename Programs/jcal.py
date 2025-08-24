# @Author: @IamRezaMousavi
# @Date:   2022-08-09 05:36:05
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-08-09 06:01:37

from jcalendar import calendar
from jdatetime import date


def main():
    c = calendar.TextCalendar()
    now = date.today()

    print(c.formatmonth(now.year, now.month))
    print('Today is', now)


if __name__ == '__main__':
    main()
