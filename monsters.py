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
        return roll(f'{self.level}d6+{self.level + 1}')

    def calc_armor_class(self):
        return 10 - random.randint(0, self.level + 2)

    def __str__(self):
        return f'{self.obj_name}(level={self.level}, hp={self.hp}, ac={self.ac})'

    def __repr__(self):
        return f'{self.obj_name}(level={self.level}, hp={self.hp}, ac={self.ac})'

class Skeleton(Monster):

    def __init__(self, name='Skeleton', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = 'Skeleton'

    def calc_hit_points(self):
        return roll(f'2d6+{self.level + 2}')

class Goblin(Monster):

    def __init__(self, name='goblin', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = 'Goblin'

    def calc_hit_points(self):
        return roll(f'{self.level}d6', find_max=True)

class Slime(Monster):

    def __init__(self, name='Slime', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = level +4
        self.obj_name = 'Slime'

class Mage(Monster):

    def __init__(self, name='Mage', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points() 
        self.obj_name = name


class Dragon(Monster):

    def __init__(self, name='Dragon', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.hp = self.calc_hit_points()
        self.obj_name = name
    
    def calc_hit_points(self):
        return roll(f'{self.level}d8+{self.level + 100}')
    
    def calc_armor_class(self):
        return 20 - random.randint(0, self.level)
    
MONSTERS = [
    {'name': 'skeleton', 'levels': '01234', 'obj_name': 'Skeleton', 'obj': Skeleton},
    {'name': 'goblin', 'levels': '01', 'obj_name': 'Goblin', 'obj': Goblin},
    {'name': 'slime', 'levels': '0123456789', 'obj_name': 'Slime', 'obj': Slime},
    {'name': 'mage', 'levels': '34567', 'obj_name': 'Mage', 'obj': Mage},
    {'name': 'dragon', 'levels': '789', 'obj_name': 'Dragon', 'obj': Dragon},
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

print(summon_monsters(level=9, count=2, name= None))

#print(summon_monsters(level=2, count=2, name= None))
#^^^^^^^^^^ to summon the monsters. pick level and count
