v0 = int(input('v0  What is the initial velocity in seconds?  '))
t_final = int(input('t  What is the time in secs from the start to the end?  '))
t0 = int(input('t0  What is the time from the context start until the object starts in secs?  '))
a = int(input('a  What is the aceleration of the object in m/s?  '))

t = t_final - t0

x = -v0 * t + 1/2 * a * t * t
print('Distance: ', int(x),'m')
