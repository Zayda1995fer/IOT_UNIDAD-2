# IOT_UNIDAD-2

## 📹 1. Videos

### 🎥 Video 1: Sensores y Actuadores (20/40)

- Listados de videos
    * Modulo Interruptor de mercurio https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Modulo Enconder: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Modulo Joistick: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor de flama: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor de linea: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor tactil de metal: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Modulo red RGB: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Modulo Led RGB SMD: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor Infrorrojo: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Modulo Led Infrarrojo Receptor: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor Efecto Hall Analogo: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor de temperatura Analoga: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor de temperatura: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor led 7 colores: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor de temperatura y humedad: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor de pulso: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor de impacto: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor de campo magnatico: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Modulo de fotoresistencia: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
    * Sensor de flama: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
  
- La base de datos PostgreSQL.
  
- Explicación del código con documentación clara.
    # Modulo Interruptor de mercurio:
      import network
      from umqtt.simple import MQTTClient
      from machine import Pin
      from time import sleep
      import json
      
      - Propiedades para conectar a un cliente MQTT
      MQTT_BROKER = "192.168.137.138"
      MQTT_USER = ""
      MQTT_PASSWORD = ""
      MQTT_CLIENT_ID = "esp32_sensor_mercurio"
      MQTT_TOPIC = "sensores/mercurio"  # Tópico para el sensor de mercurio
      MQTT_PORT = 1883
      
       - Configuración del pin del sensor KY-017 (modo digital)
      SEN-SOR_PIN = 13  # Pin GPIO para el sensor KY-017 (conectado al DO)
      sensor = Pin(SENSOR_PIN, Pin.IN)
      
      - Función para conectar a WiFi
      def conectar_wifi():
          print("Conectando a WiFi...", end="")
          sta_if = network.WLAN(network.STA_IF)
          sta_if.active(True)
          sta_if.connect('AURORA', '13082005')  
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
      
              # Crear el mensaje con el estado del sensor
              mensaje = {
                  "sensor": "mercurio",
                  "estado": "inclinado" if estado_sensor == 0 else "no inclinado"
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
      
          sleep(0.5)  



    # Modulo Joistick:

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

      
    
   #  Sensor de flama:
      
      import network
      from umqtt.simple import MQTTClient
      from machine import Pin
      from time import sleep
      import json
      
      - Propiedades para conectar a un cliente MQTT
      MQTT_BROKER = "192.168.137.138"
      MQTT_USER = ""
      MQTT_PASSWORD = ""
      MQTT_CLIENT_ID = "esp32_sensor_gas_digital"
      MQTT_TOPIC = "sensores/gas"  # Tópico para el sensor de gas
      MQTT_PORT = 1883
      
      - Configuración del pin del sensor MQ-6 (modo digital)
      SENSOR_PIN = 13  # Pin GPIO para el sensor MQ-6 (conectado al DO)
      sensor = Pin(SENSOR_PIN, Pin.IN)
      
       -Función para conectar a WiFi
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
      
              - Crear el mensaje con el estado del sensor
              mensaje = {
                  "sensor": "gas",
                  "estado": "detectado" if estado_sensor == 0 else "no detectado"
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
      
          sleep(2)  -
 
      
    # Sensor de linea:
  
      import network
      from umqtt.simple import MQTTClient
      from machine import Pin
      from time import sleep
      import json
      
      - Propiedades para conectar a un cliente MQTT
      MQTT_BROKER = "192.168.137.138"
      MQTT_USER = ""
      MQTT_PASSWORD = ""
      MQTT_CLIENT_ID = "esp32_sensor_linea"
      MQTT_TOPIC = "sensores/linea"  # Tópico para el sensor de línea
      MQTT_PORT = 1883
      
      - Configuración del pin del sensor KY-033 (modo digital)
      SENSOR_PIN = 13  # Pin GPIO para el sensor KY-033 (conectado al DO)
      sensor = Pin(SENSOR_PIN, Pin.IN)
      
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
      
              - Crear el mensaje con el estado del sensor
              mensaje = {
                  "sensor": "linea",
                  "estado": "detectado" if estado_sensor == 0 else "no detectado"
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
      
          sleep(0.5)  - Esperar 0.5 segundos antes de la siguiente lectura
 
  
    # Sensor tactil de metal:
  
      import network
      from umqtt.simple import MQTTClient
      from machine import Pin
      from time import sleep
      import json
      
      - Propiedades para conectar a un cliente MQTT
      MQTT_BROKER = "192.168.137.138"
      MQTT_USER = ""
      MQTT_PASSWORD = ""
      MQTT_CLIENT_ID = "esp32_sensor_tactil"
      MQTT_TOPIC = "sensores/tactil"  # Tópico para el sensor táctil
      MQTT_PORT = 1883
      
      - Configuración del pin del sensor KY-036
      SENSOR_PIN = 13  # Pin GPIO para el sensor KY-036
      sensor = Pin(SENSOR_PIN, Pin.IN)
      
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
              # Leer el estado del sensor KY-036
              estado_sensor = sensor.value()
      
              - Crear el mensaje con el estado del sensor
              mensaje = {
                  "sensor": "tactil",
                  "estado": "tocando" if estado_sensor == 1 else "no tocando"
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
      
          sleep(2)  
    

    * Modulo red RGB:
 
                  import network
            from umqtt.simple import MQTTClient
            from machine import ADC, Pin
            from time import sleep
            import json
            
            # Propiedades para conectar a un cliente MQTT
            MQTT_BROKER = "192.168.137.138"
            MQTT_USER = ""
            MQTT_PASSWORD = ""
            MQTT_CLIENT_ID = "esp32_sensor_temperatura"
            MQTT_TOPIC = "sensores/temperatura"  # Tópico para el sensor de temperatura
            MQTT_PORT = 1883
            
            # Configuración del pin del sensor KY-028
            SENSOR_DIGITAL_PIN = 13  # Pin GPIO para el sensor KY-028 (conectado al DO)
            SENSOR_ANALOG_PIN = 34   # Pin ADC para el sensor KY-028 (conectado al AO)
            
            # Inicializar pines del sensor
            sensor_digital = Pin(SENSOR_DIGITAL_PIN, Pin.IN)
            sensor_analog = ADC(Pin(SENSOR_ANALOG_PIN), atten=ADC.ATTN_11DB)
            
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
            
            # Función para convertir el valor analógico a temperatura aproximada
            def analog_to_temperature(analog_value):
                # El termistor NTC tiene una relación no lineal entre resistencia y temperatura
                # Ajusta estos valores según las características específicas de tu sensor
                voltage = analog_value * (3.3 / 4095)  # Convertir valor analógico a voltaje
                resistance = (3.3 - voltage) / voltage * 10000  # Resistencia del termistor
                temperature = 1 / ((1 / 298.15) + (1 / 3950) * (3.3176471 * resistance)) - 273.15  # Fórmula de Steinhart-Hart
                return round(temperature, 2)
            
            # Conectar a WiFi
            conectar_wifi()
            
            # Conectar al broker MQTT
            client = conecta_broker()
            
            # Ciclo infinito
            while True:
                try:
                    # Leer el estado digital del sensor
                    estado_digital = sensor_digital.value()
            
                    # Leer el valor analógico del sensor
                    valor_analogico = sensor_analog.read()
            
                    # Convertir el valor analógico a temperatura
                    temperatura = analog_to_temperature(valor_analogico)
            
                    # Crear el mensaje con los datos del sensor
                    mensaje = {
                        "sensor": "temperatura",
                        "estado_digital": "umbral_alto" if estado_digital == 0 else "umbral_bajo",
                        "valor_analogico": valor_analogico,
                        "temperatura": temperatura
                    }
            
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
 # Modulo Led RGB SMD:
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
  
    
   # Sensor de temperatura:
      import network
      from umqtt.simple import MQTTClient
      from machine import ADC, Pin
      from time import sleep
      import json
      
      - Propiedades para conectar a un cliente MQTT
      MQTT_BROKER = "192.168.137.138"
      MQTT_USER = ""
      MQTT_PASSWORD = ""
      MQTT_CLIENT_ID = "esp32_sensor_temperatura"
      MQTT_TOPIC = "sensores/temperatura"  # Tópico para el sensor de temperatura
      MQTT_PORT = 1883
      
      - Configuración del pin del sensor KY-028
      SENSOR_DIGITAL_PIN = 13  # Pin GPIO para el sensor KY-028 (conectado al DO)
      SENSOR_ANALOG_PIN = 34   # Pin ADC para el sensor KY-028 (conectado al AO)
      
      - Inicializar pines del sensor
      sensor_digital = Pin(SENSOR_DIGITAL_PIN, Pin.IN)
      sensor_analog = ADC(Pin(SENSOR_ANALOG_PIN), atten=ADC.ATTN_11DB)
      
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
      
      - Función para convertir el valor analógico a temperatura aproximada
      def analog_to_temperature(analog_value):
          - El termistor NTC tiene una relación no lineal entre resistencia y temperatura
          - Ajusta estos valores según las características específicas de tu sensor
          voltage = analog_value * (3.3 / 4095)  # Convertir valor analógico a voltaje
          resistance = (3.3 - voltage) / voltage * 10000  # Resistencia del termistor
          temperature = 1 / ((1 / 298.15) + (1 / 3950) * (3.3176471 * resistance)) - 273.15  # Fórmula de Steinhart-Hart
          return round(temperature, 2)
      
      - Conectar a WiFi
      conectar_wifi()
      
      - Conectar al broker MQTT
      client = conecta_broker()
      
      - Ciclo infinito
      while True:
          try:
              - Leer el estado digital del sensor
              estado_digital = sensor_digital.value()
      
              - Leer el valor analógico del sensor
              valor_analogico = sensor_analog.read()
      
              # Convertir el valor analógico a temperatura
              temperatura = analog_to_temperature(valor_analogico)
      
              # Crear el mensaje con los datos del sensor
              mensaje = {
                  "sensor": "temperatura",
                  "estado_digital": "umbral_alto" if estado_digital == 0 else "umbral_bajo",
                  "valor_analogico": valor_analogico,
                  "temperatura": temperatura
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
      
          sleep(2)  - Esperar 2 segundos antes de la siguiente lectura
      
    # Sensor led 7 colores:
            import network
            from umqtt.simple import MQTTClient
            from machine import ADC, Pin
            from time import sleep
            import json
            
            # Propiedades para conectar a un cliente MQTT
            MQTT_BROKER = "192.168.137.138"
            MQTT_USER = ""
            MQTT_PASSWORD = ""
            MQTT_CLIENT_ID = "esp32_sensor_temperatura"
            MQTT_TOPIC = "sensores/temperatura"  # Tópico para el sensor de temperatura
            MQTT_PORT = 1883
            
            # Configuración del pin del sensor KY-028
            SENSOR_DIGITAL_PIN = 13  # Pin GPIO para el sensor KY-028 (conectado al DO)
            SENSOR_ANALOG_PIN = 34   # Pin ADC para el sensor KY-028 (conectado al AO)
            
            # Inicializar pines del sensor
            sensor_digital = Pin(SENSOR_DIGITAL_PIN, Pin.IN)
            sensor_analog = ADC(Pin(SENSOR_ANALOG_PIN), atten=ADC.ATTN_11DB)
            
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
            
            # Función para convertir el valor analógico a temperatura aproximada
            def analog_to_temperature(analog_value):
                # El termistor NTC tiene una relación no lineal entre resistencia y temperatura
                # Ajusta estos valores según las características específicas de tu sensor
                voltage = analog_value * (3.3 / 4095)  # Convertir valor analógico a voltaje
                resistance = (3.3 - voltage) / voltage * 10000  # Resistencia del termistor
                temperature = 1 / ((1 / 298.15) + (1 / 3950) * (3.3176471 * resistance)) - 273.15  # Fórmula de Steinhart-Hart
                return round(temperature, 2)
            
            # Conectar a WiFi
            conectar_wifi()
            
            # Conectar al broker MQTT
            client = conecta_broker()
            
            # Ciclo infinito
            while True:
                try:
                    # Leer el estado digital del sensor
                    estado_digital = sensor_digital.value()
            
                    # Leer el valor analógico del sensor
                    valor_analogico = sensor_analog.read()
            
                    # Convertir el valor analógico a temperatura
                    temperatura = analog_to_temperature(valor_analogico)
            
                    # Crear el mensaje con los datos del sensor
                    mensaje = {
                        "sensor": "temperatura",
                        "estado_digital": "umbral_alto" if estado_digital == 0 else "umbral_bajo",
                        "valor_analogico": valor_analogico,
                        "temperatura": temperatura
                    }
            
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
                * Sensor de temperatura y humedad: https://drive.google.com/drive/folders/11ZcGPM9Rlhlp8-2W7U3PeWrwDL5IE4IZ
      
   # Sensor de pulso:
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
      
   # Sensor de impacto:
      import network
      from umqtt.simple import MQTTClient
      from machine import Pin
      from time import sleep
      import json
      
      - Propiedades para conectar a un cliente MQTT
      MQTT_BROKER = "192.168.137.138"
      MQTT_USER = ""
      MQTT_PASSWORD = ""
      MQTT_CLIENT_ID = "esp32_sensor_impacto"
      MQTT_TOPIC = "sensores/impacto"  # Tópico para el sensor de impacto
      MQTT_PORT = 1883
      
      - Configuración del pin del sensor KY-031 (modo digital)
      SENSOR_PIN = 13  # Pin GPIO para el sensor KY-031 (conectado al DO)
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
      
              if estado_sensor == 0:  - Impacto detectado
                  mensaje = {
                      "sensor": "impacto",
                      "estado": "detectado"
                  }
                  led.on()  - Encender el LED
                  print("Impacto detectado!")
              else:  - Sin impacto
                  mensaje = {
                      "sensor": "impacto",
                      "estado": "no detectado"
                  }
                  led.off()  - Apagar el LED
      
        - Publicar el mensaje al broker MQTT
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
      
          sleep(0.1)  
      
          
   # Sensor de campo magnatico:
         import network
         from umqtt.simple import MQTTClient
         from machine import Pin
         from time import sleep
         import json
         
          Propiedades para conectar a un cliente MQTT
         MQTT_BROKER = "192.168.137.138"
         MQTT_USER = ""
         MQTT_PASSWORD = ""
         MQTT_CLIENT_ID = "esp32_sensor_mercurio"
         MQTT_TOPIC = "sensores/mercurio"  # Tópico para el sensor de mercurio
         MQTT_PORT = 1883
         
          Configuración del pin del sensor KY-017 (modo digital)
         SENSOR_PIN = 13  # Pin GPIO para el sensor KY-017 (conectado al DO)
         sensor = Pin(SENSOR_PIN, Pin.IN)
         
          Función para conectar a WiFi
         def conectar_wifi():
             print("Conectando a WiFi...", end="")
             sta_if = network.WLAN(network.STA_IF)
             sta_if.active(True)
             sta_if.connect('AURORA', '13082005')  # Cambia el SSID y la contraseña según tu red WiFi
             while not sta_if.isconnected():
                 print(".", end="")
                 sleep(0.3)
             print("\nWiFi Conectada!")
         
          Función para conectarse al broker MQTT
         def conecta_broker():
             client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=60)
             client.connect()
             print(f"Conectado al broker {MQTT_BROKER} en el tópico {MQTT_TOPIC}")
             return client
         
          Conectar a WiFi
         conectar_wifi()
         
          Conectar al broker MQTT
         client = conecta_broker()
         
          Ciclo infinito
         while True:
             try:
                  Leer el estado del sensor
                 estado_sensor = sensor.value()
         
                  Determinar si el LED está encendido o apagado
                 estado_led = "encendido" if estado_sensor == 0 else "apagado"
         
                  Crear el mensaje con el estado del sensor y el LED
                 mensaje = {
                     "sensor": "mercurio",
                     "estado": "inclinado" if estado_sensor == 0 else "no inclinado",
                     "led": estado_led
                 }
         
                 print("Publicando:", mensaje)
                 client.publish(MQTT_TOPIC, json.dumps(mensaje))  # Enviar datos en formato JSON
         
             except Exception as e:
                 print(f"Error: {e}")
                  Intentar reconectar al broker MQTT en caso de error
                 try:
                     client.disconnect()
                     client = conecta_broker()
                 except Exception as ex:
                     print(f"Error al reconectar: {ex}")
         
             sleep(0.5)  
      
   # Modulo de fotoresistencia: 
         import network
         from umqtt.simple import MQTTClient
         from machine import Pin
         from time import sleep
         import json
         
         # Propiedades para conectar a un cliente MQTT
         MQTT_BROKER = "192.168.137.138"
         MQTT_USER = ""
         MQTT_PASSWORD = ""
         MQTT_CLIENT_ID = "esp32_sensor_inclinacion"
         MQTT_TOPIC = "sensores/fotoresistencia" 
         MQTT_PORT = 1883
         
         # Configuración del pin del sensor KY-027 (modo digital)
         SENSOR_PIN = 13  # Pin GPIO para el sensor KY-027 (conectado al DO)
         sensor = Pin(SENSOR_PIN, Pin.IN)
         
         # Configuración del pin del LED (opcional)
         LED_PIN = 2  # Pin GPIO para el LED externo
         led = Pin(LED_PIN, Pin.OUT)
         
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
                 # Leer el estado del sensor
                 estado_sensor = sensor.value()
         
                 if estado_sensor == 0:  # Sensor inclinado
                     mensaje = {
                         "sensor": "inclinacion",
                         "estado": "inclinado"
                     }
                     led.on()  # Encender el LED
                 else:  # Sensor no inclinado
                     mensaje = {
                         "sensor": "inclinacion",
                         "estado": "no inclinado"
                     }
                     led.off()  # Apagar el LED
         
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
         
             sleep(0.5)  # Esperar 0.5 segundos antes de la siguiente lectura
   
   # Sensor de flama: 
            import network
         from umqtt.simple import MQTTClient
         from machine import Pin
         from time import sleep
         import json
         
         # Propiedades para conectar a un cliente MQTT
         MQTT_BROKER = "192.168.137.138"
         MQTT_USER = ""
         MQTT_PASSWORD = ""
         MQTT_CLIENT_ID = "esp32_sensor_inclinacion"
         MQTT_TOPIC = "sensores/flama"
         MQTT_PORT = 1883
         
         # Configuración del pin del sensor KY-027 (modo digital)
         SENSOR_PIN = 13  # Pin GPIO para el sensor KY-027 (conectado al DO)
         sensor = Pin(SENSOR_PIN, Pin.IN)
         
         # Configuración del pin del LED (opcional)
         LED_PIN = 2  # Pin GPIO para el LED externo
         led = Pin(LED_PIN, Pin.OUT)
         
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
                 # Leer el estado del sensor
                 estado_sensor = sensor.value()
         
                 if estado_sensor == 0:  # Sensor
                     mensaje = {
                         "sensor": "inclinacion",
                         "estado": "inclinado"
                     }
                     led.on()  # Encender el LED
                 else:  # Sensor no inclinado
                     mensaje = {
                         "sensor": "inclinacion",
                         "estado": "no inclinado"
                     }
                     led.off()  # Apagar el LED
         
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
         
             sleep(0.5)  # Esperar 0.5 segundos antes de la siguiente lectura

---

## 🔧 2. Ejercicio de Soldadura

Requisitos:
- Conectar **10 LEDs** y **10 resistencias** formando una figura creativa.
- Asegurar que cada LED encienda y apague individualmente.
- La soldadura debe ser **limpia** y sin cortocircuitos.

📌 **Ubicación:** `ejercicio_soldadura/`
- Esquema del circuito: `esquema_circuito.png`
- Instrucciones detalladas: `instrucciones.md`
- Evidencias en fotos: `evidencias_fotos/`

---

## 📝 3. Quizziz y NetAcad

CAPTURAS DEL NETACAD

![Imagen de WhatsApp 2025-03-07 a las 21 22 45_025d0ead](https://github.com/user-attachments/assets/b2badf59-00ce-4b28-a45b-0ab794a8066a)
![Imagen de WhatsApp 2025-03-07 a las 21 32 59_2dd00141](https://github.com/user-attachments/assets/55804119-3797-45be-9e11-e6f295973469)
![Imagen de WhatsApp 2025-03-07 a las 21 48 32_b3d71314](https://github.com/user-attachments/assets/77515bc8-3c92-4356-9abf-f430f0210895)
![Imagen de WhatsApp 2025-03-07 a las 21 48 34_e537b355](https://github.com/user-attachments/assets/62fa4c0b-3c57-4690-a9a1-eccddaff193c)
![Imagen de WhatsApp 2025-03-07 a las 21 58 02_b67f57ca](https://github.com/user-attachments/assets/c9e81279-71eb-4d60-846d-ddc43f47379d)
![Imagen de WhatsApp 2025-03-07 a las 22 23 23_412b2738](https://github.com/user-attachments/assets/95393cfc-febe-4b94-92b7-b240e98d3957)




---
