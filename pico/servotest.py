from machine import Pin, PWM
from time import sleep



# Configure the GPIO pin for PWM
pwm_pin1 = Pin(17)
pwm1 = PWM(pwm_pin1)

pwm_pin2 = Pin(2)
pwm2 = PWM(pwm_pin2)

pwm_pin3 = Pin(3)
pwm3 = PWM(pwm_pin3)

pwm_pin4 = Pin(2)
pwm4 = PWM(pwm_pin4)

pwm_pin5 = Pin(3)
pwm5 = PWM(pwm_pin5)
# Set the PWM frequency to 50 kHz
pwm1.freq(50)
pwm2.freq(50)
pwm3.freq(50)
pwm4.freq(50)
pwm5.freq(50)


time_delay = 1 
max_angle = 180
min_angle = 0

global current_angle1 
global current_angle2 
global current_angle3 
global current_angle4 
global current_angle5 
'''
# Function: deg_to_time
# Parameters: deg : degree (0 - 180)
# Description: This function takes the degree and translates them
                to Pulse Width time.
                For a servo motor we have to use a pulse width of 500us to 2500us

'''
def deg_to_time(deg):
    temp = ((deg/90)+0.5)
    return temp

'''
# Function: timems_to_duty
# Parameters: timems : pulse width time in milli second
# Description: This function takes pulse width duration of 500us to 2500us.
                and generates a duty cycle value.

'''
def timems_to_duty(timems):
    temp = 20/timems
    temp1 = 65535/temp
    return temp1

'''
# Function: set_pwm
# Parameters: duty : duty cycle value (0 - 65535)
# Description: This function takes a duty cycle value and set it for the PWM.

'''
def set_pwm1(duty):
    pwm1.duty_u16(int(duty))
    
def angle_to_pwm1(angle):
    global current_angle1
    set_pwm1(int(timems_to_duty(deg_to_time(angle))))
    current_angle1 = angle

def add_angle1(angle):
    global current_angle1
    current_angle1 += angle
    angle_to_pwm1(current_angle1)
    
def set_max1():
    angle_to_pwm1(max_angle)

def set_min1():
    angle_to_pwm1(min_angle)
    
def sweep1(start, end, step):
    for angle in range(start, end, step):
        angle_to_pwm1(angle)
        sleep(time_delay)

def reset1():
    angle_to_pwm1(0)

#servo 2
def set_pwm2(duty):
    pwm2.duty_u16(int(duty))

def angle_to_pwm2(angle):
    global current_angle2
    set_pwm2(int(timems_to_duty(deg_to_time(angle))))
    current_angle2 = angle

def add_angle2(angle):
    global current_angle2
    current_angle2 += angle
    angle_to_pwm1(current_angle2)
    
def set_max2():
    angle_to_pwm2(max_angle)

def set_min2():
    angle_to_pwm2(min_angle)
    
def sweep2(start, end, step):
    for angle in range(start, end, step):
        angle_to_pwm2(angle)
        sleep(time_delay)

def reset2():
    angle_to_pwm2(0)
    
#servo 3
def set_pwm3(duty):
    pwm3.duty_u16(int(duty))

def angle_to_pwm3(angle):
    global current_angle3
    set_pwm3(int(timems_to_duty(deg_to_time(angle))))
    current_angle3 = angle

def add_angle3(angle):
    global current_angle3
    current_angle3 += angle
    angle_to_pwm1(current_angle3)
    
def set_max3():
    angle_to_pwm3(max_angle)

def set_min3():
    angle_to_pwm3(min_angle)
    
def sweep3(start, end, step):
    for angle in range(start, end, step):
        angle_to_pwm3(angle)
        sleep(time_delay)

def reset3():
    angle_to_pwm3(0)

#servo 4
def set_pwm4(duty):
    pwm4.duty_u16(int(duty))

def angle_to_pwm4(angle):
    global current_angle4
    set_pwm4(int(timems_to_duty(deg_to_time(angle))))
    current_angle4 = angle

def add_angle4(angle):
    global current_angle4
    current_angle4 += angle
    angle_to_pwm1(current_angle4)
    
def set_max4():
    angle_to_pwm4(max_angle)

def set_min4():
    angle_to_pwm4(min_angle)
    
def sweep4(start, end, step):
    for angle in range(start, end, step):
        angle_to_pwm4(angle)
        sleep(time_delay)

def reset4():
    angle_to_pwm4(0)
    
def set_pwm5(duty):
    pwm5.duty_u16(int(duty))

def angle_to_pwm5(angle):
    global current_angle5
    set_pwm5(int(timems_to_duty(deg_to_time(angle))))
    current_angle5 = angle

def add_angle5(angle):
    global current_angle5
    current_angle5 += angle
    angle_to_pwm1(current_angle5)
    
def set_max5():
    angle_to_pwm5(max_angle)

def set_min5():
    angle_to_pwm5(min_angle)
    
def sweep5(start, end, step):
    for angle in range(start, end, step):
        angle_to_pwm5(angle)
        sleep(time_delay)

def reset5():
    angle_to_pwm5(0)

while True:
    set_max1()
    sleep(time_delay)
    set_min1()
    sleep(time_delay)
    add_angle1(10)
    sleep(time_delay)