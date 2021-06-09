import machine
import utime
import time
import gc
from machine import *
from lcd_api import *
from pico_i2c_lcd import *

led = Pin(25, Pin.OUT)
led.low()

I2C_ADDR= 0x3F
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=4000000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.clear()


an_sw1 = machine.ADC(26)
#an_sw2 = machine.ADC(27)
#an_sw3 = machine.ADC(28)

sw1 = Pin(2, Pin.OUT)
sw2 = Pin(3, Pin.OUT)
sw3 = Pin(4, Pin.OUT)
sw4 = Pin(5, Pin.OUT)
sw5 = Pin(6, Pin.OUT)
sw6 = Pin(7, Pin.OUT)
sw7 = Pin(8, Pin.OUT)
sw8 = Pin(9, Pin.OUT)
sw9 = Pin(10, Pin.OUT)

var_1 = 0
var_2 = 0
var_3 = 0
var_4 = 0
var_5 = 0
var_6 = 0
var_7 = 0
var_8 = 0


def clearall():
    sw1.low()
    sw2.low()
    sw3.low()
    sw4.low()
    sw5.low()
    sw6.low()
    sw7.low()
    sw8.low()
    sw9.low()
    time.sleep(0.25)
    
def get_1():
    sw1.low()
    sw2.low()
    sw3.low()
    time.sleep(0.25)
    var1 = an_sw1.read_u16()
    time.sleep(0.25)
    print(var1)
#    lcd.putstr(str(var1))

def get_2():
    sw1.high()
    sw2.low()
    sw3.low()
    time.sleep(0.25)
    var2 = an_sw1.read_u16()
    time.sleep(0.25)
    print(var2)
    
def get_3():
    sw1.low()
    sw2.high()
    sw3.low()
    time.sleep(0.25)
    var3 = an_sw1.read_u16()
    time.sleep(0.25)
    print(var3)

def get_4():
    sw1.high()
    sw2.high()
    sw3.low()
    time.sleep(0.25)
    var4 = an_sw1.read_u16()
    time.sleep(0.25)
    print(var4)
    
def get_5():
    sw1.low()
    sw2.low()
    sw3.high()
    time.sleep(0.25)
    var5 = an_sw1.read_u16()
    time.sleep(0.25)
    print(var5)
    
def get_6():
    sw1.high()
    sw2.low()
    sw3.high()
    time.sleep(0.25)
    var6 = an_sw1.read_u16()
    time.sleep(0.25)
    print(var6)
    
def get_7():
    sw1.low()
    sw2.high()
    sw3.high()
    time.sleep(0.25)
    var7 = an_sw1.read_u16()
    time.sleep(0.25)
    print(var7)
    
def get_8():
    sw1.high()
    sw2.high()
    sw3.high()
    time.sleep(0.25)
    var8 = an_sw1.read_u16()
    time.sleep(0.25)
    print(var8)
    
    
#zde bude lůp
lcd.putstr("Ethernet tester     @Majklzbastlirny")
time.sleep(2)
clearall()
lcd.clear()

lcd.putstr("Merim drat 1")
get_1()
time.sleep(0.75)
clearall()
lcd.clear()

lcd.putstr("Merim drat 2")
get_2()
time.sleep(0.75)
clearall()
lcd.clear()

lcd.putstr("Merim drat 3")
get_3()
time.sleep(0.75)
clearall()
lcd.clear()

lcd.putstr("Merim drat 4")
get_4()
time.sleep(0.75)
clearall()
lcd.clear()

lcd.putstr("Merim drat 5")
get_5()
time.sleep(0.75)
clearall()
lcd.clear()

lcd.putstr("Merim drat 6")
get_6()
time.sleep(0.75)
clearall()
lcd.clear()

lcd.putstr("Merim drat 7")
get_7()
time.sleep(0.75)
clearall()
lcd.clear()

lcd.putstr("Merim drat 8")
get_8()
time.sleep(0.75)
clearall()
lcd.clear()

lcd.putstr("Zmereno")
led.toggle()      
utime.sleep(1)
led.toggle()
utime.sleep(0.2) 
led.toggle()
utime.sleep(1)
led.toggle()
utime.sleep(0.2) 

#generic
if var_1 > var_2 > var_3 > var_4 > var_5 > var_6 > var_7 > var_8:
    print("Vše ok")
    lcd.clear()
    lcd.putstr("Kabel OK")
    time.sleep(10)
    lcd.clear()
#full crossover    
elif var_3 > var_6 > var_1 > var_7 > var_8 > var_2 > var_4 > var_5:
    print("full crossover")
    lcd.clear()
    lcd.putstr("Je to               crossover kabel.")
    time.sleep(10)
    lcd.clear()
          
#half crossover    
elif var_3 > var_6 > var_1 > var_4 > var_5 > var_2 > var_7 > var_8:
    print("half crossover")
    lcd.clear()
    lcd.putstr("Je to               crossover kabel.")
    time.sleep(10)
    lcd.clear()
    
#oof
else:
    lcd.clear()
    print("undfnd")
    lcd.putstr("Kabel je vadny      :-(")
    time.sleep(10)
    lcd.clear()