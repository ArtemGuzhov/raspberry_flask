from flask import Flask
from flask import request
import RPi.GPIO as GPIO
import ConfigParser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def open():
    if request.method == 'POST' and request.form['function'] == 'open':
        config = ConfigParser.RawConfigParser()            #воспользуемся конфигом
        config.read("/home/pi/global_config.conf")         #считаем конфиг
        pin_number = config.getint("relay_pins", "relay1") #пина из конфига присвоем переменной pin_number
        
        print "use pin:"+str(pin_number)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)            
        GPIO.setup(pin_number, GPIO.OUT)   #устанавливаем пин на выходной сигнал
        GPIO.output(pin_number, GPIO.HIGH) #ставим логическую еденицу на выходе
        return 'OK'
    else:
        print("Error")

    if request.method == 'POST' and request.form['function'] == 'close':
        config = ConfigParser.RawConfigParser()            #воспользуемся конфигом
        config.read("/home/pi/global_config.conf")         #считаем конфиг
        pin_number = config.getint("relay_pins", "relay1") #пина из конфига присвоем переменной pin_number
        
        print "use pin:"+str(pin_number)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)            
        GPIO.setup(pin_number, GPIO.OUT)   #устанавливаем пин на выходной сигнал
        GPIO.output(pin_number, GPIO.LOW)  #ставим логический ноль на выходе
        return 'OK'
    else:
        print("Error")

if __name__ == "__main__":
    app.run()
