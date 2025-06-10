from enum import Enum
import re

class SkillType(Enum):
    PASSIVE = "被动"  # 回合开始前触发，无视控制
    COMMAND = "指挥"  # 回合开始前触发，无视控制
    ACTIVE = "主动"  # 回合中概率判定
    NORMAL_ATTACK = "普攻"  # 必触发
    PURSUIT = "追击"  # 普攻后概率触发

class Skill:
    def __init__(self, skill_id: str, name: str, skill_type: SkillType, 
                 power: int, trigger_condition: str = "", description: str = ""):
        self.id = skill_id
        self.name = name
        self.type = skill_type
        self.power = power  # 技能威力值
        self.trigger_condition = trigger_condition  # 触发条件（如“受到伤害后”）
        self.description = description

    def can_trigger(self, round_num: int) -> bool:
        """判定技能是否触发（主动/追击类需概率判定）"""
        if self.type in [SkillType.PASSIVE, SkillType.COMMAND, SkillType.NORMAL_ATTACK]:
            return True  # 被动/指挥/普攻必触发
        # 主动/追击需概率判定（此处简化为50%概率）
        return random.random() < 0.5