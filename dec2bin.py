# convert decimal to binary
import pytest

num = 250
temp = num
bin = ""
while (num!=0):
  r = int(num%2)
  num = int(num/2)
  bin = bin+str(r)

bin = bin[::-1] #reverse the string
print(bin)
