vf = int(input('vf What is the final velocity in m/s?  '))
v0 = int(input('v0 What is the initial velocity in m/s?  '))
tf = int(input('tf What is the time spent in this experiment in s?  '))
t0 = int(input('t0 What is the time from when it starts to when it ends with the context in s?  '))

t = tf - t0
v = vf - v0
a = v/t
print('Aceleration: ',int(a), 'm/s^2')
