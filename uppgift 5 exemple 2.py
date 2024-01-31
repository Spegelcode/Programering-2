class Character:
    def perform_action(self):
        pass

class Hero(Character):
    def perform_action(self):
        return "Hjälten attackerar fienden med sitt svärd!"

class Enemy(Character):
    def perform_action(self):
        return "Fienden skjuter på hjälten med sina pilar!"

class NPC(Character):
    def perform_action(self):
        return "NPC:n ger spelaren en gåva som belöning!"

def perform_character_action(character):
    return character.perform_action()

hero = Hero()
enemy = Enemy()
npc = NPC()

print(perform_character_action(hero))  # Output: "Hjälten attackerar fienden med sitt svärd!"
print(perform_character_action(enemy))  # Output: "Fienden skjuter på hjälten med sina pilar!"
print(perform_character_action(npc))    # Output: "NPC:n ger spelaren en gåva som belöning!"
