  import network
  from umqtt.simple import MQTTClient
  from machine import Pin
  from time import sleep
  import json
  
  - Propiedades para conectar a un cliente MQTT
  MQTT_BROKER = "192.168.137.138"
  MQTT_USER = ""
  MQTT_PASSWORD = ""
  MQTT_CLIENT_ID = "esp32_reed_switch"
  MQTT_TOPIC = "sensores/reed_switch"  # Tópico para el sensor reed switch
  MQTT_PORT = 1883
  
  - Configuración del pin del sensor KY-025 (modo digital)
  SENSOR_PIN = 13  # Pin GPIO para el sensor KY-025 (conectado al DO)
  sensor = Pin(SENSOR_PIN, Pin.IN)
  
  - Configuración del pin del LED (opcional)
  LED_PIN = 2  # Pin GPIO para el LED externo
  led = Pin(LED_PIN, Pin.OUT)
  
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
          - Leer el estado del sensor
          estado_sensor = sensor.value()
  
          if estado_sensor == 0:  # Interruptor cerrado (imán cerca)
              mensaje = {
                  "sensor": "reed_switch",
                  "estado": "cerrado"
              }
              led.on()  # Encender el LED
          else:  - Interruptor abierto (imán lejos)
              mensaje = {
                  "sensor": "reed_switch",
                  "estado": "abierto"
              }
              led.off()  - Apagar el LED
  
          - Publicar el mensaje al broker MQTT
          print("Publicando:", mensaje)
          client.publish(MQTT_TOPIC, json.dumps(mensaje))  - Enviar datos en formato JSON
  
      except Exception as e:
          print(f"Error: {e}")
          - Intentar reconectar al broker MQTT en caso de error
          try:
              client.disconnect()
              client = conecta_broker()
          except Exception as ex:
              print(f"Error al reconectar: {ex}")
  
      sleep(0.5)  - Esperar 0.5 segundos antes de la siguiente lectura
