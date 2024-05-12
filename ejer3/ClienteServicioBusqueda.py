from ejer3.ServicioBusquedaVuelos import ServicioBusquedaVuelos


class ClienteServicioBusqueda:
    def __init__(self):
        self.servicio_busqueda = ServicioBusquedaVuelos()

    def buscar_vuelos(self, origen, destino, fecha):
        return self.servicio_busqueda.buscar_vuelos(origen, destino, fecha)

if __name__ == "__main__":
    cliente_busqueda = ClienteServicioBusqueda()
    vuelos = cliente_busqueda.buscar_vuelos("MAD", "BCN", "2024-05-15")
    if vuelos:
        print("Vuelos disponibles:")
        for vuelo in vuelos:
            print(vuelo)
