#day 6
#task 5 Uniform Acceleration
u = 0
a = int(input('Enter the acceleration (m/s^2):'))
t = int(input('Enter the time (s):'))

#Final velocity
v = u + (a * t)

#distance traveled 
s = u*t+(a*t**2)/2

#Average velocity
v_avg = (u+v) / 2

print('Final velocity:', v, 'm/s')
print('Distance traveled:', s, 'm')
print('Average velocity:', v_avg, 'm/s')
