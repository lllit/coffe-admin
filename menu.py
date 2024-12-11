
class ItemMenu:
    def __init__(self, nombre, precio, cantidad=1):

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.precio * self.cantidad
    

class BebidasCalientes(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)
        self.tipo ="Bebidas Calientes"

class BebidasFrias(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)
        self.tipo = "Bebidas Frias"

class Reposteria(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)
        self.tipo = "Reposteria"

class Bocadillos(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)
        self.tipo = "Bocadillos"

class Complementos(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)
        self.tipo = "Complementos"

class Desayunos(ItemMenu):
    def __init__(self, nombre, precio, cantidad=1):
        super().__init__(nombre, precio, cantidad)
        self.tipo = "Desayunos"



class Menu:
    def __init__(self):
        self.bebidas_calientes = []
        self.bebidas_frias = []
        self.reposteria = []
        self.bocadillos = []
        self.complementos = []
        self.desayunos = []

    def agregar_bebidas_calientes(self, nombre, precio):
        bebida_caliente = BebidasCalientes(nombre, precio)
        self.bebidas_calientes.append(bebida_caliente)
        return bebida_caliente
    
    def agregar_bebidas_frias(self, nombre, precio):
        bebida_frias = BebidasFrias(nombre, precio)
        self.bebidas_frias.append(bebida_frias)
        return bebida_frias
    
    def agregar_reposteria(self, nombre, precio):
        reposteria = Reposteria(nombre, precio)
        self.reposteria.append(reposteria)
        return reposteria
    
    def agregar_bocadillos(self, nombre, precio):
        bocadillos = Bocadillos(nombre, precio)
        self.bocadillos.append(bocadillos)
        return bocadillos
    
    def agregar_complementos(self, nombre, precio):
        complementos = Complementos(nombre, precio)
        self.complementos.append(complementos)
        return complementos
    
    def agregar_desayuno(self, nombre, precio):
        desayunos = Desayunos(nombre, precio)
        self.desayunos.append(desayunos)
        return desayunos
    


    def eliminar_item(self, tipo, nombre):
        
        if tipo == "Bebidas Calientes":
            items = self.bebidas_calientes
        elif tipo == "Bebidas Frias":
            items = self.bebidas_frias
        elif tipo == "Reposteria":
            items = self.reposteria
        elif tipo == "Bocadillos":
            items = self.bocadillos
        elif tipo == "Complementos":
            items = self.complementos
        elif tipo == "Desayunos":
            items = self.desayunos
        
        else:
            return False
        

        for item in items[:]:
            if item.nombre == nombre:
                items.remove(item)
                return True
        return False
    

    def eliminar_bebida_caliente(self,nombre):
        return self.eliminar_item("Bebidas Calientes", nombre)

    def eliminar_bebida_fria(self,nombre):
        return self.eliminar_item("Bebidas Frias", nombre)

    def eliminar_reposteria(self,nombre):
        return self.eliminar_item("Reposteria", nombre)

    def eliminar_bocadillo(self,nombre):
        return self.eliminar_item("Bocadillos", nombre)

    def eliminar_complemento(self,nombre):
        return self.eliminar_item("Complementos", nombre)

    def eliminar_desayuno(self,nombre):
        return self.eliminar_item("Desayunos", nombre)
    

    def obtener_item(self, tipo, nombre):
        
        if tipo == "Bebidas Calientes":
            items = self.bebidas_calientes
        elif tipo == "Bebidas Frias":
            items = self.bebidas_frias
        elif tipo == "Reposteria":
            items = self.reposteria
        elif tipo == "Bocadillos":
            items = self.bocadillos
        elif tipo == "Complementos":
            items = self.complementos
        elif tipo == "Desayunos":
            items = self.desayunos
        
        else:
            return None
        

        for item in items[:]:
            if item.nombre == nombre:
                return item
        return None

