from menu import ItemMenu

class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.items = {
            "bebidas_calientes": [],
            "bebidas_frias": [],
            "reposteria": [],
            "bocadillos": [],
            "complementos": [],
            "desayunos": []
        }
        self.estado = "Pendiente"

    def agregar_item(self, item):

        if isinstance(item, ItemMenu):

            if item.tipo == "Bebidas Calientes":
                self.items["bebidas_calientes"].append(item)

            elif item.tipo == "Bebidas Frias":
                self.items["bebidas_frias"].append(item)

            elif item.tipo == "Reposteria":
                self.items["reposteria"].append(item)

            elif item.tipo == "Bocadillos":
                self.items["bocadillos"].append(item)

            elif item.tipo == "Complementos":
                self.items["complementos"].append(item)

            elif item.tipo == "Desayunos":
                self.items["desayunos"].append(item)

# Esta en dolares
    def calcular_total(self):
        total = 0
        for categoria in self.items.values():
            for item in categoria:
                total += item.calcular_subtotal()
            
        return round(total,2)
    
    def cambiar_estado(self,nuevo_estado):
        estados_validos = ["Pendiente", "En Preparación", "Listo", "Entregado"]

        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            return True

        return False
    
    def obtener_resumen(self):
        resumen = []
        for categoria, items in self.items.items():
            if items:
                resumen.append(f"\n{categoria.replace('_', ' ').title()}")
                for item in items:
                    resumen.append(f"- {item.nombre} x{item.cantidad}: ${item.calcular_subtotal():.2f}")
                
        resumen.append(f"\nTotal: ${self.calcular_total():.2f}")

        return "\n".join(resumen)
                
