import RPi.GPIO as GPIO

class motor(object):

    define = define()

    def ativarMotor(sinal):

        GPIO.setup(define.GPIO_COMPRESSOR, GPIO.OUT)

        if sinal:
            GPIO.output(define.GPIO_MOTORA, GPIO.HIGH)
            GPIO.output(define.GPIO_MOTORB, GPIO.LOW)
            GPIO.output(define.GPIO_MOTORE, GPIO.HIGH)
        else:
            GPIO.output(define.GPIO_MOTORE, GPIO.LOW)

    def move(sinal):
        
        GPIO.setup(define.GPIO_SERV, GPIO.OUT)

        pwm = GPIO.PWM(define.GPIO_SERV, 50)

        pwm.start(7.5)#INICIA O SERVO MOTOR NEUTRO
        
        if sinal == 0:
            pwm.ChangeDutyCycle(2.5)#SERVO MOTOR EM 0º
            pass
        elif sinal == 180:
            pwm.ChangeDutyCycle(12.5)#SERVO MOTOR EM 180º
            pass
        else:
            pwm.ChangeDutyCycle(7.5)##SERVO MOTOR EM 90º
            pass
        
