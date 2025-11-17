from adafruit_circuitplayground import cp
import time



while True:
    cp.pixels.fill((0,255,0)) == True
    cp.pixels.brightness = 0.1
    time.sleep(0.367)
    cp.pixels.fill((0, 0, 0)) == True 
    cp.pixels.brightness = 0.1
    time.sleep(0.367)