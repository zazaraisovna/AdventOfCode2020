#!/usr/bin/env python
# coding: utf-8

# In[77]:


# FBFBBFFRLR: row 44, column 5, seat ID 357
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
bpass = input().split()


# In[87]:


# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63. - 0
# B means to take the upper half, keeping rows 32 through 63. - 1
# F means to take the lower half, keeping rows 32 through 47. - 2
# B means to take the upper half, keeping rows 40 through 47. - 3
# B keeps rows 44 through 47. - 4
# F keeps rows 44 through 45. - 5
# The final F keeps the lower of the two, row 44. - 6

# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.

# seat ID: multiply the row by 8, then add the column.

seat_ids = []

for k in range(len(bpass)):
    frm = 0
    to = 127
    row = 0
    for i in range(6):
        if bpass[k][i] == 'F':
            frm = frm
            to = int((to + 1 - frm)/2 + frm - 1)
        elif bpass[k][i] == 'B':
            frm = int((to + 1 - frm)/2) + frm
            to = to
    if bpass[k][6] == 'F':
        row =frm
    elif bpass[k][6] == 'B':
        row = to

    # print('row: ',row)

    a = 0
    b = 7
    column = 0
    for j in range(7,10):
        if bpass[k][j] == 'L':
            b = int((b + 1 - a)/2 + a - 1)
        elif bpass[k][j] == 'R':
            a = int((b + 1 - a)/2 + a)
    if bpass[k][9] == 'R':
        column = b
    elif bpass[k][9] == 'L':
        column = a
    # print('column: ', column)

    # print('seat ID: ', row * 8 + column)
    seat_ids.append(row * 8 + column)
print(seat_ids)
print(max(seat_ids))


# In[93]:


# Part 2

for l in range(1, len(seat_ids) - 1):
    if (l not in seat_ids) and (l - 1 in seat_ids) and (l + 1 in seat_ids):
        print(l)

