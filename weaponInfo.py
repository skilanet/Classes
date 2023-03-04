class GeneralInfo:
    def __init__(self, name, weigth, damage, size, type, price):
        self.weight = weigth
        self.damage = damage
        self.size = size
        self.type = type
        self.name = name
        self.price = price
    def __str__(self):
        return 'weapon'


class LongDistWeapon(GeneralInfo):
    def __init__(self, name, weigth, damage, size, type, dist, cart_number, accuracy, price):
        super().__init__(name, weigth, damage, size, type, price)
        self.dist = dist
        self.cart_number = cart_number
        self.accuracy = accuracy
        self.price = price

    def __str__(self):
        out = f'Long distance {super().__str__()}:\n' + f'  Name: {self.name}\n' + f'  Type: {self.type}\n' \
              + f'  Weigth: {self.weight} kilos\n' + f'  Damage: {self.damage} hp\n' \
              + f'  Size: {self.size}\n' + f'  Distance: {self.dist} meters\n' \
              + f'  Number of cartrigies: {self.cart_number}\n' + f'  Accuracy:{self.accuracy}\n' + f'  Price: {self.price}$'
        return out


class ShortDistWeapon(GeneralInfo):
    def __init__(self, name, weigth, damage, size, type, price):
        super().__init__(name, weigth, damage, size, type, price)

    def __str__(self):
        out = f'Long distance {super().__str__()}:\n' + f'  Name: {self.name}\n' + f'  Type: {self.type}\n' \
              + f'  Weigth: {self.weight}  kilos\n' + f'  Damage: {self.damage} hp\n' \
              + f'  Size: {self.size}\n' + f'  Price: {self.price}$'
        return out
