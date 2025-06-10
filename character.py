from general import General, GENERAL_DICT

class Character:
    def __init__(self, general_name: str):
        if general_name not in GENERAL_DICT:
            raise ValueError(f"武将 {general_name} 不存在")
        self.general = GENERAL_DICT[general_name]

    def get_attributes(self):
        """获取武将的属性"""
        return {
            "name": self.general.name,
            "force": self.general.force,
            "strength": self.general.strength,
            "intelligence": self.general.intelligence,
            "leadership": self.general.leadership,
            "agility": self.general.agility
        }

    def __repr__(self):
        return f"Character({self.general})"