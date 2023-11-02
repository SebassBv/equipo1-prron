from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Configura los pines GPIO para los LEDs :D
led_pins = [17, 27, 22]
GPIO.setmode(GPIO.BCM)
for pin in led_pins:
    
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


@app.route("/", methods=["GET", "POST"])
def method_post():
    return render_template("post_led.html")

@app.route('/led_post_act', methods=["POST"])
def method_post_act():
    if request.method == "POST":
        NumLed=-1
        NumLed =int(request.form["NumLed"]) 
        if 0 <= NumLed <= 7:
            for i, pin in enumerate(led_pins):
            # Verifica si el bit correspondiente está encendido
                if NumLed & (1 << i):
                    GPIO.output(pin, GPIO.HIGH)
                else:
                    GPIO.output(pin, GPIO.LOW)
                Respuesta="Encendidos para el número " + str(NumLed)
        else:
            Respuesta="Número no válido"
        return render_template("post_led.html", ret=Respuesta)
    
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')    
