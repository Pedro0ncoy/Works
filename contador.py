#!/usr/bin/python
# -*- coding: utf-8 -*-


x = 1
m=100
e=0.1
while (m-(x**x)) < e:
	x=(x+(m/x))/2

print(x)
