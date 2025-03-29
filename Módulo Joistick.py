import network
from umqtt.simple import MQTTClient
from machine import ADC, Pin
from time import sleep
import json

- Propiedades para conectar a un cliente MQTT
MQTT_BROKER = "192.168.137.138"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = "esp32_joystick"
MQTT_TOPIC = "sensores/joystick"  # Tópico para el joystick
MQTT_PORT = 1883

- Configuración del joystick
JOYSTICK_X_PIN = 34  # Pin ADC para el eje X (VRx)
JOYSTICK_Y_PIN = 35  # Pin ADC para el eje Y (VRy)
JOYSTICK_BUTTON_PIN = 13  # Pin digital para el botón (SW)

- Inicializar ADC para los ejes X e Y
joystick_x = ADC(Pin(JOYSTICK_X_PIN), atten=ADC.ATTN_11DB)
joystick_y = ADC(Pin(JOYSTICK_Y_PIN), atten=ADC.ATTN_11DB)

- Inicializar el botón como entrada digital
joystick_button = Pin(JOYSTICK_BUTTON_PIN, Pin.IN, Pin.PULL_UP)

- Función para conectar a WiFi
def conectar_wifi():
    print("Conectando a WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('AURORA', '13082005')  # Cambia el SSID y la contraseña según tu red WiFi
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("\nWiFi Conectada!")

- Función para conectarse al broker MQTT
def conecta_broker():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=60)
    client.connect()
    print(f"Conectado al broker {MQTT_BROKER} en el tópico {MQTT_TOPIC}")
    return client

- Conectar a WiFi
conectar_wifi()

- Conectar al broker MQTT
client = conecta_broker()

- Ciclo infinito
while True:
    try:
          - Leer los valores de los ejes X e Y
          x_value = joystick_x.read()  # Valor entre 0 y 4095
          y_value = joystick_y.read()  # Valor entre 0 y 4095

        - Determinar la dirección basada en los valores de X e Y
        - Dividimos el rango de 0-4095 en tres zonas: izquierda/centro/derecha y arriba/centro/abajo
        if x_value < 1000:
            direccion_x = "izquierda"
        elif x_value > 3000:
            direccion_x = "derecha"
        else:
            direccion_x = "centro_x"

        if y_value < 1000:
            direccion_y = "arriba"
        elif y_value > 3000:
            direccion_y = "abajo"
        else:
            direccion_y = "centro_y"

        - Leer el estado del botón
        boton_presionado = "presionado" if joystick_button.value() == 0 else "no presionado"

        - Crear el mensaje con los datos del joystick
        mensaje = {
            "sensor": "joystick",
            "direccion_x": direccion_x,
            "direccion_y": direccion_y,
            "boton": boton_presionado
        }

        print("Publicando:", mensaje)
        client.publish(MQTT_TOPIC, json.dumps(mensaje))  # Enviar datos en formato JSON

    except Exception as e:
        print(f"Error: {e}")
        - Intentar reconectar al broker MQTT en caso de error
        try:
            client.disconnect()
            client = conecta_broker()
        except Exception as ex:
            print(f"Error al reconectar: {ex}")

    sleep(0.2)  
