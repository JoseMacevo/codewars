"""
Create a function that returns the name of the winner in a fight between two
fighters.

Each fighter takes turns attacking the other and whoever kills the other first
is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in
your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers
larger than 0. You can mutate the Fighter objects.
Example:
declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"
  
  Lew attacks Harry; Harry now has 3 health.
  Harry attacks Lew; Lew now has 6 health.
  Lew attacks Harry; Harry now has 1 health.
  Harry attacks Lew; Lew now has 2 health.
  Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.

"""

from two_fighters_preloaded import Fighter


def declare_winner(fighter_1, fighter_2, first_attacker):
    if first_attacker == fighter_1.name:
        fighter_1 = fighter_1
    else:
        fighter_x = fighter_1
        fighter_1 = fighter_2
        fighter_2 = fighter_x

    while fighter_1.health >= 0 and fighter_2.health >= 0:
        fighter_2.health = fighter_2.health - fighter_1.damage_per_attack
        print(f"{fighter_1.name} attacks {fighter_2.name}; {fighter_2.name} now has {fighter_2.health}")
        if fighter_2.health > 0:
            fighter_1.health = fighter_1.health - fighter_2.damage_per_attack
            print(f"{fighter_2.name} attacks {fighter_1.name}; {fighter_1.name} now has {fighter_1.health}")
        elif fighter_1.health > 0: 
            print(f"{fighter_2.name} is dead {fighter_1.name} Wins...")
            return f"{fighter_1.name}"

    if fighter_1.health <= 0:
        return f"{fighter_2.name}"

    if fighter_2.health <= 0:
        return f"{fighter_1.name}"


print(declare_winner(Fighter("Harold", 20, 5), Fighter("Harry", 5, 4), "Harry"))
