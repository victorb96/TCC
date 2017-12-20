import RPi.GPIO as GPIO

class compressor(object):

    define = defines()

    def ativarCompressor(sinal):

        GPIO.setup(define.GPIO_COMPRESSOR, GPIO.OUT)

        if sinal:
            GPIO.output(define.GPIO_COMPRESSOR, GPIO.HIGH)
        else:
            GPIO.output(define.GPIO_COMPRESSOR, GPIO.LOW)
        
