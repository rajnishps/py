import re

def num(name):
    fname = (name)
    sum = 0
    fh = open(fname)

    for line in fh:
        dig = re.findall('[0-9]+', line)
        for di in dig:
            sum += int(di)
    return sum

a=input("Enter File name: ")
x= num(a)
print(x)

#regex_sum_996616.txt