#20km/h --> 2500
#30km/h -> 4000
#40km/h --> 5500
#y-y0 = m(x-x0)
#m = (5500-4000)/(40-30) = 150
#x = (y-2500)/150 + 20

from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from machine import ADC, Pin, I2C
import time


NUM_ROWS = 2
NUM_COLS = 16
SDA = Pin(0)
SCL = Pin(1)
i2c = I2C(0, sda=SDA, scl=SCL, freq = 400000)
#print(i2c.scan())
I2C_ADDR = 0x27
LCD = I2cLcd(i2c, I2C_ADDR, NUM_ROWS, NUM_COLS)

SENSOR_TEMP = ADC(4)
CONVERSION_FACTOR = 3.3/65535

ANEMOMETRO = ADC(0)


def main():
    run = True
    
    while run:
        temp_reading = SENSOR_TEMP.read_u16() * CONVERSION_FACTOR
        temperature = round(37 - (temp_reading - 0.706)/0.001721, 2)
        LCD.clear()
        LCD.move_to(0,0)
        LCD.putstr("Temp: ")
        LCD.putstr(str(temperature))
        LCD.putstr(" C")
        LCD.move_to(0,1)
        LCD.putstr("Viento: ")
        wind_reading = ANEMOMETRO.read_u16()
        if wind_reading < 2500:
            LCD.putstr("NULL")
            
        else:
            wind = round((wind_reading-2500)/150 + 20,2)
            LCD.putstr(str(wind) + " km/h")
        
        
        print(temperature)
        time.sleep(3)



if __name__ == "__main__":
    main()