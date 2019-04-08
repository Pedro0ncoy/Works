#!/usr/bin/python
# -*- coding: utf-8 -*-

int x=0;y=0;m=0;
x = raw_input('ingrese x: ')
y = raw_input('ingrese y: ')
m=x*(x>y)+y*(y>x);
print "el mayor es",m
