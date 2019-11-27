# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:43:38 2019

@author: 张和持
"""

from openpyxl import load_workbook
from numpy import *
import numpy as np

file_1 = load_workbook('exec5.5.xlsx')

sheets_1 = file_1.get_sheet_names()

booksheet_1 = file_1.get_sheet_by_name(sheets_1[0])

rows_1 = booksheet_1.rows

x_0 = mat([0.6, 3.0])

pi_1 = []
pi_2 = []

for row_1 in rows_1:
    line = [col_1.value for col_1 in row_1]
    if line[0] == 'x1':
        continue
    if line[2] == 1:
        pi_1.append(mat(line[0:2]))
    elif line[2] == 2:
        pi_2.append(mat(line[0:2]))

S_1 = 0
S_2 = 0

xb_1 = mat([0, 0])
xb_2 = mat([0, 0])

for x in pi_1:
    xb_1 = xb_1 + x

for x in pi_2:
    xb_2 = xb_2 + x

xb_1 /= len(pi_1)
xb_2 /= len(pi_2)

S_1 = np.zeros((2,2))
S_2 = np.zeros((2,2))

for i in range(0, len(pi_1)):
    S_1 = S_1 + np.transpose(pi_1[i] - xb_1) * (pi_1[i] - xb_1)
for i in range(0, len(pi_2)):
    S_2 = S_2 + np.transpose(pi_2[i] - xb_2) * (pi_2[i] - xb_2)

S_1 /= (len(pi_1) - 1)
S_2 /= (len(pi_2) - 1)


S_p = ((len(pi_1) - 1) * S_1 + (len(pi_2) - 1) * S_2) / (len(pi_1) + len(pi_2) - 2)
S_pm = np.linalg.inv(S_p)

I_1 = S_pm * np.transpose(xb_1)
I_2 = S_pm * np.transpose(xb_2)

c_1 = -1/2 * xb_1 * S_pm * np.transpose(xb_1)
c_2 = -1/2 * xb_2 * S_pm * np.transpose(xb_2)


if np.transpose(I_1) * np.transpose(x_0) + c_1 >= np.transpose(I_2) * np.transpose(x_0) + c_2:
    print('下雨')
else:
    print('不下雨')