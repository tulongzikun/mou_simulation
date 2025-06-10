from skill import Skill, SkillType, SKILL_DICT
import csv

class General:
    def __init__(self, name: str, force: str,
                 strength: float, strength_growth: float, 
                 intelligence: float, intelligence_growth: float,
                 leadership: float, leadership_growth: float,
                 agility: float, agility_growth: float,
                 skill: str, type: str):
        self.id = 0
        self.name = name
        self.type = type
        self.force = force  # 势力（魏/蜀/吴）
        self._strength = float(strength)  # 武力 → 影响兵刃伤害
        self._strength_growth = float(strength_growth)
        self._intelligence = float(intelligence)  # 智力 → 影响谋略伤害
        self._intelligence_growth = float(intelligence_growth)
        self._leadership = float(leadership)
        self._leadership_growth =  float(leadership_growth)
        self._agility = float(agility)
        self._agility_growth = float(agility_growth)
        self.level = 50 # 初始等级（可根据实际情况调整）
        
        # 存储技能/战法ID（实际对象通过load_data关联）
        self.skill = SKILL_DICT[skill]

    @property
    def strength(self) -> float:
        """武力属性"""
        return self._strength + self._strength_growth * (self.level - 5)
    
    @property
    def intelligence(self) -> float:
        """智力属性"""
        return self._intelligence + self._intelligence_growth * (self.level - 5)
    
    @property
    def leadership(self) -> float:
        """统率属性"""
        return self._leadership + self._leadership_growth * (self.level - 5)    
    
    @property
    def agility(self) -> float:
        """敏捷属性"""
        return self._agility + self._agility_growth * (self.level - 5)
    
    def __repr__(self):
        return f"{self.name}({self.force}) - 力量: {self.strength}, 智力: {self.intelligence}, 统率: {self.leadership}, 敏捷: {self.agility}"
    
GENERAL_DICT = {}
    
def read_from_file(path="./data/general.txt"):
    with open(path, encoding="utf8") as f:
        reader = csv.reader(f)
        for row in reader:
            GENERAL_DICT[row[0]] = General(*row)

read_from_file()

if __name__ == "__main__":
    print(GENERAL_DICT)