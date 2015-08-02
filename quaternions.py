from math import *

def hamilton_prod(a,b):
    a1,b1,c1,d1 = a[0],a[1],a[2],a[3]
    a2,b2,c2,d2 = b[0],b[1],b[2],b[3]
    a3 = a1*a2-b1*b2-c1*c2-d1*d2
    b3 = a1*b2+b1*a2+c1*d2-d1*c2
    c3 = a1*c2-b1*d2+c1*a2+d1*b2
    d3 = a1*d2+b1*c2-c1*b2+d1*a2
    return [a3,b3,c3,d3]

def rot_quaternion(u,theta):
    s = sin(theta/2)
    c = cos(theta/2)
    return [c,s*u[0],s*u[1],s*u[2]]

def conj_quaternion(q):
    return [q[0],-q[1],-q[2],-q[3]]

def vec_quaternion(v):
    return [0,v[0],v[1],v[2]]

def rotate(P,u,theta):
    p = vec_quaternion(P)
    u_mod = sqrt(u[0]**2+u[1]**2+ u[2]**2)
    u = [x/u_mod for x in u]
    q = rot_quaternion(u,theta)
    r = hamilton_prod(q,p)
    r = hamilton_prod(r,conj_quaternion(q))
    return [r[1],r[2],r[3]]

P = [1,2,3]
u = [1,1,1]
theta = 2*pi/3
P_rotated = rotate(P,u,theta)
print(P_rotated)
