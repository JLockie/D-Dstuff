from d20 import roll
import random
from tkinter import*

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
        return roll(f'{self.level}d8+{self.level + 25}')

class Drake(Monster):

    def __init__(self, name='Drake', level=0, hp=None, ac=None):
        Monster.__init__(self, name=name, level=level, hp=hp, ac=ac)
        self.obj_name = name
    
    def calc_hit_points(self):
        return roll(f'{self.level}d8+{self.level + 50}')
    
    def calc_armor_class(self):
        return 20 - random.randint(0, 7)
    
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

MONSTERS = [
    {'name': 'skeleton', 'levels': '1234', 'obj_name': 'Skeleton', 'obj': Skeleton},
    {'name': 'goblin', 'levels': '1234', 'obj_name': 'Goblin', 'obj': Goblin},
    {'name': 'slime', 'levels': '1234', 'obj_name': 'Slime', 'obj': Slime},
    {'name': 'mage', 'levels': '5678', 'obj_name': 'Mage', 'obj': Mage},
    {'name': 'spirit', 'levels': '5678', 'obj_name': 'Spirit', 'obj': Spirit},
    {'name': 'giant', 'levels': '5678', 'obj_name': 'Giant', 'obj': Giant},
    {'name': 'drake', 'levels': '9', 'obj_name': 'Drake', 'obj': Drake},
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

ITEMMODS = ['of Minor Alchemy(Fortify Alchemy 1 12%)','of Alchemy(Fortify Alchemy 2 15%)','of Major Alchemy(Fortify Alchemy 3 17%)','of Eminent Alchemy (Fortify Alchemy 4 20%)','of Extreme Alchemy (Fortify Alchemy 5 22%)','of Peerless Alchemy (Fortify Alchemy 6 25%)',
'of Minor Alteration (Fortify Alteration 1 12%)','of Alteration (Fortify Alteration 2 15%)','of Major Alteration (Fortify Alteration 3 17%)','of Eminent Alteration (Fortify Alteration 4 20%)','of Extreme Alteration (Fortify Alteration 5 22%)','of Peerless Alteration (Fortify  Alteration 6 25%)',
'of Minor Blocking (Fortify Block 1 15%)','of Blocking (Fortify Block 2 20%)','of Major Blocking (Fortify Block 3 25%)','of Eminent Blocking (Fortify Block 4 30%)','of Extreme Blocking (Fortify Block 5 35%)','of Peerless Blocking (Fortify Block 6 40%)',
'of Lifting (Fortify Carry Weight 1 +25)','of Hauling (Fortify Carry Weight 2 +30)','of Strength (Fortify Carry Weight 3 +35)','of Brawn (Fortify Carry Weight 4 +40)','of the Ox (Fortify Carry Weight 5 +45)','of the Mammoth (Fortify Carry Weight 6 +50)',
'of Minor Conjuration (Fortify Conjuration 1 12%)','of Conjuration (Fortify Conjuration 2 15%)','of Major Conjuration (Fortify Conjuration 3 17%)','of Eminent Conjuration (Fortify Conjuration 4 20%)','of Extreme Conjuration (Fortify Conjuration 5 22%)','of Peerless Conjuration (Fortify Conjuration 6 25%)',
'of Minor Destruction (Fortify Destruction 1 12%)','of Destruction (Fortify Destruction 2 15%)','of Major Destruction (Fortify Destruction 3 17%)','of Eminent Destruction (Fortify Destruction 4 20%)','of Extreme Destruction (Fortify Destruction 5 22%)','of Peerless Destruction (Fortify Destruction 6 25%)',
'of Remedy (Fortify Healing Rate 3 20%)','of Mending (Fortify Healing Rate 4 30%)','of Regeneration (Fortify Healing Rate 5 40%)','of Revival (Fortify Healing Rate 6 50%)',
'of Minor Health (Fortify Health 1 +20)','of Health (Fortify Health 2 +30)','of Major Health (Fortify Health 3 +40)','of Eminent Health (Fortify Health 4 +50)','of Extreme Health (Fortify Health 5 +60)','of Peerless Health (Fortify Health 6 +70)',
'of the Minor Knight (Fortify Heavy Armor 1 12%)','of the Knight (Fortify Heavy Armor 2 15%)','of the Major Knight (Fortify Heavy Armor 3 17%)','of the Eminent Knight (Fortify Heavy Armor 4 20%)','of the Extreme Knight (Fortify Heavy Armor 5 22%)','of the Peerless Knight (Fortify Heavy Armor 6 25%)',
'of Minor Illusion (Fortify Illusion 1 12%)','of Illusion (Fortify Illusion 2 15%)','of Major Illusion (Fortify Illusion 3 17%)','of Eminent Illusion (Fortify Illusion 4 20%)','of Extreme Illusion (Fortify Illusion 5 22%)','of Peerless Illusion (Fortify Illusion 6 25%)',
'of the Minor Squire (Fortify Light Armor 1 12%)','of the Squire (Fortify Light Armor 2 15%)','of the Major Squire (Fortify Light Armor 3 17%)','of the Eminent Squire (Fortify Light Armor 4 20%)','of the Extreme Squire (Fortify Light Armor 5 22%)','of the Peerless Squire (Fortify Light Armor 6 25%)',
'of Minor Magicka (Fortify Magicka 1 +20)','of Magicka (Fortify Magicka 2 +30)','of Major Magicka (Fortify Magicka 3 +40)','of Eminent Magicka (Fortify Magicka 4 +50)','of Extreme Magicka (Fortify Magicka 5 +60)','of Peerless Magicka (Fortify Magicka 6 +70)',
'of Recharging (Fortify Magicka Rate 3 40%)','of Replenishing (Fortify Magicka Rate 4 60%)','of Resurgence (Fortify Magicka Rate 5 80%)','of Recovery (Fortify Magicka Rate 6 100%)',
'of Minor Wielding (Fortify One-Handed 1 15%)','of Wielding (Fortify One-Handed 2 20%)','of Major Wielding (Fortify One-Handed 3 25%)','of Eminent Wielding (Fortify One-Handed 4 30%)','of Extreme Wielding (Fortify One-Handed 5 35%)','of Peerless Wielding (Fortify One-Handed 6 40%)',
'of Minor Archery (Fortify Archery 1 15%)','of Archery (Fortify Archery 2 20%)','of Major Archery (Fortify Archery 3 25%)','of Eminent Archery (Fortify Archery 4 30%)','of Extreme Archery (Fortify Archery 5 35%)','of Peerless Archery (Fortify Archery 6 40%)',
'of Minor Deft Hands (Fortify Pickpocket 1 15%)','of Deft Hands (Fortify Pickpocket 2 20%)','of Major Deft Hands (Fortify Pickpocket 3 25%)','of Eminent Deft Hands (Fortify Pickpocket 4 30%)','of Extreme Deft Hands (Fortify Pickpocket 5 35%)','of Peerless Deft Hands (Fortify Pickpocket 6 40%)',
'of Minor Smithing (Fortify Smithing 1 12%)','of Smithing (Fortify Smithing 2 15%)','of Major Smithing (Fortify Smithing 3 17%)','of Eminent Smithing (Fortify Smithing 4 20%)','of Extreme Smithing (Fortify Smithing 5 22%)','of Peerless Smithing (Fortify Smithing 6 25%)',
'of Minor Restoration (Fortify Restoration 1 12%)','of Restoration (Fortify Restoration 2 15%)','of Major Restoration (Fortify Restoration 3 17%)','of Eminent Restoration (Fortify Restoration 4 20%)','of Extreme Restoration (Fortify Restoration 5 22%)','of Peerless Restoration (Fortify Restoration 6 25%)',
'of Minor Sneaking (Fortify Sneak 1 15%)','of Sneaking (Fortify Sneak 2 20%)','of Major Sneaking (Fortify Sneak 3 25%)','of Eminent Sneaking (Fortify Sneak 4 30%)','of Extreme Sneaking (Fortify Sneak 5 35%)','of Peerless Sneaking (Fortify Sneak 6 40%)',
'of Minor Lockpicking (Fortify Lockpicking 1 15%)','of Lockpicking (Fortify Lockpicking 2 20%)','of Major Lockpicking (Fortify Lockpicking 3 25%)','of Eminent Lockpicking (Fortify Lockpicking 4 30%)','of Extreme Lockpicking (Fortify Lockpicking 5 35%)','of Peerless Lockpicking (Fortify Lockpicking 6 40%)',
'of Minor Haggling (Fortify Barter 1 12%)','of Haggling (Fortify Barter 2 15%)','of Major Haggling (Fortify Barter 3 17%)','of Eminent Haggling (Fortify Barter 4 20%)','of Extreme Haggling (Fortify Barter 5 22%)','of Peerless Haggling (Fortify Barter 6 25%)',
'of Minor Striking (Fortify Two-Handed 1 15%)','of Striking (Fortify Two-Handed 2 20%)','of Major Striking (Fortify Two-Handed 3 25%)','of Extreme Striking (Fortify Two-Handed 5 35%)','of Peerless Striking (Fortify Two-Handed 6 40%)',
'of Disease Resistance (Resist Disease 50%)','of Disease Immunity (Resist Disease 100%)',
'of Waning Fire (Resist Fire 1 30%)','of Dwindling Flames (Resist Fire 2 40%)','of Flame Suppression (Resist Fire 3 50%)','of Fire Abatement (Resist Fire 4 60%)','of the Firewalker (Resist Fire 5 70%)',
'of Waning Frost (Resist Frost 1 30%)','of Dwindling Frost (Resist Frost 2 40%)','of Frost Suppression (Resist Frost 3 50%)','of Frost Abatement (Resist Frost 4 60%)','of Warmth (Resist Frost 5 70%)',
'of Poison Resistance (Resist Poison 50%)','of Poison Immunity 9Resist Poison 100%)',
'of Waning Shock (Resist Shock 1 30%)','of Dwindling Shock (Resist Shock 2 40%)','of Shock Suppression (Resist Shock 3 50%)','of Shock Abatement (Resist Shock 4 60%)','of Grounding (Resist Shock 5 70%)',
'of Resist Magic (Resist Magic 1 10%)','of Dwindling Magic (Resist Magic 2 15%)','of Magic Suppression (Resist Magic 3 17%)','of Magic Abatement (Resist Magic 4 20%)','of Nullification (Resist Magic 5 22%)',
'of Waterbreathing','of Muffling'
]

ITEMS = ['Amulet ','Abacus ','Arcane Focus ','Backpack ','Bagpipes ','Ball Bearings ','Barding ','Barrel ','Basket ','Bedroll ','Bell ','Ring ','Necklace ','Cloth ','Walking Stick ','Watch ','Potion ','Elixir ','Boots ','Breastplate ','Bottle ','Book ','Bucket ','Candle '
]

def summon_item():
    Item = []
    for i in range(1):
        a=random.sample(ITEMS,1)
        b=random.sample(ITEMMODS,1)
        Item.append(a[0]+b[0])
    return Item

window = Tk()
window.geometry("650x200")
l1=Label(window,text="Need a Monster?",font=10)
l1.grid(row=5,column=2)
l2=Label(window,text="Need a Boss?",font=10)
l2.grid(row=0,column=2)
l3=Label(window,text="Need a Magic Item?",font=10)
l3.grid(row=10,column=2)
def click1():
    res = summon_monsters(level=random.randint(1,9), count=1, name= None)
    l1.configure(text=res)
def click2():
    res = summon_boss(level=random.randint(3,9), count=1, name= None)
    l2.configure(text=res)
def click3():
    res = summon_item()
    l3.configure(text=res)
btn1=Button(window,text="Monster",fg="yellow",bg="red",command=click1)
btn1.grid(row=5,column=0)
btn2=Button(window,text="Boss",fg="yellow",bg="red",command=click2)
btn2.grid(row=0,column=0)
btn3=Button(window,text="Item",fg="yellow",bg="red",command=click3)
btn3.grid(row=10,column=0)
window.mainloop()
