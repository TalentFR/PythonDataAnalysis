#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-22 10:37:29
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import scipy.misc
import matplotlib.pyplot as plt

im = scipy.misc.ascent()
xmax = im.shape[0]
ymax = im.shape[1]

im[range(xmax), range(ymax)] = 0
im[range(xmax-1, -1, -1), range(ymax)] = 0

plt.imshow(im)
plt.show()