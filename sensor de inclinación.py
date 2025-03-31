import network
from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep
import json

# Propiedades para conectar a un cliente MQTT
MQTT_BROKER = "192.168.137.138"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = "esp32_inclinacion"
MQTT_TOPIC = "sensores/inclinacion"
MQTT_PORT = 1883

# Configuración del pin del sensor de inclinación (entrada digital)
INCLINACION_PIN = 15  # Pin GPIO para el sensor de inclinación
sensor_inclinacion = Pin(INCLINACION_PIN, Pin.IN, Pin.PULLUP)  # Configuración del pin en modo de entrada con pull-up interno

# Función para conectar a WiFi
def conectar_wifi():
    print("Conectando a WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('AURORA', '13082005')  
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("\nWiFi Conectada!")

# Función para conectarse al broker MQTT
def conecta_broker():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=60)
    client.connect()
    print(f"Conectado al broker {MQTT_BROKER} en el tópico {MQTT_TOPIC}")
    return client

# Conectar a WiFi
conectar_wifi()

# Conectar al broker MQTT
client = conecta_broker()

# Ciclo infinito
while True:
    try:
        # Leer el estado del sensor de inclinación (0 cuando está inclinado, 1 cuando está en posición normal)
        estado_inclinacion = "inclinado" if sensor_inclinacion.value() == 0 else "normal"

        # Crear el mensaje con el estado del sensor de inclinación
        mensaje = {
            "sensor": "inclinacion",
            "estado": estado_inclinacion
        }

        print("Publicando:", mensaje)
        client.publish(MQTT_TOPIC, json.dumps(mensaje))  # Enviar los datos en formato JSON

    except Exception as e:
        print(f"Error: {e}")
        # Intentar reconectar al broker MQTT en caso de error
        try:
            client.disconnect()
            client = conecta_broker()
        except Exception as ex:
            print(f"Error al reconectar: {ex}")

    sleep(1)  # Leer el estado del sensor de inclinación cada 1 segundo
