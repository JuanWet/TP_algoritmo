class Notificacion:
    def _init_(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

class ColaNotificaciones:
    def _init_(self):
        self.notificaciones = []

    def agregar_notificacion(self, notificacion):
        self.notificaciones.append(notificacion)

    def obtener_notificacion(self):
        if self.notificaciones:
            return self.notificaciones.pop(0)
        else:
            return None

cola = ColaNotificaciones()

notificacion1 = Notificacion("09:30", "Facebook", "Tienes una nueva solicitud de amistad")
cola.agregar_notificacion(notificacion1)

notificacion2 = Notificacion("10:15", "Twitter", "Nuevo mensaje directo")
cola.agregar_notificacion(notificacion2)

primera_notificacion = cola.obtener_notificacion()
if primera_notificacion:
    print("Hora:", primera_notificacion.hora)
    print("Aplicación:", primera_notificacion.aplicacion)
    print("Mensaje:", primera_notificacion.mensaje)
else:
    print("No hay notificaciones en la cola.")

def eliminar_notificaciones_facebook(cola):
    cola_sin_facebook = [notif for notif in cola if notif["app"] != "Facebook"]
    return cola_sin_facebook

def mostrar_notificaciones_twitter_python(cola):
    notificaciones_python = [notif for notif in cola if notif["app"] == "Twitter" and "Python" in notif["mensaje"]]
    for notif in notificaciones_python:
        print(notif)

def contar_notificaciones_entre_horas(cola):
    pila_temporal = []
    contador = 0
    for notif in cola:
        hora = notif["hora"]
        if hora >= "11:43" and hora <= "15:57":
            pila_temporal.append(notif)
            contador += 1
    return contador, pila_temporal
