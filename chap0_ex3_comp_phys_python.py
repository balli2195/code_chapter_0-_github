# The data in file Ba137.txt is actual data from a radioactive decay
# experiment; the first column is the number of decays N , the second is
# the time t in seconds. We’d like to know the half-life t1/2 of Ba137. 
# It should follow the decay equation
#
# 						N = No*exp(−λt)
# 
# where λ = (log 2)/ (t1/2). Using the techniques you’ve learned in this 
# chapter, load the data from file Ba137.txt into appropriately-named 
# variables in an ipython session. Experiment with different values of N and λ
# and plot the resulting equation on top of the data. (Python uses exp()
# calculate the exponential function: i.e. y = A∗exp(−L∗time) ). 
# 
# Don’t worry about automating this process yet (unless you really want to!)
# just try adjusting things by hand until the equation matches the data
# pretty well. What is your best estimate for t1/2?

from scipy.optimize import curve_fit #For usage in fitting precisely.

# Loading Giger counter data.
numberOfDecays, time = loadtxt('C:\OpenWormMatlab\OpenWormAcademy2014\Home_work\hw3\code_chapter_0\Ba137.txt', unpack = 'True')

# My best estimate of the parameters is roughly to measure 
# how long does it take to get half of the material to decay.
# My estimate is (13587 delays, 190 seconds). Try in another program
# the automated fit.
numberOfDecaysAproximation = numberOfDecays[0] * exp(-(log(2)/190)*time)

figure();
plot(time, numberOfDecays, 'g*');     			#Geiger counter plot.
plot(time, numberOfDecaysAproximation, 'y-*');	#Rough aproximation plot.
