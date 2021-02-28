from machine import ADC
import time

ANEMOMETRO = ADC(0)


def main():
    run = True
    
    while run:
        lecture = ANEMOMETRO.read_u16()
        print(lecture)
        time.sleep_ms(200)
        


if __name__ == "__main__":
    main()