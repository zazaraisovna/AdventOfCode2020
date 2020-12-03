#!/usr/bin/env python
# coding: utf-8
map = input().split()

## Part 1 (without function)

## columns on the map
col = 0
## count of trees on the way
cnt = 0
## Right 3, down 1.
for i in range(1, len(map)):
    if col + 3 < len(map[0]):
        col += 3
    else:
        col = col + 3 - len(map[0])
    if map[i][col] == '.': ## free way
        continue
    if map[i][col] == '#': ## tree on the way
        cnt += 1
print('Right 3, down 1: ' + str(cnt))


## Part Two

def treecount(r, d):
    ## columns on the map
    col = 0
    ## row on the map
    row = 0
    ## count of trees on the way
    cnt = 0
    for i in range(1, len(map), d):
        if col + r < len(map[0]):
            col += r
        else:
            col = col + r - len(map[0])
        if row + d < len(map):
            row += d
        if map[row][col] == '.': ## free way
            continue
        if map[row][col] == '#': ## tree on the way
            cnt += 1
    return cnt
print(treecount(1, 1) * treecount(3, 1) * treecount(5, 1) * treecount(7, 1) * treecount(1, 2))