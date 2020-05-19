import math
#to_cartesian accepts x and y coordinates and returns equivalent polar coordinates
#it returns an array having the first element as radius and second as angle in degrees

def to_polar(x,y):
    x=float(x)
    y=float(y)
    theta=math.atan(y/x)
    theta=180/math.pi*theta

    radius=math.sqrt(x**2 + y**2)
    pol_cod=list()
    pol_cod.append(radius)
    pol_cod.append(theta)
    return pol_cod
#to_cartesian accepts radius and angle in  degrees  and returns equivalent cartesian coordinates
#it returns an array having the first element x coordinate and second element is y coordinate
def to_cartesian(r,theta):
    r=float(r)
    theta=float(theta)
    theta=math.pi/180*theta
    x=r*math.cos(theta)
    y=r*math.sin(theta)

    cart_cod=list()
    cart_cod.append(x)
    cart_cod.append(y)
    return cart_cod
