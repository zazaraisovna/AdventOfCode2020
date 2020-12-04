#!/usr/bin/env python
# coding: utf-8

# In[39]:


## I am changing my input data before start
## changed \n\r --> * to separate passports
passports = input().split('*')


# In[40]:


## Part 1

count = 0
for i in range(0, len(passports)):
    if passports[i].count('byr') == 1 and passports[i].count('iyr') == 1 and passports[i].count('eyr') == 1:
        if passports[i].count('hgt') == 1 and passports[i].count('hcl') == 1 and passports[i].count('ecl') == 1 and passports[i].count('pid') == 1:
            count += 1
print(count)


# In[66]:


## Part 2

def find_srez(s, atribut):
    str = ''
    frm = s.find(atribut) + len(atribut) + 1
    to = s.find(' ', frm)
    if to != -1:
        str = s[frm:to]
    else:
        str = s[frm:]
    return str

## - a number followed by either cm or in:
## If cm, the number must be at least 150 and at most 193.
## If in, the number must be at least 59 and at most 76.
def valid_height(s):
    v = False
    if s.find('cm') > -1:
        h = int(s[0:hgt.find('cm')])
        if h >= 150 and h <= 193:
            v = True
    elif s.find('in') > -1:
        h = int(s[0:hgt.find('in')])
        if h >= 59 and h <= 76:
            v = True
    return v

## hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def valid_haircolor(s):
    v = False
    if (len(s) == 7 and s[0] == '#'):
        for i in range(1,7):
            if (s[i] >= str(0) and s[i] <= str(9)) or (s[i] >= 'a' and s[i] <= 'f'):
                v = True
            else:
                v = False
                break
    return v

## ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def valid_eyecolor(s):
    v = False
    if (s == 'amb' or s == 'blu' or s == 'brn' or s == 'gry' or s == 'grn' or s == 'hzl' or s == 'oth'):
        v = True
    return v

## pid (Passport ID) - a nine-digit number, including leading zeroes.
def valid_passportid(s):
    v = False
    if (len(s) == 9):
        for i in range(9):
            if (s[i] >= str(0) and s[i] <= str(9)):
                v = True
            else:
                v = False
                break
    return v

valid_count = 0
for i in range(0, len(passports)):
    if passports[i].count('byr') == 1 and passports[i].count('iyr') == 1 and passports[i].count('eyr') == 1:
        if passports[i].count('hgt') == 1 and passports[i].count('hcl') == 1 and passports[i].count('ecl') == 1 and passports[i].count('pid') == 1:
            byr = int(find_srez(passports[i], 'byr'))
            iyr = int(find_srez(passports[i], 'iyr'))
            eyr = int(find_srez(passports[i], 'eyr'))
            hgt = find_srez(passports[i], 'hgt')
            hcl = find_srez(passports[i], 'hcl')
            ecl = find_srez(passports[i], 'ecl')
            pid = find_srez(passports[i], 'pid')
            ## cid (Country ID) - ignored, missing or not.
            if (byr >= 1920 and byr <= 2002) and (iyr >= 2010 and iyr <= 2020) and (eyr >= 2020 and eyr <= 2030):
                if (valid_height(hgt) and valid_haircolor(hcl) and valid_eyecolor(ecl) and valid_passportid(pid)):
                    valid_count += 1
print(valid_count)

