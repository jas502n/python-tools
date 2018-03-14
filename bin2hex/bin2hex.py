#!/usr/bin/python
# -*- coding: utf-8 -*-

###进制的转换

### bin2ten
### 2进制转10进制
### 1000100111011000
print "_____________________________________________________"
print "***********wwww.canyouseeme.cc *************"
print "************Author By Jas502n*************"
print "\n2进制转10进制\n"
print "例如  bin = 1000100111011000"

###dec = int(input("输入数字 ="))
## 默认输入10进制

s = int(raw_input("请输入2进制 = "),2)

print "\n"

print "转换为2进制为 = ", bin(s)
print "转换为8进制为 = ", oct(s)
print "10进制数为 = ", s
print "转换为16进制为 = ", hex(s)

####  oct2ten
print "_____________________________________________________"
print "\n8进制转10进制\n"

y = int(raw_input("请输入8进制 = "),8)

print "\n"

print "转换为2进制为 = ", bin(y)
print "转换为8进制为 = ", oct(y)
print "10进制数为 = ", y
print "转换为16进制为 = ", hex(y)

#### hex2ten
print "_____________________________________________________"
print "\n16进制转10进制\n"

x = int(raw_input("请输入16进制 = "),16)

print "\n"

print "转换为2进制为 = ", bin(x)
print "转换为8进制为 = ", oct(x)
print "10进制数为 = ", y
print "转换为16进制为 = ", hex(x)
### 
print "_____________________________________________________"

