#Plot the trajectory of a free falling object.
#Create a single plot that shows separate graphs of position, velocity,
#and acceleration for an object in free-fall. Your plot should have a 
#single horizontal time axis and separate stacked graphs showing position,
#velocity, and acceleration each on their own vertical axis. (See figure
#3.) The online matplotlib gallery will probably be helpful! Print the
#graph, with your name in the title

#import pylab odeint
from pylab import *
from scipy.integrate import odeint

#Time array for the Large Wooden Rabit's (LWR) position, velocity, and acceleration.
tmin = 0;
tmax = 3;
N = 100;

time = linspace(tmin, tmax, N);

#Initial conditions array.
initialPositionLWR = 0.0;
initialVelocityLWR = 15.0;

#Earth's gravitational constant in [m/s^2].
gravitationalAcceleration = 9.81

initialConditionsLWR = [initialPositionLWR,initialVelocityLWR, -gravitationalAcceleration];

#The LWR's equations of motions.
#A callable function must be declared in order to use the 'odeint' function.
def LWREquationsOfMotion(y, t): 
	g0 = y[1] #position_derivative = y[1]
	g1 = y[2] #velocity_derivative = y[2]
	return array([g0,g1]) #array([position_derivative,velocity_derivative])

#Solve the LWR's differential equations of motion.
LWRDynamics = odeint(LWREquationsOfMotion, initialConditionsLWR, time)

#Obtain the position, velocity, and acceleration 100x1 arrays from the LWRDynamics 100x3 array.
position_solution = LWRDynamics[:,0];
velocity_solution = LWRDynamics[:,1];
acceleration_solution = LWRDynamics[:,2];

#Geiger Counter plots.
#Plot formatting for the LWR's position.
plt.subplot(2, 1, 1)
plt.plot(time, position_solution, 'bo-')
plt.title('Geiger counter data')
plt.ylabel('Position, m')
plt.ylim(0, 12)

#Plot formatting for the LWR's acceleration.
plt.subplot(3, 1, 3)
plt.plot(time, acceleration_solution, 'r^-')
plt.xlabel('time (s)')
plt.ylabel('Geiger counter exponential fit test')
plt.ylim(-15, 15)

plt.show()
