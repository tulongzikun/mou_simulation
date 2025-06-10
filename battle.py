class BattleSystem:
    def execute_round(self, general: General):
        # 1. 被动技能（无视控制）
        self._trigger_skills(general, SkillType.PASSIVE)
        
        # 2. 指挥技能（无视控制）
        self._trigger_skills(general, SkillType.COMMAND)
        
        # 3. 主动技能（概率判定）
        self._trigger_skills(general, SkillType.ACTIVE)
        
        # 4. 普通攻击（必触发）
        self._trigger_skills(general, SkillType.NORMAL_ATTACK)
        
        # 5. 追击技能（普攻后概率触发）
        self._trigger_skills(general, SkillType.PURSUIT)

    def _trigger_skills(self, general: General, skill_type: SkillType):
        for skill in general.equipped_skills:
            if skill.type == skill_type and skill.can_trigger():
                print(f"{general.name} 触发 {skill.name}：{skill.description}")