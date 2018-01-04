#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-03 21:31:02
# @Author  : FR (teamo4869@163.com.)
# @Link    : http://FR.org
# @Version : $Id$

import numpy as np
import matplotlib.pyplot as plt

N = 10000

normal_values = np.random.normal(size = N)
dummy, bins, dummy = plt.hist(normal_values, int(np.sqrt(N)), normed=True, lw=1)
sigma = 1
mu = 0
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( -( bins - mu)**2 / (2 * sigma**2) ), lw=2)
plt.show()