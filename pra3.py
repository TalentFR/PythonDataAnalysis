#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-25 11:14:44
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import scipy.io.wavfile
import matplotlib.pyplot as plt
import urllib.request
import numpy as np

response = urllib.request.urlopen('http://www.thesoundarchive.com/austinpowers/smashingbaby.wav')
print(response.info())

WAV_FILE = 'smashingbaby.wav'
filehandle = open(WAV_FILE, 'wb+')
filehandle.write(response.read())
filehandle.close()

sample_rate, data = scipy.io.wavfile.read(WAV_FILE)

plt.subplot(2,1,1)
plt.title("Original")
plt.plot(data)

newdata = data*0.2
newdata = newdata.astype(np.uint8)

print("Data Type", newdata.dtype, "Shape", newdata.shape)

scipy.io.wavfile.write("quiet.wav", sample_rate, newdata)

plt.subplot(2,1,2)
plt.title("Quiet")
plt.plot(newdata)

plt.show()
