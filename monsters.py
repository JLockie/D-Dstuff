from d20 import roll
import random

class Monster:

    def __init__(self, name=None, level=0, hp=None, ac=None):
        self.name = name.upper() if name else 'UNKNOWN MONSTER'
        self.level = level
        self.hp = hp if hp else self.calc_hit_points()
        self.ac = ac if ac else self.calc_armor_class()
        self.obj_name = 'Monster'
        self.spells = []

    def calc_hit_points(self):
        return roll(f'{self.level}d6+{self.level + 10}')

    def calc_armor_class(self):
        return random.randint(self.level, 20)

    def __str__(self):
        return f'{self.obj_name}(level={self.level}, hp={self.hp}, ac={self.ac})'

    def __repr__(self):
        return f'{self.obj_name}(level={self.level}, hp={self.hp}, ac={self.ac})'

class Skeleton(Monster):

    def __init__(self, name='Skeleton', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Skeleton'

class Goblin(Monster):

    def __init__(self, name='goblin', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Goblin'

class Slime(Monster):

    def __init__(self, name='Slime', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = 'Slime'

class Mage(Monster):

    def __init__(self, name='Mage', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac) 
        self.obj_name = name

class Spirit(Monster):

    def __init__(self, name="Spirit", level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = name

class Giant(Monster):
    
    def __init__(self, name="Giant", level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = name
    
    def calc_hit_points(self):
        return roll(f'{self.level}d8+{self.level + 50}')

class Dragon(Monster):

    def __init__(self, name='Dragon', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = name
    
    def calc_hit_points(self):
        return roll(f'{self.level}d8+{self.level + 101}')
    
    def calc_armor_class(self):
        return 23 - random.randint(0, 7)
    
MONSTERS = [
    {'name': 'skeleton', 'levels': '1234', 'obj_name': 'Skeleton', 'obj': Skeleton},
    {'name': 'goblin', 'levels': '1234', 'obj_name': 'Goblin', 'obj': Goblin},
    {'name': 'slime', 'levels': '1234', 'obj_name': 'Slime', 'obj': Slime},
    {'name': 'mage', 'levels': '5678', 'obj_name': 'Mage', 'obj': Mage},
    {'name': 'spirit', 'levels': '5678', 'obj_name': 'Spirit', 'obj': Spirit},
    {'name': 'giant', 'levels': '5678', 'obj_name': 'Giant', 'obj': Giant},
    {'name': 'dragon', 'levels': '9', 'obj_name': 'Dragon', 'obj': Dragon},
]

def summon_monsters(level=0, count=1, name=None):
    eligible = None
    if name:
        for m in MONSTERS:
            if m.get('name') == name:
                eligible = [m]
                break
        if not eligible:
            eligible = [m for m in MONSTERS if '0' in m.get('levels', '0')]
    else:
        eligible = [m for m in MONSTERS if str(level) in m.get('levels', '0')]
    monster = random.choice(eligible)
    summoned = [monster.get('obj', Slime)(name=monster.get('obj_name', 'Slime'), level=level) for _ in range(count)]
    return summoned


#test random summons:
#print(summon_monsters(level=4, count=2, name= None))
#print(summon_monsters(level=8, count=2, name= None))
#print(summon_monsters(level=9, count=2, name= None))
#print(summon_monsters(level=random.randint(1,9), count=random.randint(1,3), name= None))
