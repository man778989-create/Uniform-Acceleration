#day 5
initial_velocity = 0 
acceleration = int(input('Enter acceleration:'))
time = int(input('Enter time:'))

v = initial_velocity + (acceleration * time)
s = (initial_velocity * time) + (0.5 * acceleration * time**2)
v_avg = initial_velocity + v / 2

print('Final velocity:', v)
print('Distance covered:', s)
print('Average velocity:', v_avg)

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
