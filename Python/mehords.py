class Calculator:
    def calculate_total(self, price, quantity, tax_rate):
        subtotal = price * quantity
        total = subtotal + (subtotal * tax_rate)
        return total

calc = Calculator()
total_price = calc.calculate_total(100, 2, 0.1)


# REFACTOING MEHORDS

class Calculator:
    def calculate_total(self, price=0, quantity=0, tax_rate=0):
        subtotal = price * quantity
        total = subtotal + (subtotal * tax_rate)
        return total

calc = Calculator()
total_price = calc.calculate_total(price=100, quantity=2, tax_rate=0.1)
