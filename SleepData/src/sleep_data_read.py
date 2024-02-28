# -*- coding: utf-8 -*-
# @Author: S.Reza Mousavi
# @Date:   2021-12-23 18:33:16
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2022-02-11 01:21:48

import pandas as pd
from datetime import timedelta

df = pd.read_csv("All Sleep Data.csv")
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
