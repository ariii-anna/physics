y0 = int(input('y0 Altura inicial del objeto en m  '))
v0 = int(input('v0 Velocidad inicial(si no ejerce fuerza es 0)'))
v = 0

vel = v0 - v
t = vel / 9.8

print('t, y0, v0', t, y0, v0)

y = y0 + v0 * t - 4.9 * t * t

print(y)
