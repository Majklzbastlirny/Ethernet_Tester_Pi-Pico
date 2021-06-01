import machine
import utime
import time
import gc
from machine import *
from lcd_api import *
from pico_i2c import *



an_sw1 = machine.ADC(26)
an_sw2 = machine.ADC(27)
an_sw3 = machine.ADC(28)

sw1 = Pin(0, Pin.OUT)
sw2 = Pin(1, Pin.OUT)
sw3 = Pin(2, Pin.OUT)
sw4 = Pin(3, Pin.OUT)
sw5 = Pin(4, Pin.OUT)
sw6 = Pin(5, Pin.OUT)
sw7 = Pin(6, Pin.OUT)
sw8 = Pin(7, Pin.OUT)
sw9 = Pin(8, Pin.OUT)


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

def get_2():
    sw1.high()
    time.sleep(0.25)
    var2 = an_sw1.read_u16()
    time.sleep(0.25)
    sw1.low()


