import socket
import threading

class ClienteMensajeria:
    def __init__(self):
        self.host = "127.0.0.1"
        self.puerto = 5050
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.connect((self.host, self.puerto))
        thread_recepcion = threading.Thread(target=self.recibir_mensajes)
        thread_recepcion.start()

    def enviar_mensaje(self, mensaje):
        self.cliente.send(mensaje.encode("utf-8"))

    def recibir_mensajes(self):
        while True:
            try:
                mensaje = self.cliente.recv(1024).decode("utf-8")
                if mensaje:
                    print("Mensaje recibido:", mensaje)
            except Exception as e:
                print(f"Error al recibir mensaje: {e}")
                break

if __name__ == "__main__":
    cliente = ClienteMensajeria()
    while True:
        mensaje = input("Ingrese el mensaje a enviar (Escriba 'exit' para salir): ")
        if mensaje.lower() == "exit":
            break
        cliente.enviar_mensaje(mensaje)
