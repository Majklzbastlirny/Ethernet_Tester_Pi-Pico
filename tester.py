import machine
import utime
import time
import gc
from machine import *
from lcd_api import *
from pico_i2c_lcd import *



I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    


an_sw1 = machine.ADC(26)
an_sw2 = machine.ADC(27)
an_sw3 = machine.ADC(28)

sw1 = Pin(2, Pin.OUT)
sw2 = Pin(3, Pin.OUT)
sw3 = Pin(4, Pin.OUT)
sw4 = Pin(5, Pin.OUT)
sw5 = Pin(6, Pin.OUT)
sw6 = Pin(7, Pin.OUT)
sw7 = Pin(8, Pin.OUT)
sw8 = Pin(9, Pin.OUT)
sw9 = Pin(10, Pin.OUT)


def clear():
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
    time.sleep(0.25)
    var1 = an_sw1.read_u16()
    time.sleep(0.25)
    print(var1)
#    lcd.putstr(str(var1))

def get_2():
    sw1.high()
    time.sleep(0.25)
    var2 = an_sw1.read_u16()
    time.sleep(0.25)
    sw1.low()
    
def get_3():
    sw1.high()
    time.sleep(0.25)
    var3 = an_sw1.read_u16()
    time.sleep(0.25)
    sw1.low()

def get_4():
    sw1.high()
    time.sleep(0.25)
    var4 = an_sw1.read_u16()
    time.sleep(0.25)
    sw1.low()
    
def get_5():
    sw1.high()
    time.sleep(0.25)
    var5 = an_sw1.read_u16()
    time.sleep(0.25)
    sw1.low()
    
def get_6():
    sw1.high()
    time.sleep(0.25)
    var6 = an_sw1.read_u16()
    time.sleep(0.25)
    sw1.low()
    
def get_7():
    sw1.high()
    time.sleep(0.25)
    var7 = an_sw1.read_u16()
    time.sleep(0.25)
    sw1.low()
    
def get_8():
    sw1.high()
    time.sleep(0.25)
    var8 = an_sw1.read_u16()
    time.sleep(0.25)
    sw1.low()
    
#zde bude lůp
lcd.putstr("Vadim blyat")
time.sleep(2)
lcd.clear()

lcd.putstr("Měřím drát 1")
get_1()
time.sleep(0.75)
lcd.clear()

lcd.putstr("Měřím drát 2")
get_2()
time.sleep(0.75)
lcd.clear()

lcd.putstr("Měřím drát 3")
get_3()
time.sleep(0.75)
lcd.clear()

lcd.putstr("Měřím drát 4")
get_4()
time.sleep(0.75)
lcd.clear()

lcd.putstr("Měřím drát 5")
get_5()
time.sleep(0.75)
lcd.clear()

lcd.putstr("Měřím drát 6")
get_6()
time.sleep(0.75)
lcd.clear()

lcd.putstr("Měřím drát 7")
get_7()
time.sleep(0.75)
lcd.clear()

lcd.putstr("Měřím drát 8")
get_8()
time.sleep(0.75)
lcd.clear()

lcd.putstr("Změřeno")

