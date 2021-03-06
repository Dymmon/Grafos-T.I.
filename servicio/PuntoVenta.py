from utils import debug_print

ARCHIVO = "PuntosVenta"


class PuntoVenta:
    def __init__(self, id, coordenadas, productos=None):
        debug_print(ARCHIVO, "__init__", str(
            {"id": id, "coordenadas": coordenadas, "productos": productos}))
        self.id = id
        self.coordenadas = coordenadas
        self.productos = productos

    @staticmethod
    def from_json(json):
        debug_print(ARCHIVO, "__init__", json)
        return PuntoVenta(json["id"], (json["coordenadas"]["x"], json["coordenadas"]["y"]), json["productos"])

    def to_dict(self):
        debug_print(ARCHIVO, "to_dict")
        return {
            "id": self.id,
            "esCentroDistribucion": False,
            "coordenadas": {
                "x": self.coordenadas[0],
                "y": self.coordenadas[0],
            },
            "productos": self.productos
        }

    @staticmethod
    def lista_to_dict(puntos):
        debug_print(ARCHIVO, "lista_to_dict", {"puntos": puntos})
        lista = []
        for punto in puntos:
            lista.append(punto.to_dict())
        return lista

    @staticmethod
    def get_by_id(id, puntos):
        debug_print(ARCHIVO, "get_by_id", {"id": id, "puntos": puntos})
        for punto in puntos:
            if (punto.id == id):
                return punto
        return None
