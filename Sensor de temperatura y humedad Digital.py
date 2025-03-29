import network
  from umqtt.simple import MQTTClient
  from machine import Pin, ADC
  from time import sleep
  import json
  
  # Propiedades para conectar a un cliente MQTT
  MQTT_BROKER = "192.168.137.138"
  MQTT_USER = ""
  MQTT_PASSWORD = ""
  MQTT_CLIENT_ID = "esp32_sensor_temperatura"
  MQTT_TOPIC = "sensores/temperatura"
  MQTT_PORT = 1883
  
  # Configuración del pin ADC para el sensor LM35
  SENSOR_PIN = 34  # Pin GPIO34 (compatible con ADC)
  sensor = ADC(Pin(SENSOR_PIN))
  sensor.atten(ADC.ATTN_11DB)  # Configurar atenuación para un rango de 0-3.3V
  
  # Función para conectar a WiFi
  def conectar_wifi():
      print("Conectando a WiFi...", end="")
      sta_if = network.WLAN(network.STA_IF)
      sta_if.active(True)
      sta_if.connect('AURORA', '13082005')  # Cambia el SSID y la contraseña según tu red WiFi
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
          # Leer el valor  del sensor
          valor_sensor = sensor.read()  # Valor entre 0 y 4095 (12 bits)
  
          # Convertir el valor a temperatura en grados Celsius
          voltaje = valor_sensor * 3.3 / 4095  # Convertir a voltios
          temperatura = voltaje * 100  # LM35: 10mV por grado Celsius
  
          # Crear el mensaje JSON con los datos del sensor
          mensaje = {
              "sensor": "temperatura_analog",
              "valor": temperatura
          }
  
          # Publicar el mensaje al broker MQTT
          print("Publicando:", mensaje)
          client.publish(MQTT_TOPIC, json.dumps(mensaje))  # Enviar datos en formato JSON
  
      except Exception as e:
          print(f"Error: {e}")
          # Intentar reconectar al broker MQTT en caso de error
          try:
              client.disconnect()
              client = conecta_broker()
          except Exception as ex:
              print(f"Error al reconectar: {ex}")
  
      sleep(2)  # Esperar 2 segundos antes de la siguiente lectura
