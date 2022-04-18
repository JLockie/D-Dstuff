from d20 import roll
import random

class Boss:

    def __init__(self, name=None, level=0, hp=None, ac=None):
        self.name = name.upper() if name else 'UNKNOWN BOSS'
        self.level = level
        self.hp = hp if hp else self.calc_hit_points()
        self.ac = ac if ac else self.calc_armor_class()
        self.obj_name = 'Boss'
        self.spells = []

    def calc_hit_points(self):
        return roll(f'{self.level}d6+{self.level + 10}')

    def calc_armor_class(self):
        return random.randint(self.level, 20)

    def __str__(self):
        return f'{self.obj_name}(level={self.level}, hp={self.hp}, ac={self.ac})'

    def __repr__(self):
        return f'{self.obj_name}(level={self.level}, hp={self.hp}, ac={self.ac})'

class SkeletonKnight(Boss):

    def __init__(self, name='Skeleton Knight', level=0, hp=None, ac=None):
        Boss.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Skeleton Knight'

class Hobgoblin(Boss):

    def __init__(self, name='Hobgoblin', level=0, hp=None, ac=None):
        Boss.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Hobgoblin'

class GelatinousCube(Boss):

    def __init__(self, name='Gelatinous Cube', level=0, hp=None, ac=None):
        Boss.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Gelatinous Cube'
    
    def calc_armor_class(self):
        return random.randint(5, 10)

class Archmage(Boss):

    def __init__(self, name='Archmage', level=0, hp=None, ac=None):
        Boss.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Archmage'

class Lich(Boss):

    def __init__(self, name='Lich', level=0, hp=None, ac=None):
        Boss.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Lich'

class StormGiant(Boss):

    def __init__(self, name='Storm Giant', level=0, hp=None, ac=None):
        Boss.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Storm Giant'
    
    def calc_hit_points(self):
        return roll(f'{self.level}d8+{self.level + 75}')

class Dragon(Boss):

    def __init__(self, name='Dragon', level=0, hp=None, ac=None):
        Boss.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Dragon'
    
    def calc_hit_points(self):
        return roll(f'{self.level}d8+{self.level + 101}')
    
    def calc_armor_class(self):
        return 23 - random.randint(0, 7)

BOSS = [
    {'name': 'Skeleton Knight', 'levels': '3456', 'obj_name': 'Skeleton', 'obj': SkeletonKnight},
    {'name': 'Hobgoblin', 'levels': '3456', 'obj_name': 'Goblin', 'obj': Hobgoblin},
    {'name': 'Gelantinous Cube', 'levels': '3456', 'obj_name': 'Slime', 'obj': GelatinousCube},
    {'name': 'Archmage', 'levels': '5678', 'obj_name': 'Mage', 'obj': Archmage},
    {'name': 'Lich', 'levels': '5678', 'obj_name': 'Spirit', 'obj': Lich},
    {'name': 'Storm Giant', 'levels': '5678', 'obj_name': 'Giant', 'obj': StormGiant},
    {'name': 'Dragon', 'levels': '9', 'obj_name': 'Dragon', 'obj': Dragon},
]

def summon_boss(level=0, count=1, name=None):
    eligible = None
    if name:
        for m in BOSS:
            if m.get('name') == name:
                eligible = [m]
                break
        if not eligible:
            eligible = [m for m in BOSS if '0' in m.get('levels', '0')]
    else:
        eligible = [m for m in BOSS if str(level) in m.get('levels', '0')]
    boss = random.choice(eligible)
    summoned = [boss.get('obj', GelatinousCube)(name=boss.get('obj_name', 'Gelantinous Cube'), level=level) for _ in range(count)]
    return summoned

#test random summons:
#print(summon_boss(level=4, count=3, name= None))
#print(summon_boss(level=8, count=2, name= None))
#print(summon_boss(level=9, count=5, name= None))
#print(summon_boss(level=random.randint(1,9), count=random.randint(1,3), name= None))
