# The file Ba137.txt contains two columns. The first is counts from a
# Geiger counter, the second is time in seconds.
# (a) Make a useful graph of this data.
# (b) If this data follows an exponential curve, then plotting the natural
# log of the data (or plotting the raw data on a logrithmic scale) will
# result in a straight line. Determine whether this is the case, and
# explain your conclusion with —you guessed it— an appropriate
# graph.

# Loading Giger counter data.
numberOfDecays, time = loadtxt('C:\OpenWormMatlab\OpenWormAcademy2014\Home_work\hw3\code_chapter_0\Ba137.txt', unpack = 'True')

#Useful graph of the Geiger counter signal.
figure();
plot(time, numberOfDecays, 'g*');     	#Geiger counter plot.
plot(time, log(numberOfDecays), 'r-^');  #Log plot of the Geiger counter plot to ascertain if the trend is exponential (base 2.718).

# Range
xlim(10.00, 470.00);
ylim(4e3, 30e3);

# Axis labels
xlabel( 'Time (s) ')
ylabel('Remaining substance')

# Title
title('Geiger counter reading.');


#Plot formatting for the LWR's position.
plt.subplot(2, 1, 1)
plt.plot(time, numberOfDecays, 'bo-')
plt.title('Geiger counter and log transformation of the data')
plt.ylabel('Original Geiger counter decays')
plt.ylim(4000, 30000)

#Plot formatting for the LWR's acceleration.
plt.subplot(2, 1, 2)
plt.plot(time, log(numberOfDecays), 'r^-')
plt.xlabel('Time (s)')
plt.ylabel('Log formula test')
plt.ylim(8, 11)