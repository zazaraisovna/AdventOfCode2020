#!/usr/bin/env python
# coding: utf-8

## Advent of code
##Day 1
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])

for i in range(len(A)):
    for j in range(len(A)):
        if i != j and A[i] + A[j] == 2020:
            m = A[i] * A[j]
print(m)

for i in range(len(A)):
    for j in range(len(A)):
        for k in range(len(A)):
            if i != j and j != k and A[i] + A[j] + A[k] == 2020:
                m3 = A[i] * A[j] * A[k]
print(m3)