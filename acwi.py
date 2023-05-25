# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:09:25 2023

@author: lmaurelli
"""

import pandas as pd

file = 'historyIndex.xls'

df = pd.read_excel(file, header=6, index_col=0, skipfooter=19, parse_dates=True,
                   names=['Price'])

days = df.loc['1997-01-01':, :]
days = days * 100 / days.iat[0, 0]

weeks = days.resample('w').ffill()
idx_yw = weeks.index.isocalendar()[['year', 'week']]
idx_yw = pd.MultiIndex.from_frame(idx_yw)
weeks = weeks.set_index(idx_yw)
weeks['Change'] = weeks.pct_change()

rweeks = weeks.rolling(4)

months = days.resample('m').ffill()
years = days.resample('y').ffill()

rmonths = weeks.rolling(52).mean()

irs = pd.read_csv('IRS10.csv', usecols=[0, 1], skiprows=5, index_col=0,
                  date_format='%Y%b', header=0, names=['index', 'IRS10'])
irs.describe()
