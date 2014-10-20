# The data shown in figure 2 is most usefully analyzed by looking at the
# ratio of the two microphone signals. Plot this ratio, with frequency
# on the x axis. Be sure to clean up the graph with appropriate scales,
# axes labels, and a title.

# The frequency spectrum from two microphone signals.
frequency, mic1, mic2 = loadtxt('C:\OpenWormMatlab\OpenWormAcademy2014\Home_work\hw3\code_chapter_0\microphones.txt', unpack = 'True')

#Plot of the frequency domain signals.
figure();
#plot(frequency, mic1/mic2, 'm-'); 			  #Plot of the magnitude ratio.
plot(frequency, log(mic1/mic2)/log(10), 'g'); #Plot of the logarithm of the magnitude ratio. Using base 10 logarithms.

# Range
xlim(10.00, 2999.00);
ylim(0, 2.5);

# Axis labels
xlabel( 'Frequency (Hz)')
ylabel('log-Ratio of two microphone signals (dB)')

# Title
title('Ratio of two microphone signals.');

