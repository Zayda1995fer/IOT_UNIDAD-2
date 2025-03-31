import network
from umqtt.simple import MQTTClient
from machine import ADC, Pin
from time import sleep
import json

# Propiedades para conectar a un cliente MQTT
MQTT_BROKER = "192.168.137.138"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = "esp32_microfono"
MQTT_TOPIC = "sensores/microfono"
MQTT_PORT = 1883

# Configuración del sensor de sonido
MIC_PIN = 34  # GPIO para la salida analógica del micrófono
microfono = ADC(Pin(MIC_PIN))
microfono.atten(ADC.ATTN_11DB)  # Ajuste para leer valores de 0 a 3.3V

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
    client
