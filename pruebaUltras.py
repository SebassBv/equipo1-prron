from gpiozero import DistanceSensor
import subprocess

topic = "gauge1"
message = None
# Definir los pines GPIO para los LEDs y el sensor ultrasónico
sensor = DistanceSensor(echo=15, trigger=14)

message = str(sensor.distance)

# Construye el comando mosquitto_pub
command = ["mosquitto_pub", "-t", topic, "-m", message]

# Ejecuta el comando
while True:
    try:
        subprocess.run(command, check=True)
        print(message)
    except subprocess.CalledProcessError as e:
        print(f"Error al enviar el mensaje: {e}")
