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
  
  
## 🔧 2. Ejercicio de Soldadura

Requisitos:
- Conectar **10 LEDs** y **10 resistencias** formando una figura creativa.
- Asegurar que cada LED encienda y apague individualmente.
- La soldadura debe ser **limpia** y sin cortocircuitos.

- Esquema del circuito:
  ![Imagen de WhatsApp 2025-03-20 a las 08 30 17_bf6656d7](https://github.com/user-attachments/assets/a5458eac-7e57-43fb-86f0-869cb802706f)

- Instrucciones detalladas:

            from machine import Pin
            from time import sleep
            
            # Configuración de los pines GPIO para los grupos de LEDs
            cuerpo = Pin(13, Pin.OUT)    # GPIO13 - Cuerpo (4 LEDs)
            aletas = Pin(14, Pin.OUT)    # GPIO14 - Aletas (2 LEDs)
            cola = Pin(12, Pin.OUT)      # GPIO12 - Cola (2 LEDs)
            ojos = Pin(26, Pin.OUT)      # GPIO26 - Ojos (2 LEDs)
            efecto_especial = Pin(27, Pin.OUT)  # GPIO27 - Efecto especial (nuevo grupo)
            
            # Función para apagar todos los grupos de LEDs excepto los ojos
            def apagar_todos():
                cuerpo.off()
                aletas.off()
                cola.off()
                efecto_especial.off()
            
            # Efecto de "nadar" (simula movimiento del pez)
            def nadar():
                # Encender los ojos (siempre encendidos)
                ojos.on()
                
                # Movimiento del cuerpo y efectos adicionales (encender y apagar en secuencia)
                for _ in range(2):  # Repetir el efecto 2 veces
                    cuerpo.on()     # Encender el cuerpo
                    sleep(0.3)
                    
                    apagar_todos()
                    aletas.on()     # Encender las aletas
                    sleep(0.3)
                    
                    apagar_todos()
                    cola.on()       # Encender la cola
                    sleep(0.3)
                    
                    apagar_todos()
                    efecto_especial.on()  # Encender el efecto especial (GPIO27)
                    sleep(0.3)
                    
                    apagar_todos()
                
                # Apagar todo al final excepto los ojos
                apagar_todos()
            
            # Ciclo principal
            while True:
                try:
                    nadar()  # Ejecutar el efecto de "nadar"
                    sleep(1)  # Pausa antes de repetir
                except KeyboardInterrupt:
                    apagar_todos()  # Apagar todos los LEDs si se interrumpte el programa
                    ojos.off()      # Apagar los ojos también
                    break


- Evidencias en fotos:
  
![Imagen de WhatsApp 2025-03-20 a las 08 30 17_445bb20e](https://github.com/user-attachments/assets/1555db96-f459-4d00-ae20-439ac7af57a6)
![Imagen de WhatsApp 2025-03-20 a las 08 30 17_4a56e8b2](https://github.com/user-attachments/assets/88ee72f6-b5b4-491c-956a-8fa9da48f879)


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
