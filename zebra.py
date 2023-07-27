from info import info

# https://simewu.com/SAT-solver/
# https://waitbutwhy.com/table/zebra-puzzle

# GENERATE SYNTAX

houses = ["1", "2", "3", "4", "5"]
colors = ["Red", "Green", "Ivory", "Yellow", "Blue"]
nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
pets = ["Dog", "Snails", "Fox", "Horse", "Zebra"]
drinks = ["Water", "Tea", "OrangeJuice", "Milk", "Coffee"]
cigarettes = ["OldGold", "Kools", "Chesterfields", "LuckyStrike", "Parliaments"]

syntactical_constraints = []

# Jedes Haus hat genau eine Farbe.
for house in houses:

  has_at_least_one_color = " OR ".join([f"{color}_{house}" for color in colors])
  syntactical_constraints.append(has_at_least_one_color)
  for color in colors:
    for not_this_color in colors:
      if not_this_color == color: continue
      has_at_most_one_color = f"IF {color}_{house} THEN NOT {not_this_color}_{house}"
      syntactical_constraints.append(has_at_most_one_color)

  has_at_least_one_nationality = " OR ".join([f"{nationality}_{house}" for nationality in nationalities])
  syntactical_constraints.append(has_at_least_one_nationality)
  for nationality in nationalities:
    for not_this_nationality in nationalities:
      if not_this_nationality == nationality: continue
      has_at_most_one_nationality = f"IF {nationality}_{house} THEN NOT {not_this_nationality}_{house}"
      syntactical_constraints.append(has_at_most_one_nationality)

  has_at_least_one_pet = " OR ".join([f"{pet}_{house}" for pet in pets])
  syntactical_constraints.append(has_at_least_one_pet)
  for pet in pets:
    for not_this_pet in pets:
      if not_this_pet == pet: continue
      has_at_most_one_pet = f"IF {pet}_{house} THEN NOT {not_this_pet}_{house}"
      syntactical_constraints.append(has_at_most_one_pet)

  has_at_least_one_drink = " OR ".join([f"{drink}_{house}" for drink in drinks])
  syntactical_constraints.append(has_at_least_one_drink)
  for drink in drinks:
    for not_this_drink in drinks:
      if not_this_drink == drink: continue
      has_at_most_one_drink = f"IF {drink}_{house} THEN NOT {not_this_drink}_{house}"
      syntactical_constraints.append(has_at_most_one_drink)

  has_at_least_one_cigarette = " OR ".join([f"{cigarette}_{house}" for cigarette in cigarettes])
  syntactical_constraints.append(has_at_least_one_cigarette)
  for cigarette in cigarettes:
    for not_this_cigarette in cigarettes:
      if not_this_cigarette == cigarette: continue
      has_at_most_one_cigarette = f"IF {cigarette}_{house} THEN NOT {not_this_cigarette}_{house}"
      syntactical_constraints.append(has_at_most_one_cigarette)



# Jede Farbe kommt bei genau einem Haus vor.
for color in colors:
  has_at_least_one_house = " OR ".join([f"{color}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {color}_{house} THEN NOT {color}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)

for nationality in nationalities:
  has_at_least_one_house = " OR ".join([f"{nationality}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {nationality}_{house} THEN NOT {nationality}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)

for pet in pets:
  has_at_least_one_house = " OR ".join([f"{pet}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {pet}_{house} THEN NOT {pet}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)

for drink in drinks:
  has_at_least_one_house = " OR ".join([f"{drink}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {drink}_{house} THEN NOT {drink}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)

for cigarette in cigarettes:
  has_at_least_one_house = " OR ".join([f"{cigarette}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {cigarette}_{house} THEN NOT {cigarette}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)

# CONVERT NAMES TO NUMBERS

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

def process_constraints(constraints_string):
  constraints = constraints_string.split('\n')
  constraints_using_numbers = []

  for constraint in constraints:

    # Ignore comment
    if constraint and constraint[0] == '=': continue

    # Split the constraint into parts
    parts = constraint.split()
    if not parts: continue

    # Convert the statement into the new format
    if 'IF' not in parts:
      # Single condition or multiple OR conditions without a precondition
      conditions = parts
      condition_ids = [str(1 + statements.index(condition.strip())) for condition in conditions if condition.strip() not in ['OR']]
      constraints_using_numbers.append('{}'.format(' '.join(condition_ids)))
    elif 'OR' not in parts:
      # Handle the case where there are multiple options after THEN
      if parts[3] == 'NOT':
        options = parts[4:]
        option_ids = [str(1 + statements.index(option.strip())) for option in options if option.strip() not in ['OR', 'THEN']]
        constraints_using_numbers.append('-{} -{}'.format(1 + statements.index(parts[1]), ' '.join(option_ids)))
      else:
        options = parts[3:]
        option_ids = [str(1 + statements.index(option.strip())) for option in options if option.strip() not in ['OR', 'THEN']]
        constraints_using_numbers.append('-{} {}'.format(1 + statements.index(parts[1]), ' '.join(option_ids)))

  return constraints_using_numbers

with open("empirical_constraints.txt") as sat_file:
 simple_sat_language = sat_file.read()

syntactical_constraints = "\n".join(syntactical_constraints)
simple_sat_language = f"{syntactical_constraints}\n{simple_sat_language}"

constraints_using_numbers = process_constraints(simple_sat_language)

with open("mapping.csv", "w") as mapping_file:
  for index, right in enumerate(statements):
   print(f"{index + 1}: {right}", file=mapping_file)

with open("cons.txt", "w") as cons_file:
  for statement in constraints_using_numbers:
    print(statement, file=cons_file)
