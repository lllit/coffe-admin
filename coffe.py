from menu import Menu
from pedido import Pedido

class Coffe:
    def __init__(self):
        self.mesas = []
        self.clientes = []
        self.pedidos_activos = []
        self.menu = Menu()
        self._inicializar_menu()

    def _inicializar_menu(self):
        """
        Bebidas Calientes
        """
        self.menu.agregar_bebidas_calientes("Cafe de Grano - Colombiano Supremo", 2800.00)
        self.menu.agregar_bebidas_calientes("Cafe de Grano - Etiopía Sidamo", 3200.00)
        self.menu.agregar_bebidas_calientes("Cafe de Grano - Brasil Santos", 2800.00)
        self.menu.agregar_bebidas_calientes("Cafe de Grano - Perú Orgánico", 3000.00)
        self.menu.agregar_bebidas_calientes("Cafe de Grano - Costa Rica Tarrazú", 3200.00)

        """
        Bebidas Frias
        """


        self.menu.agregar_bebidas_frias("Jugo de naranja 500ml",2000.00)
        self.menu.agregar_bebidas_frias("Jugo de manzana 500ml",2000.00)
        self.menu.agregar_bebidas_frias("Batido de frutas 500ml",3500.00)
        self.menu.agregar_bebidas_frias("Agua mineral 500ml",1500.00)
        self.menu.agregar_bebidas_frias("Refresco 500ml",2500.00)




        """
        Reposteria
        """

        self.menu.agregar_reposteria("Croissant Veg.", 2500.00)
        self.menu.agregar_reposteria("Muffin Veg.", 2000.00)
        self.menu.agregar_reposteria("Brownie Veg.", 2500.00)
        self.menu.agregar_reposteria("Tarta de manzana Veg.", 3000.00)
        self.menu.agregar_reposteria("Galletas caseras Veg.", 2000.00)


        """
        Bocadillos
        """

        self.menu.agregar_bocadillos("Sándwich de verduras picante", 4000.00)
        self.menu.agregar_bocadillos("Sándwich de tofu", 4500.00)
        self.menu.agregar_bocadillos("Ensalada Mix Veg.", 5000.00)
        self.menu.agregar_bocadillos("Tostadas con Palta.", 4000.00)
        self.menu.agregar_bocadillos("Burger Tofu Seitan.", 5500.00)

        """
        Complementos
        """
        self.menu.agregar_complementos("Palta",2500.00)
        self.menu.agregar_complementos("Queso Veg.",3000.00)
        self.menu.agregar_complementos("Chorizo Veg.",2500.00)
        self.menu.agregar_complementos("Tomate",1500.00)
        self.menu.agregar_complementos("Lechuga",1500.00)

        """
        Desayunos
        """

        self.menu.agregar_desayuno("Desayuno clásico (café simple o té orgánico, jugo del día y tostadas clásicas)", 8500.00)
        self.menu.agregar_desayuno("Desayuno de avocado (café simple o té orgánico, jugo del día y tostón de aguacate)", 12900.00)

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

        return f"Mesa {mesa.numero} (capacidad: {mesa.tamaño}) agregada exitosamente"
    

    def asignar_cliente_mesa(self, cliente, numero_mesa):
        mesa = self.buscar_mesa(numero_mesa)

        if not mesa:
            return "Mesa no encontrada"
        
        if mesa.ocupada:
            return "Mesa no disponible"
        
        if cliente.tamaño_grupo > mesa.tamaño:
            return f"Grupo demasiado grande para la mesa (capacidad maxima: {mesa.tamaño})"
        
        if mesa.asignar_cliente(cliente):
            self.clientes.append(cliente)
            return f"Cliente {cliente.id} asignado a mesa {numero_mesa}"
        
        return "No se pudo asignar el cliente a la mesa"
    

    def buscar_mesa(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa:
                return mesa
        
        return None
    
    def crear_pedido(self, numero_mesa):
        mesa= self.buscar_mesa(numero_mesa)

        if mesa and mesa.ocupada:
            pedido = Pedido(mesa)
            self.pedidos_activos.append(pedido)
            mesa.pedido_actual = pedido
            mesa.cliente.asignar_pedido(pedido)
            return pedido
        return None
    

    def liberar_mesa(self, numero_mesa):
        mesa= self.buscar_mesa(numero_mesa)
        if mesa:
            cliente = mesa.cliente
            if cliente:
                cliente.limpiar_pedido()
                if cliente in self.clientes:
                    self.clientes.remove(cliente)
                if mesa.pedido_actual in self.pedidos_activos:
                    self.pedidos_activos.remove(mesa.pedido_actual)
            mesa.liberar()
            return f"Mesa {numero_mesa} liberada"
        return "Mesa no encontrada"
    
    def obtener_item_menu(self, tipo, nombre):
        return self.menu.obtener_item(tipo, nombre)

