import random

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

ITEMS = ['Amulet','Abacus','Arcane Focus','Backpack','Bagpipes','Ball Bearings','Barding','Barrel','Basket','Bedroll','Bell','Ring','Necklace','Cloth','Walking Stick','Watch','Potion','Elixir','Boots','Breastplate','Bottle','Book','Bucket','Candle'
]

item = []
for i in range(10):
    a=random.sample(ITEMS,1)
    b=random.sample(ITEMMODS,1)
    item.append(a[0]+b[0])
print(item)
