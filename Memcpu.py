from flask import Flask
from gpiozero import LED
import psutil

app = Flask(__name__)

@app.route('/helloWorld')
def helloW():
    return "Hello World"

@app.route('/CaracteristicasDelServidor')
def getCaracteristicas(): 
    memory = psutil.virtual_memory().used * 100 / psutil.virtual_memory().total
    cpu = psutil.cpu_percent(interval=1)
    return ("Memoria: " + str(memory) + "   CPU: " + str(cpu)) 


if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')