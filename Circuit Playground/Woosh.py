from adafruit_circuitplayground import cp
import time



while True:
    if cp.button_a:
        for i in range(10):
            cp.pixels[i] = (0,150,0)
            time.sleep(0.1)
            cp.pixels[i] = (0, 0, 0)
            time.sleep(0.1)




