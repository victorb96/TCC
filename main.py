import RPi.GPIO as GPIO
import time

def main(*argv):
    
    motor = motor()
    compressor = compressor()
    
    while True:
        
        #INICIA
        motor.ativarMotor(True)

        compressor.ativarCompressor(True)
        tmpComp = time.time()

        timer = timer_config(tmpComp)

        timer.timerBomba()
