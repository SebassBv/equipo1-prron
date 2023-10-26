import subprocess
import random

topic = "gauge1"
message = None

message = str(random.randint(1,100))


# Construye el comando mosquitto_pub
command = ["mosquitto_pub", "-t", topic, "-m", message]

# Ejecuta el comando
try:
    subprocess.run(command, check=True)
    #print(f"Mensaje enviado: {message}")
    print(message)
except subprocess.CalledProcessError as e:
    print(f"Error al enviar el mensaje: {e}")