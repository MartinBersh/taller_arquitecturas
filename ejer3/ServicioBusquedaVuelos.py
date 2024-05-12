
class ServicioBusquedaVuelos:
    def buscar_vuelos(self, origen, destino, fecha):

        vuelos_disponibles = [
            {"numero_vuelo": "AB123", "origen": "MAD", "destino": "BCN", "fecha": "2024-05-15", "hora": "08:00", "precio": 150.00},
            {"numero_vuelo": "CD456", "origen": "BCN", "destino": "MAD", "fecha": "2024-05-15", "hora": "10:00", "precio": 120.00},
        ]
        return vuelos_disponibles
