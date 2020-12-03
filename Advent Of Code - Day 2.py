#!/usr/bin/env python
# coding: utf-8

passwords = input().split()
a = []
for i in range(0, len(passwords)-2, 3):
    new_elem = passwords[i], passwords[i + 1], passwords[i + 2]
    a.append(new_elem)

## first
    ## берём каждый элемент (подсписок) списка b
    ## берём первый элемент (подсписка) и достаём их элементы frm и to
    ## считаем сколько раз встреачется второй элемент подсписка и сравниваем с frm и to
    
valid_cnt = 0
for k in range(0, len(a)):
    first = (a[k])[0].split('-')
    second = ((a[k])[1])[0]
    third = (a[k])[2]
    frm = int(first[0])
    to = int(first[1])
    cnt = third.count(second)
    if third.find(second) >= 0 and cnt >= frm and cnt <= to:
        valid_cnt  +=1
print(valid_cnt)

## second

b = []
for j in range(0, len(passwords)-2, 3):
    new_elem = passwords[j], passwords[j + 1], passwords[j + 2]
    b.append(new_elem)
    
valid2_cnt = 0
for l in range(0, len(a)):
    first = (b[l])[0].split('-')
    second = ((b[l])[1])[0]
    third = (b[l])[2]
    frm = int(first[0]) - 1 
    to = int(first[1]) - 1
    if (third[frm] == second and third[to] != second) or (third[frm] != second and third[to] == second):
        valid2_cnt  += 1
print(valid2_cnt)