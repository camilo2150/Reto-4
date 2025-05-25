class MenuItem:
    def _init_(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price


# Subclases
class MainCourse(MenuItem):
    pass


class Beverage(MenuItem):
    pass


class Dessert(MenuItem):
    pass


# Clase para manejar una orden
class Order:
    def _init_(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total_price(self):
        total = 0
        has_main_course = any(isinstance(item, MainCourse) for item in self.items)
        for item in self.items:
            if isinstance(item, Beverage) and has_main_course:
                total += item.get_price() * 0.9  # Descuento del 10%
            else:
                total += item.get_price()
        return total

    def show_order(self):
        print("\nPedido actual:")
        for item in self.items:
            print(f"- {item.get_name()} : ${item.get_price():.2f}")
        print(f"Total hasta ahora: ${self.calculate_total_price():.2f}\n")


# Clase para procesar pagos
class Payment:
    def _init_(self, order, payment_method):
        self.order = order
        self.payment_method = payment_method

    def process_payment(self):
        total_price = self.order.calculate_total_price()
        print(f"\nPago de ${total_price:.2f} realizado con {self.payment_method}. ¡Gracias por tu compra!\n")


# Función para mostrar menú y recibir pedidos
def show_menu():
    print("\n--- MENÚ ---")
    print("1. Hamburguesa ($12.00)")
    print("2. Pizza ($15.00)")
    print("3. Refresco ($3.00)")
    print("4. Agua ($2.00)")
    print("5. Helado ($5.00)")
    print("6. Pastel ($6.00)")
    print("7. Ver pedido")
    print("8. Pagar")
    print("9. Salir")


if _name_ == "_main_":
    order = Order()

    while True:
        show_menu()
        choice = input("Elige una opción: ")

        if choice == "1":
            order.add_item(MainCourse("Hamburguesa", 12.00))
        elif choice == "2":
            order.add_item(MainCourse("Pizza", 15.00))
        elif choice == "3":
            order.add_item(Beverage("Refresco", 3.00))
        elif choice == "4":
            order.add_item(Beverage("Agua", 2.00))
        elif choice == "5":
            order.add_item(Dessert("Helado", 5.00))
        elif choice == "6":
            order.add_item(Dessert("Pastel", 6.00))
        elif choice == "7":
            order.show_order()
        elif choice == "8":
            if len(order.items) == 0:
                print("\nNo has agregado productos al pedido.\n")
            else:
                metodo = input("Método de pago (Ej: Tarjeta / Efectivo): ")
                pago = Payment(order, metodo)
                pago.process_payment()
                break
        elif choice == "9":
            print("\nGracias por visitarnos. ¡Hasta luego!\n")
            break
        else:
            print("\nOpción inválida, intenta de nuevo.\n")
