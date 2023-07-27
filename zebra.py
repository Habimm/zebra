from info import info

houses = ["1", "2", "3", "4", "5"]
colors = ["Red", "Green", "Ivory", "Yellow", "Blue"]
nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
pets = ["Dog", "Snails", "Fox", "Horse", "Zebra"]
drinks = ["Water", "Tea", "OrangeJuice", "Milk", "Coffee"]
cigarettes = ["OldGold", "Kools", "Chesterfields", "LuckyStrike", "Parliaments"]

# Jedes Haus hat genau eine Farbe.
for house in houses:

  has_at_least_one_color = " OR ".join([f"{color}_{house}" for color in colors])
  print(has_at_least_one_color)
  for color in colors:
    for not_this_color in colors:
      if not_this_color == color: continue
      has_at_most_one_color = f"IF {color}_{house} THEN NOT {not_this_color}_{house}"
      print(has_at_most_one_color)
  print()

  has_at_least_one_nationality = " OR ".join([f"{nationality}_{house}" for nationality in nationalities])
  print(has_at_least_one_nationality)
  for nationality in nationalities:
    for not_this_nationality in nationalities:
      if not_this_nationality == nationality: continue
      has_at_most_one_nationality = f"IF {nationality}_{house} THEN NOT {not_this_nationality}_{house}"
      print(has_at_most_one_nationality)
  print()

  has_at_least_one_pet = " OR ".join([f"{pet}_{house}" for pet in pets])
  print(has_at_least_one_pet)
  for pet in pets:
    for not_this_pet in pets:
      if not_this_pet == pet: continue
      has_at_most_one_pet = f"IF {pet}_{house} THEN NOT {not_this_pet}_{house}"
      print(has_at_most_one_pet)
  print()

  has_at_least_one_drink = " OR ".join([f"{drink}_{house}" for drink in drinks])
  print(has_at_least_one_drink)
  for drink in drinks:
    for not_this_drink in drinks:
      if not_this_drink == drink: continue
      has_at_most_one_drink = f"IF {drink}_{house} THEN NOT {not_this_drink}_{house}"
      print(has_at_most_one_drink)
  print()

  has_at_least_one_cigarette = " OR ".join([f"{cigarette}_{house}" for cigarette in cigarettes])
  print(has_at_least_one_cigarette)
  for cigarette in cigarettes:
    for not_this_cigarette in cigarettes:
      if not_this_cigarette == cigarette: continue
      has_at_most_one_cigarette = f"IF {cigarette}_{house} THEN NOT {not_this_cigarette}_{house}"
      print(has_at_most_one_cigarette)
  print()



# Jede Farbe kommt bei genau einem Haus vor.
for color in colors:
  has_at_least_one_house = " OR ".join([f"{color}_{house}" for house in houses])
  print(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {color}_{house} THEN NOT {color}_{not_this_house}"
      print(has_at_most_one_house)
  print()

for nationality in nationalities:
  has_at_least_one_house = " OR ".join([f"{nationality}_{house}" for house in houses])
  print(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {nationality}_{house} THEN NOT {nationality}_{not_this_house}"
      print(has_at_most_one_house)
  print()

for pet in pets:
  has_at_least_one_house = " OR ".join([f"{pet}_{house}" for house in houses])
  print(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {pet}_{house} THEN NOT {pet}_{not_this_house}"
      print(has_at_most_one_house)
  print()

for drink in drinks:
  has_at_least_one_house = " OR ".join([f"{drink}_{house}" for house in houses])
  print(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {drink}_{house} THEN NOT {drink}_{not_this_house}"
      print(has_at_most_one_house)
  print()

for cigarette in cigarettes:
  has_at_least_one_house = " OR ".join([f"{cigarette}_{house}" for house in houses])
  print(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {cigarette}_{house} THEN NOT {cigarette}_{not_this_house}"
      print(has_at_most_one_house)
  print()




# https://simewu.com/SAT-solver/
# https://waitbutwhy.com/table/zebra-puzzle



statements = []
for color in colors:
  for house in houses:
    statement = f"{color}_{house}"
    statements.append(statement)
for nationality in nationalities:
  for house in houses:
    statement = f"{nationality}_{house}"
    statements.append(statement)
for pet in pets:
  for house in houses:
    statement = f"{pet}_{house}"
    statements.append(statement)
for drink in drinks:
  for house in houses:
    statement = f"{drink}_{house}"
    statements.append(statement)
for cigarette in cigarettes:
  for house in houses:
    statement = f"{cigarette}_{house}"
    statements.append(statement)
info(statements)






def process_constraints(constraints_string):
  constraints = constraints_string.split('\n')
  output_constraints = []

  for statement in constraints:
    # Split the statement into parts
    parts = statement.split()
    if not parts: continue

    # Convert the statement into the new format
    # info(parts)
    # info(output_constraints)
    if 'IF' not in parts:
      # Single condition or multiple OR conditions without a precondition
      conditions = parts
      condition_ids = [str(1 + statements.index(condition.strip())) for condition in conditions if condition.strip() not in ['OR']]
      output_constraints.append('{}'.format(' '.join(condition_ids)))
    elif 'OR' not in parts:
      # Handle the case where there are multiple options after THEN
      if parts[3] == 'NOT':
        options = parts[4:]
        option_ids = [str(1 + statements.index(option.strip())) for option in options if option.strip() not in ['OR', 'THEN']]
        output_constraints.append('-{} -{}'.format(1 + statements.index(parts[1]), ' '.join(option_ids)))
      else:
        options = parts[3:]
        option_ids = [str(1 + statements.index(option.strip())) for option in options if option.strip() not in ['OR', 'THEN']]
        output_constraints.append('-{} {}'.format(1 + statements.index(parts[1]), ' '.join(option_ids)))

  return output_constraints


with open("zebra.sat") as sat_file:
 simple_sat_language = sat_file.read()

info(simple_sat_language)

output_constraints = process_constraints(simple_sat_language)

with open("mapping.csv", "w") as mapping_file:
  for index, right in enumerate(statements):
   print(f"{index + 1}: {right}", file=mapping_file)

with open("cons.text", "w") as cons_file:
  for statement in output_constraints:
    print(statement, file=cons_file)
