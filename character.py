from general import General, GENERAL_DICT

class Character:
    def __init__(self, general_name: str):
        if general_name not in GENERAL_DICT:
            raise ValueError(f"武将 {general_name} 不存在")
        self.general = GENERAL_DICT[general_name]
        self.level = 50
        self.position = 0 # 0 前排 1 后排
        self.init_attributes()

    def init_attributes(self):
        self.max_human_power = 10000
        self.strength = self.general.strength
        self.intelligence = self.general.intelligence
        self.leadership = self.general.leadership
        self.agility = self.general.agility

        # add 50 default the max one
        max_attribute = max(self.strength, self.intelligence, self.leadership, self.agility)
        if self.strength == max_attribute:
            self.strength += 50
        elif self.intelligence == max_attribute:
            self.intelligence += 50
        elif self.leadership == max_attribute:
            self.leadership += 50
        elif self.agility == max_attribute:
            self.agility += 50

        self.current_human_power = self.max_human_power

        self._damage_buff = 0
        self._ap_damage_buff = 0
        self._hurt_buff = 0
        self._ap_hurt_buff = 0
        


