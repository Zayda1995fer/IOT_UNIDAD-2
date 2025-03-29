import network
  from umqtt.simple import MQTTClient
  from machine import ADC, Pin
  from time import ticks_ms, ticks_diff, sleep
  import json
  
  - Propiedades para conectar a un cliente MQTT
  MQTT_BROKER = "192.168.137.138"
  MQTT_USER = ""
  MQTT_PASSWORD = ""
  MQTT_CLIENT_ID = "esp32_sensor_pulso"
  MQTT_TOPIC = "sensores/pulso"  # Tópico para el sensor de pulso
  MQTT_PORT = 1883
  
  - Configuración del pin del sensor KY-039 (modo analógico)
  SENSOR_PIN = 34  # Pin ADC para el sensor KY-039 (conectado al AO)
  sensor = ADC(Pin(SENSOR_PIN), atten=ADC.ATTN_11DB)
  
  - Variables para calcular la frecuencia cardíaca
  THRESHOLD = 2000  # Umbral para detectar un pulso
  last_time = None
  bpm = 0
  
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
          - Leer el valor analógico del sensor
          valor_analogico = sensor.read()  # Devuelve un valor entre 0 y 4095
  
          - Detectar un pulso cuando el valor supera el umbral
          if valor_analogico > THRESHOLD:
              current_time = ticks_ms()
              if last_time is not None:
                  - Calcular el tiempo entre pulsos
                  intervalo = ticks_diff(current_time, last_time) / 1000  # En segundos
                  bpm = int(60 / intervalo)  # Calcular BPM
                  print(f"BPM: {bpm}")
  
                  - Crear el mensaje con el valor del BPM
                  mensaje = {
                      "sensor": "pulso",
                      "valor_analogico": valor_analogico,
                      "bpm": bpm
                  }
  
                  print("Publicando:", mensaje)
                  client.publish(MQTT_TOPIC, json.dumps(mensaje))  # Enviar datos en formato JSON
  
              - Actualizar el tiempo del último pulso
              last_time = current_time
  
          sleep(0.05)  
  
      except Exception as e:
          print(f"Error: {e}")
          - Intentar reconectar al broker MQTT en caso de error
          try:
              client.disconnect()
              client = conecta_broker()
          except Exception as ex:
              print(f"Error al reconectar: {ex}")
