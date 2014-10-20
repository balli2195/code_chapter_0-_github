# Graph both of the following functions on a single figure, with a usefully sized scale.
# (a) x**4 * exp(−2x)
# (b) (x**2 * e(−x) * sin(x**2))**2
# Make sure your figure has legend, range, title, axis labels, and so on.

# The time array contains (N=50) 50 data points over 5 seconds.
startingPoint = 0.0
endingPoint = 10.0
N = 1000

positionArray = linspace(startingPoint, endingPoint, N);


figure();
plot(positionArray, (positionArray**4) * exp(-2*positionArray), 'r-');
plot(positionArray, ((positionArray**2) * exp(-positionArray) * sin(positionArray**2))**2, 'g^');

# legend
legend( ['damped', 'constant amplitude'], loc = 'upper right')

# range
xlim(0, 10);
ylim(0, 0.3);


# title
title('My first graph.');

# axis labels
xlabel( 'Horizontal Position (m)')
ylabel('Vertical Position (m)')