from gpiozero import DistanceSensor
import subprocess

topic = "testTopic"
message = None
# Definir los pines GPIO para los LEDs y el sensor ultrasónico
sensor = DistanceSensor(echo=15, trigger=14)

# Construye el comando mosquitto_pub
command = ["mosquitto_pub", "-t", topic, "-m", message]

# Ejecuta el comando
try:
    while True:
        message = str(sensor.distance)
        subprocess.run(command, check=True)
        print(message)
except subprocess.CalledProcessError as e:
    print(f"Error al enviar el mensaje: {e}")
