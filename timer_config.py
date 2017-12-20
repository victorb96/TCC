import time

class timer_config(object):
    
    compressor = compressor()

    timeBomba = 0

    def __init__(time):
        timeBomba = time

    def timerBomba():

        if (timeBomba-time.time()) >= TIMER_BOMBA:
            
            compressor.ativarCompressor(False)
            return
        
    compressor.ativarCompressor(True)