from gpiozero import DistanceSensor
import subprocess
import time

topic = "gauge1"
message = None
# Definir los pines GPIO para los LEDs y el sensor ultrasónico
sensor = DistanceSensor(echo=15, trigger=14)
# Ejecuta el comando
while True:
    try:
        message = str((sensor.distance)*100)
        # Construye el comando mosquitto_pub
        command = ["mosquitto_pub", "-t", topic, "-m", message]
        subprocess.run(command, check=True)
        time.sleep(2)
    except subprocess.CalledProcessError as e:
        print(f"Error al enviar el mensaje: {e}")
