from math import acos,pi

def sss(a:int, b:int, c:int) -> int:
    return round( 180/pi*acos((b**2 + c**2 - a**2)/(2*b*c)))


def get_angle(a:int, b:int, c:int) -> int:
    alpha = sss(a,b,c)
    beta  = sss(b,a,c)
    gamma = 180 - alpha - beta
    print(alpha,beta,gamma)

    if (alpha and beta and gamma < 90):
        print('Acute angle  ')
    elif ( alpha or beta or gamma == 90):
        print('Right angle')
    elif ( alpha or beta or gamma > 90 and alpha or beta or gamma < 180):
        print('Obtuse angle')
    elif (  alpha or beta or gamma >= 180):
        print('Non triangle')

get_angle(3,4,5)