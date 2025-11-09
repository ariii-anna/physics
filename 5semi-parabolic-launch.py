import math

y0 = float(input("altura desde la q se lanza:  "));
vx = float(input("velocidad a la q se lanza:  "));

y_final = -y0;
t_final = math.sqrt(y_final/-4.9);
x_max = vx*t_final;
vy_final = -9.8*t_final;

print("t vuelo:", t_final);
print("alcance maximo:", x_max);
print("vel a la q llega al suelo:", vy_final);

a = input('quieres saber algo mas?("si" o "no")');
if (a == 'si'):
    vyt = float(input('Vy cuando t= '));
    x_t = float(input('x cuando t= '));
    y_t = float(input('y cuando t= '));

    vy = -9.8*vyt;
    x = vx*x_t;
    y = y0+(-4.9*y_t*y_t);
    print('Vy cuando t=',vyt,':', vy, 'm/s');
    print('x cuando t=', x_t, ':', x, 'm');
    print('y cuando t=', y_t, ':', y, 'm');

elif(a == 'no'):
    print('eespero q estes satisfecho/a');
else:
    a; #esto ultimo no funciona hahjsh
