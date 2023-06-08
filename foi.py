# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:09:25 2023

@author: lmaurelli
"""

import pandas as pd

# file1995 = 'C:/Users/lmaurelli/OneDrive - CAMOZZI GROUP SPA/Desktop/foi1995.csv'
# df1995 = pd.read_csv(file1995, usecols=[1, 5, 7, 8, 10], index_col=3,
#                  date_format='%Y-%m')
# mask_territorio1995 = df1995['Territorio'] == 'Italia'
# mask_misura1995= df1995['Misura'] == 'numeri indici'
# mask_FOI1995 = df1995['COICOP'] == 'indice generale'
# mask_FOIxT1995 = df1995['COICOP'] == 'indice generale (senza tabacchi)'
# FOI1995 = df1995.loc[mask_territorio1995 & mask_misura1995 & mask_FOI1995, 'Value'].rename('FOI').to_frame()
# FOIxT1995 = df1995.loc[mask_territorio1995 & mask_misura1995 & mask_FOIxT1995, 'Value'].rename('FOIxT').to_frame()

# rebase_FOI_2010_12 = FOI1995.at['2010-12', 'FOI'][0]
# rebase_FOIxT_2010_12 = FOIxT1995.at['2010-12', 'FOIxT'][0]

# file2011 = 'C:/Users/lmaurelli/OneDrive - CAMOZZI GROUP SPA/Desktop/foi2011.csv'
# df2011 = pd.read_csv(file2011, usecols=[1, 5, 7, 8, 10], index_col=3,
#                  date_format='%Y-%m')
# mask_territorio2011 = df2011['Territorio'] == 'Italia'
# mask_misura2011 = df2011['Misura'] == 'numeri indici'
# mask_FOI2011 = df2011['COICOP Rev. Istat'] == 'indice generale'
# mask_FOIxT2011 = df2011['COICOP Rev. Istat'] == 'indice generale senza tabacchi'
# FOI2011 = df2011.loc[mask_territorio2011 & mask_misura2011 & mask_FOI2011, 'Value'].rename('FOI').to_frame()
# FOI2011 = (FOI2011 * rebase_FOI_2010_12 / 100).round(1)
# FOIxT2011 = df2011.loc[mask_territorio2011 & mask_misura2011 & mask_FOIxT2011, 'Value'].rename('FOIxT').to_frame()
# FOIxT2011 = (FOIxT2011 * rebase_FOIxT_2010_12 / 100).round(1)

# rebase_FOI_2015_12 = FOI2011.at['2015-12', 'FOI'][0]
# rebase_FOIxT_2015_12 = FOIxT2011.at['2015-12', 'FOIxT'][0]

# file2015 = 'C:/Users/lmaurelli/OneDrive - CAMOZZI GROUP SPA/Desktop/foi2015.csv'
# df2015 = pd.read_csv(file2015, usecols=[1, 5, 7, 8, 10], index_col=3,
#                  date_format='%Y-%m')
# mask_territorio2015 = df2015['Territorio'] == 'Italia'
# mask_misura2015 = df2015['Misura'] == 'numeri indici'
# mask_FOI2015 = df2015['COICOP Rev. Istat'] == 'indice generale'
# mask_FOIxT2015 = df2015['COICOP Rev. Istat'] == 'indice generale senza tabacchi'
# FOI2015 = df2015.loc[mask_territorio2015 & mask_misura2015 & mask_FOI2015, 'Value'].rename('FOI').to_frame()
# FOI2015 = (FOI2015 * rebase_FOI_2015_12 / 100).round(1)
# FOIxT2015 = df2015.loc[mask_territorio2015 & mask_misura2015 & mask_FOIxT2015, 'Value'].rename('FOIxT').to_frame()
# FOIxT2015 = (FOIxT2015 * rebase_FOIxT_2015_12 / 100).round(1)

# FOI = pd.concat([FOI1995, FOI2011, FOI2015])
# FOIxT = pd.concat([FOIxT1995, FOIxT2011, FOIxT2015])

# df = pd.concat([FOI, FOIxT], axis=1)
# df.index.name = 'index'
# df.to_csv('FOI_FOIxT_1995_2023.csv')

file = 'FOI_FOIxT_1995_2023.csv'
df = pd.read_csv(file, index_col=0, parse_dates=True)

# CARG
first = df.loc[df.index[0], 'FOI']
last = df.loc[df.index[-1], 'FOI']
CAGR_FOI = (last/first) ** (12 / len(df.index)) - 1 

# TFR
df_dec = df.iloc[11::12]
df_dec_diff = df_dec.diff()
df_dec_diff.iloc[0, :] = df_dec.iloc[0, :] - [100, 100]
df_dec_diff[0] 

x = df.groupby([df.index.year, df.index.month]).first()
x.index.names = ['Year', 'Month']
