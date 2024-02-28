# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2021-09-25 06:29:13
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2022-02-11 01:21:56

print("\tYA ALLAH")
filename = "All Sleep Data"

from datetime import datetime, timedelta
import pandas as pd


def getDaysHoursMinutes(timedelta):
    return timedelta.days, timedelta.seconds//3600, (timedelta.seconds//60)%60

def creatDate(startTime, endTime, startDate="", endDate=""):
    
    if startDate == "":
        one_day = datetime(2021, 9, 23) - datetime(2021, 9, 22)
        yesterday = datetime.today() - one_day
        startDate = yesterday.strftime("%Y-%m-%d")
        
        endDate = datetime.today().strftime("%Y-%m-%d")
    
        startDateTime = datetime.strptime(startDate + " " + startTime, "%Y-%m-%d %H:%M")
        endDateTime = datetime.strptime(endDate + " " + endTime, "%Y-%m-%d %H:%M")

        delta = endDateTime - startDateTime

        if not getDaysHoursMinutes(delta)[0] == 0:
            startDateTime = datetime.strptime(endDate + " " + startTime, "%Y-%m-%d %H:%M")
    else:
        startDateTime = datetime.strptime(startDate + " " + startTime, "%Y-%m-%d %H:%M")
    endDateTime = datetime.strptime(endDate + " " + endTime, "%Y-%m-%d %H:%M")
    delta = endDateTime - startDateTime

    print("\t ---> ", startDateTime, "\n\t ---> ", endDateTime)
    print("\tTime:", str(delta), "\n")
    return startDateTime, endDateTime, delta

start_sleep = input("Please enter START time:")
end_sleep = input("Please enter END time:")
startDate, endDate, delta = creatDate(start_sleep, end_sleep)

while True:    
    answer = input("\tIs it currect??").lower()
    if answer == "y" or answer == "exit":
        break
    elif answer == "n":
        start_date = input("please enter START data (YYYY-MM-DD):")
        end_date = input("please enter END data (YYYY-MM-DD):")
        startDate, endDate, delta = creatDate(start_sleep, end_sleep, start_date, end_date)


if answer == "y":
    # Create Data
    data = {
        "startDate": startDate.strftime("%Y-%m-%d"),
        "startTime": startDate.strftime("%H:%M"),
        "endDate": endDate.strftime("%Y-%m-%d"),
        "endTime": endDate.strftime("%H:%M"),
        "sleepTime": str(delta),
        "sleepSeconds": delta.seconds
    }

    # Load, Update, Save Data
    newData = pd.DataFrame(data, index=[0])
    df = pd.read_csv(filename + ".csv")
    df = df.append(newData).reset_index(drop=True)

    print("\n\n\tCompleted Successfully!\n")
    
    print(df)
    sum_df = df.groupby(["endDate"]).sum()
    convert_seconds = []
    for index in sum_df.index:
        convert_seconds.append(str(timedelta(seconds=int(sum_df["sleepSeconds"][index]))))
    
    sum_df["sleepTime"] = convert_seconds
    print("\n", sum_df)
    
    seconds_mean = sum_df["sleepSeconds"].mean()
    sleep_mean = str(timedelta(seconds=int(seconds_mean)))
    print(f"\n\tMean: {seconds_mean} s --> {sleep_mean}")
	
print("\tGood Luck!")
