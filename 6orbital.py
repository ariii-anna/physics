import math
def ask_T():
    T = float(input('how much time does it take to lap? '))
    return T
def ask_m():
    m = float(input('what is its mass? '))
    return m
def ask_M():
    M = float(input('what is the mass of the great heavenly body? '))
    return M
def ask_r():
    r = float(input('WHat is the radius or distance from the center of this planet to the other? '))
    return r

need = input('what do u need to calculate? T, M, r, vo or g: ').split()

def calc_all(need):
    for x in need:
        if(x=='T'):
            M = ask_M() 
            r = ask_r()
            G = 6.67*10**(-11)
            T = ((4*(r**3)*math.pi**2)/(G*M))**(1/2)
            print('T = ', T)
        elif(x=='M'):
            T=ask_T()
            r=ask_r()
            G= 6.67*10**(-11)
            M = (4*(math.pi**2)*r**3)/(G*T**2)
            print('M = ', M)
        elif(x=='g'):
            M=ask_M()
            r=ask_r()
            G= 6.67*10**(-11)
            g = (G*M/r**2)
            print('g = ', g)
        elif(x=='r'):
            M=ask_M()
            T=ask_T()
            G= 6.67*10**(-11)
            r = ((G*M*T**2)/(4*math.pi**2))**(1/3)
            print('r = ', r)
        elif(x=='vo'):
            M=ask_M()
            r=ask_r()
            G= 6.67*10**(-11)
            vo = ((G*M)/r)**(1/2)
            print('vo = ', vo)
        else:
            print('la proxima lo escribes bien, maricon')
    

print(calc_all(need))
