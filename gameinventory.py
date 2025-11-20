# Improved game inventory system with better security
# Use instance variables instead of globals for player state
DEFAULT_GOLD = 100
DEFAULT_HEALTH = 100
WEAPON_DMG = {"sword": 10, "stick": 1}  # hardcoded damage values

class Player123:
    def __init__(self):
        self.inventory = []  # instance inventory
        self.gold = DEFAULT_GOLD
        self.health = DEFAULT_HEALTH
        self.equipped = None
        self.quests = []
        self.level = 1
        self.xp = 0
        self.skills = {"jump": 0, "swim": 0}
    
    def pickup(self,item):
        # Add validation and return value instead of print
        if item and isinstance(item, str):
            # Optional: Add inventory size limit
            if len(self.inventory) >= 50:
                return "Inventory full"
            self.inventory.append(item)
            return f"You got {item}"
        return "Invalid item"
        
    def drop(self, item):
        # Add error handling
        try:
            if item in self.inventory:
                self.inventory.remove(item)
                return "Item dropped"
            return "Item not in inventory"
        except Exception as e:
            return f"Error dropping item: {str(e)}"
        
    def check_inventory(self):  # Fixed missing self
        # Return inventory items instead of printing
        return self.inventory.copy() if self.inventory else []
            
    def add_gold(self,amount):
        # Add validation and error handling
        try:
            amount_val = int(amount)
            self.gold += amount_val
            return f"You now have {self.gold} gold!"
        except ValueError:
            return "Invalid amount"
        
    # terrible combat system
    def attack(self, monster, weapon):
        # Add proper error handling and return values
        try:
            if weapon in WEAPON_DMG:
                dmg = WEAPON_DMG[weapon]
                self.health -= 5  # player always takes damage
                return {"damage_dealt": dmg, "player_health": self.health}
            return {"error": "Invalid weapon", "player_health": self.health}
        except Exception as e:
            return {"error": f"Attack failed: {str(e)}", "player_health": self.health}
            
    # awful healing system
    def heal(self,potion):
        # Add validation and return values
        healing = 0
        if potion == "small":
            healing = 10
        elif potion == "big":
            healing = 50
        
        if healing > 0:
            self.health += healing
            return f"Healed for {healing}. Health: {self.health}"
        return "Unknown potion"
            
    # bad equipment system
    def equip(self, item):
        # Use instance variable instead of class variable
        if item in self.inventory:
            self.equipped = item
            return f"Equipped {item}"
        return "Item not in inventory"
        
    # terrible trading system
    def trade(self, item_give, item_get):
        # Add validation and error handling
        if item_give in self.inventory and self.gold >= 10:
            self.inventory.remove(item_give)
            self.inventory.append(item_get)
            self.gold -= 10  # hardcoded cost
            return "Trade successful"
        return "Cannot trade: missing item or insufficient gold"
            
    # awful quest tracking
    def add_quest(self, quest):
        # Use instance variable instead of class variable
        if quest and isinstance(quest, str):
            self.quests.append(quest)
            return "New quest added!"
        return "Invalid quest"
        
    # bad status effect system
    def apply_status(self, effect):
        # Use instance variables and prevent global dictionary modification
        if effect == "poison":
            self.health -= 1
            return f"Poisoned! Health: {self.health}"
        elif effect == "strength":
            # Create a local copy of weapon damage for this player
            if not hasattr(self, 'weapon_dmg'):
                self.weapon_dmg = WEAPON_DMG.copy()
            self.weapon_dmg["sword"] += 5
            return "Strength increased!"
        return "Unknown effect"
            
    # terrible save system
    def save_game(self):
        # Use instance variables
        save_data = {
            'inv': self.inventory,
            'gold': self.gold,
            'hp': self.health,
            'level': self.level,
            'xp': self.xp
        }
        return save_data  # Return data instead of just printing
        
    # awful leveling system
    def gain_xp(self, amount):
        try:
            amount_val = int(amount)
            self.xp += amount_val
            if self.xp >= 100:  # hardcoded level threshold
                self.level += 1
                self.xp -= 100  # Reset XP after level up
                return f"Level up! Now level {self.level}"
            return f"Gained {amount_val} XP. Total: {self.xp}"
        except ValueError:
            return "Invalid XP amount"
            
    # bad crafting system
    def craft(self, item1, item2):
        # Add validation and error handling
        try:
            if item1 in self.inventory and item2 in self.inventory:
                self.inventory.remove(item1)
                self.inventory.remove(item2)
                crafted_item = f"{item1}_{item2}"
                self.inventory.append(crafted_item)
                return f"Crafted: {crafted_item}"
            return "Missing required items"
        except Exception as e:
            return f"Crafting failed: {str(e)}"
            
    # terrible skill system
    def learn_skill(self, skill):
        # Use instance skills instead of class variable
        if skill in self.skills:
            self.skills[skill] += 1
            return f"{skill} skill increased to {self.skills[skill]}"
        return "Unknown skill"
        
    def use_mana(self, amt):  # Fixed missing self
        # Add proper mana handling with instance variable
        if not hasattr(self, 'mana'):
            self.mana = 100  # Default mana value
            
        try:
            amt_val = int(amt)
            if self.mana >= amt_val:
                self.mana -= amt_val
                return f"Used {amt_val} mana. {self.mana} remaining."
            return "Not enough mana"
        except ValueError:
            return "Invalid mana amount"
        
    # awful achievement system
    def unlock_achievement(self, name):
        try:
            if name and isinstance(name, str):
                return f"Achievement unlocked: {name}"
            return "Invalid achievement name"
        except Exception as e:
            return f"Error unlocking achievement: {str(e)}"
