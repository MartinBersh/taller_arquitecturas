import socket
import threading


class ServidorMensajeria:
    def __init__(self):
        self.host = "127.0.0.1"
        self.puerto = 5050
        self.clientes = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.puerto))

    def iniciar_servidor(self):
        self.server.listen()
        print(f"Servidor de mensajería iniciado en {self.host}:{self.puerto}")
        while True:
            cliente_socket, cliente_direccion = self.server.accept()
            thread_cliente = threading.Thread(target=self.atender_cliente, args=(cliente_socket, cliente_direccion))
            thread_cliente.start()

    def atender_cliente(self, cliente_socket, cliente_direccion):
        print(f"Nuevo cliente conectado: {cliente_direccion}")
        self.clientes.append(cliente_socket)
        while True:
            try:
                mensaje = cliente_socket.recv(1024).decode("utf-8")
                if mensaje:
                    print(f"Mensaje recibido de {cliente_direccion}: {mensaje}")
                    self.retransmitir_mensaje(mensaje, cliente_socket)
            except Exception as e:
                print(f"Error al recibir mensaje de {cliente_direccion}: {e}")
                break
        cliente_socket.close()
        self.clientes.remove(cliente_socket)

    def retransmitir_mensaje(self, mensaje, emisor_socket):
        for cliente in self.clientes:
            if cliente != emisor_socket:
                try:
                    cliente.send(mensaje.encode("utf-8"))
                except Exception as e:
                    print(f"Error al retransmitir mensaje: {e}")
        print("Mensaje retransmitido a todos los clientes")


if __name__ == "__main__":
    servidor = ServidorMensajeria()
    servidor.iniciar_servidor()
