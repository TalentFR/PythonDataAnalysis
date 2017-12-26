#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-07 15:33:10
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import sys
from datetime import datetime
import numpy as np

def numpysum(n):
	a = np.arange(n) ** 2
	b = np.arange(n) ** 3
	c = a+b
	return c

def pythonsum(n):
	a = list(range(n))
	b = list(range(n))
	c = []

	for i in range(len(a)):
		a[i] = i ** 2
		b[i] = i ** 3
		c.append(a[i] + b[i])
	return c

size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start

print("the last two elements of the sum", c[-2:])
print("the elapsed time in ms:", delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start

print("the last two elements of the sum", c[-2:])
print("the elapsed time in ms:", delta.microseconds)

