import subprocess

topic = "testTopic"
message = "Funciona!!"

# Construye el comando mosquitto_pub
command = ["mosquitto_pub", "-t", topic, "-m", message]

# Ejecuta el comando
try:
    subprocess.run(command, check=True)
    print(f"Mensaje enviado: {message}")
except subprocess.CalledProcessError as e:
    print(f"Error al enviar el mensaje: {e}")