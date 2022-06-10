from equipment import Equipment


class Shopkeeper:
    def __init__(self, x, y):
        self.position = (x, y)
        self.equipment = Equipment(6)
        self.equipment.add_new_sword("resources/map1/assets/weapons/stone_sword.png", 20, 10)
        self.equipment.add_new_sword("resources/map1/assets/weapons/golden_sword.png", 40, 20)
        self.equipment.add_new_sword("resources/map1/assets/weapons/iron_sword.png", 50, 40)
        self.equipment.add_new_sword("resources/map1/assets/weapons/diamond_sword.png", 100, 80)
        self.equipment.add_new_sword("resources/map1/assets/weapons/netherite_sword.png", 120, 160)

    def get_position(self):
        return self.position

    def get_equipment(self):
        return self.equipment.get_items()

    def sell_item(self, index):
        return self.equipment.get_items()[index]
