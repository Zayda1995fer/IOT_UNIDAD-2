from machine import Pin, PWM
from time import sleep

# Configurar el buzzer en el pin GPIO 27
BUZZER_PIN = 27
buzzer = PWM(Pin(BUZZER_PIN))

# Función para reproducir un tono a una frecuencia específica
def tono(frecuencia, duracion):
    buzzer.freq(frecuencia)  # Establece la frecuencia del tono
    buzzer.duty(512)  # Activa el buzzer con un 50% de ciclo de trabajo
    sleep(duracion)  # Mantiene el tono durante el tiempo especificado
    buzzer.duty(0)  # Apaga el buzzer

# Reproducir una melodía sencilla
notas = [
    (440, 0.5),  # La (A4)
    (523, 0.5),  # Do (C5)
    (659, 0.5),  # Mi (E5)
    (784, 0.5),  # Sol (G5)
]

for frecuencia, duracion in notas:
    tono(frecuencia, duracion)
    sleep(0.2)  # Pequeña pausa entre notas

# Detener el PWM al final
buzzer.deinit()
