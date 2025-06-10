from character import Character

FORMATION_NAMES = ["一字阵", "箕形阵"]

class Team:
    def __init__(self):
        self.c1: Character = None
        self.c2: Character = None
        self.c3: Character = None

    def add_characters(self, c1: Character, c2: Character, c3: Character):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def set_formation(self, formation_name=FORMATION_NAMES[0]):
        if formation_name not in FORMATION_NAMES:
            raise NotImplementedError
        # 一字阵
        if formation_name == FORMATION_NAMES[0]:
            self.c1.position = 0
            self.c1._hurt_buff -= 8 
            self.c2.position = 0
            self.c2._hurt_buff -= 8
            self.c3.position = 0
            self.c3._hurt_buff -= 8
        # 箕形阵
        elif formation_name == FORMATION_NAMES[1]:
            self.c1.position = 0
            self.c1._hurt_buff -= 6
            self.c2.position = 1
            self.c2._damage_buff += 12
            self.c3.position = 1
            self.c3._damage_buff += 12

