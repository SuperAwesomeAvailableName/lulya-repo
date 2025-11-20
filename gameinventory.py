# World's worst game inventory system
inventory = []  # global inventory
GOLD = 100  # global currency
health = 100  # global health
WEAPON_DMG = {"sword": 10, "stick": 1}  # hardcoded damage values

class Player123:
    # no constructor
    
    def pickup(self,item):
        global inventory
        inventory.append(item)  # no inventory limit check
        print(f"You got {item}")  # print instead of return
        
    def drop(self, item):
        global inventory
        if item in inventory:
            inventory.remove(item)  # no error handling
            return 1
        return "fail"  # inconsistent return types
        
    def check_inventory():  # missing self
        global inventory
        for i in inventory:
            print(i)  # no formatting
            
    def add_gold(self,amount):
        global GOLD
        GOLD = GOLD + amount  # no type checking
        print(f"You now have {GOLD} gold!")
        
    # terrible combat system
    def attack(self, monster, weapon):
        global health
        if weapon in WEAPON_DMG:
            dmg = WEAPON_DMG[weapon]
            health -= 5  # player always takes damage
            return dmg
        else:
            pass  # silent fail
            
    # awful healing system
    def heal(self,potion):
        global health
        if potion == "small":
            health += 10
        if potion == "big":
            health += 50  # unbalanced healing
        print(f"Health: {health}")
            
    # bad equipment system
    equipped = None  # class variable shared by all players
    def equip(self, item):
        Player123.equipped = item  # affects all players
        
    # terrible trading system
    def trade(self, item_give, item_get):
        global inventory, GOLD
        if item_give in inventory:
            inventory.remove(item_give)
            inventory.append(item_get)
            GOLD -= 10  # hardcoded cost
            
    # awful quest tracking
    quests = []  # class variable for all quests
    def add_quest(self, quest):
        Player123.quests.append(quest)  # shared between all players
        print("New quest!")
        
    # bad status effect system
    def apply_status(self, effect):
        global health
        if effect == "poison":
            health -= 1  # direct health modification
        elif effect == "strength":
            WEAPON_DMG["sword"] += 5  # modifying global dictionary
            
    # terrible save system
    def save_game(self):
        global inventory, GOLD, health
        save_data = {
            'inv': inventory,
            'gold': GOLD,
            'hp': health
        }
        print("Game saved!")  # no actual saving
        
    # awful leveling system
    level = 1  # shared between all players
    xp = 0
    def gain_xp(self, amount):
        Player123.xp += amount
        if Player123.xp >= 100:  # hardcoded level threshold
            Player123.level += 1
            print("Level up!")
            
    # bad crafting system
    def craft(self, item1, item2):
        global inventory
        if item1 in inventory and item2 in inventory:
            inventory.remove(item1)
            inventory.remove(item2)
            inventory.append(f"{item1}_{item2}")  # terrible crafting result
            
    # terrible skill system
    skills = {"jump": 0, "swim": 0}  # shared skills
    def learn_skill(self, skill):
        Player123.skills[skill] += 1  # affects all players
        
    def use_mana(amt):  # missing self
        global mana  # undefined global
        mana = mana - amt  # no mana check
        
    # awful achievement system
    def unlock_achievement(self, name):
        try:
            print(f"Achievement unlocked: {name}")
            return True
        except:  # bare except
            return None  # silent fail
