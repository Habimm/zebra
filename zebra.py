from info import info
import os

# https://simewu.com/SAT-solver/
# https://waitbutwhy.com/table/zebra-puzzle

# SOLUTION:
# 1) The Norwegian drinks water
# 2) The Japanese guy has a pet zebra

# GENERATE SYNTAX

# The puzzle consists of five different-colored houses in a row, each lived in by a resident of a different nationality. Each resident owns a different pet, prefers a different drink, and smokes a different brand of cigarettes than the others.
# 1. There are five houses.

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
  syntactical_constraints.append("")

  has_at_least_one_nationality = " OR ".join([f"{nationality}_{house}" for nationality in nationalities])
  syntactical_constraints.append(has_at_least_one_nationality)
  for nationality in nationalities:
    for not_this_nationality in nationalities:
      if not_this_nationality == nationality: continue
      has_at_most_one_nationality = f"IF {nationality}_{house} THEN NOT {not_this_nationality}_{house}"
      syntactical_constraints.append(has_at_most_one_nationality)
  syntactical_constraints.append("")

  has_at_least_one_pet = " OR ".join([f"{pet}_{house}" for pet in pets])
  syntactical_constraints.append(has_at_least_one_pet)
  for pet in pets:
    for not_this_pet in pets:
      if not_this_pet == pet: continue
      has_at_most_one_pet = f"IF {pet}_{house} THEN NOT {not_this_pet}_{house}"
      syntactical_constraints.append(has_at_most_one_pet)
  syntactical_constraints.append("")

  has_at_least_one_drink = " OR ".join([f"{drink}_{house}" for drink in drinks])
  syntactical_constraints.append(has_at_least_one_drink)
  for drink in drinks:
    for not_this_drink in drinks:
      if not_this_drink == drink: continue
      has_at_most_one_drink = f"IF {drink}_{house} THEN NOT {not_this_drink}_{house}"
      syntactical_constraints.append(has_at_most_one_drink)
  syntactical_constraints.append("")

  has_at_least_one_cigarette = " OR ".join([f"{cigarette}_{house}" for cigarette in cigarettes])
  syntactical_constraints.append(has_at_least_one_cigarette)
  for cigarette in cigarettes:
    for not_this_cigarette in cigarettes:
      if not_this_cigarette == cigarette: continue
      has_at_most_one_cigarette = f"IF {cigarette}_{house} THEN NOT {not_this_cigarette}_{house}"
      syntactical_constraints.append(has_at_most_one_cigarette)
  syntactical_constraints.append("")


syntactical_constraints.append("")



# Jede Farbe kommt bei genau einem Haus vor.
for color in colors:
  has_at_least_one_house = " OR ".join([f"{color}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {color}_{house} THEN NOT {color}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)
  syntactical_constraints.append("")

for nationality in nationalities:
  has_at_least_one_house = " OR ".join([f"{nationality}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {nationality}_{house} THEN NOT {nationality}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)
  syntactical_constraints.append("")

for pet in pets:
  has_at_least_one_house = " OR ".join([f"{pet}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {pet}_{house} THEN NOT {pet}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)
  syntactical_constraints.append("")

for drink in drinks:
  has_at_least_one_house = " OR ".join([f"{drink}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {drink}_{house} THEN NOT {drink}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)
  syntactical_constraints.append("")

for cigarette in cigarettes:
  has_at_least_one_house = " OR ".join([f"{cigarette}_{house}" for house in houses])
  syntactical_constraints.append(has_at_least_one_house)
  for house in houses:
    for not_this_house in houses:
      if not_this_house == house: continue
      has_at_most_one_house = f"IF {cigarette}_{house} THEN NOT {cigarette}_{not_this_house}"
      syntactical_constraints.append(has_at_most_one_house)
  syntactical_constraints.append("")
syntactical_constraints = syntactical_constraints[:-1]

# CONVERT NAMES TO NUMBERS


# Milestone 0: Loaded empirical constraints
with open("empirical_constraints.txt") as cons_file:
  simple_sat_language = cons_file.read()

if not os.path.exists("milestones"):
  os.mkdir("milestones")
with open("milestones/1_loaded.txt", "w") as loaded_file:
  loaded_file.write(simple_sat_language)

# Milestone 1: Added in the syntax rules.
syntactical_constraints = "\n".join(syntactical_constraints)
simple_sat_language = (
  "= 1. There are five houses."
  "\n"
  "====================================================================================="
  "\n"
  f"{syntactical_constraints}"
  "\n"
  "====================================================================================="
  "\n\n"
  f"{simple_sat_language}"
)

with open("milestones/2_syntax.txt", "w") as syntax_file:
  syntax_file.write(simple_sat_language)

# Milestone 2: Removed the comments and whitespace.
simple_sat_language = simple_sat_language.split("\n")
cleaned = []
for line in simple_sat_language:
  if not line or line.startswith("="): continue
  print(line)
  cleaned.append(line)

with open("milestones/3_cleaned.txt", "w") as cleaned_file:
  cleaned_file.write("\n".join(cleaned))

# Milestone 3: Transformed operators.
transformed_operators = []
for line in cleaned:
  transformed_line = line.replace("IF ", "-")
  transformed_line = transformed_line.replace("THEN ", "")
  transformed_line = transformed_line.replace("OR ", "")
  transformed_line = transformed_line.replace("NOT ", "-")
  transformed_operators.append(transformed_line)

with open("milestones/4_operators.txt", "w") as operators_file:
  operators_file.write("\n".join(transformed_operators))

# Milestone 4: Enumerated variables.

propositions = []
for color in colors:
  for house in houses:
    proposition = f"{color}_{house}"
    propositions.append(proposition)
for nationality in nationalities:
  for house in houses:
    proposition = f"{nationality}_{house}"
    propositions.append(proposition)
for pet in pets:
  for house in houses:
    proposition = f"{pet}_{house}"
    propositions.append(proposition)
for drink in drinks:
  for house in houses:
    proposition = f"{drink}_{house}"
    propositions.append(proposition)
for cigarette in cigarettes:
  for house in houses:
    proposition = f"{cigarette}_{house}"
    propositions.append(proposition)

proposition_enumeration = {}
for index, proposition in enumerate(propositions):
  proposition_enumeration[proposition] = index + 1

with open("milestones/proposition_enumeration.txt", "w") as propositions_file:
  for proposition, number in proposition_enumeration.items():
    print(f"{number}: {proposition}", file=propositions_file)

def replace_literal(literal):
  if literal.startswith("-"): return f"-{proposition_enumeration[literal[1:]]}"
  else: return f"{proposition_enumeration[literal]}"

enumerated_language = []
for line in transformed_operators:
  literals = line.split(" ")
  proposition_numbers = [replace_literal(literal) for literal in literals]
  enumerated_language.append(" ".join(proposition_numbers))

with open("milestones/5_enumerated.txt", "w") as propositions_file:
  propositions_file.write("\n".join(enumerated_language))

constraints_using_numbers = process_constraints(simple_sat_language)

with open("mapping.csv", "w") as mapping_file:
  for index, right in enumerate(propositions):
   print(f"{index + 1}: {right}", file=mapping_file)

with open("cons.txt", "w") as cons_file:
  for proposition in constraints_using_numbers:
    print(proposition, file=cons_file)
