import os
import pandas

# See:
#   https://simewu.com/SAT-solver/
#   MIT NULLEN: http://logicrunch.it.uu.se:4096/~wv/minisat/?ex=simple%2Fanomaly
#   MIT NULLEN: https://msoos.github.io/cryptominisat_web/
#   https://waitbutwhy.com/table/zebra-puzzle

def generate_syntactical_constraints():
  houses = ["1", "2", "3", "4", "5"]
  colors = ["Red", "Green", "Ivory", "Yellow", "Blue"]
  nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
  pets = ["Dog", "Snails", "Fox", "Horse", "Zebra"]
  drinks = ["Water", "Tea", "OrangeJuice", "Milk", "Coffee"]
  cigarettes = ["OldGold", "Kools", "Chesterfields", "LuckyStrike", "Parliaments"]

  syntactical_constraints = []

  # Each house has one color.
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

  # Each color has one house.
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

  return syntactical_constraints



if __name__ == "__main__":

  # Milestone 0: Loaded empirical constraints
  with open("empirical_constraints.satcode") as empirical_constraints_file:
    simple_sat_language = empirical_constraints_file.read()

  if not os.path.exists("milestones"):
    os.mkdir("milestones")

  with open("milestones/0_loaded.satcode", "w") as loaded_file:
    loaded_file.write(simple_sat_language)

  # Milestone 1: Added in the syntax rules.
  # ==================================================================================================
  generated_syntactical_constraints = generate_syntactical_constraints()
  generated_syntactical_constraints = "\n".join(generated_syntactical_constraints)
  simple_sat_language = (
    "= 1. There are five houses."
    "\n"
    "====================================================================================="
    "\n"
    f"{generated_syntactical_constraints}"
    "\n"
    "====================================================================================="
    "\n\n"
    f"{simple_sat_language}"
  )

  with open("milestones/1_syntax.satcode", "w") as syntax_file:
    syntax_file.write(simple_sat_language)

  # Milestone 2: Removed the comments and whitespace.
  # ==================================================================================================
  simple_sat_language = simple_sat_language.split("\n")
  cleaned = []
  for line in simple_sat_language:
    if not line or line.startswith("="): continue
    cleaned.append(line)

  with open("milestones/2_cleaned.satcode", "w") as cleaned_file:
    cleaned_file.write("\n".join(cleaned))

  # Milestone 3: Transformed operators.
  # ==================================================================================================
  transformed_operators = []
  for line in cleaned:
    transformed_line = line.replace("IF ", "-")
    transformed_line = transformed_line.replace("THEN ", "")
    transformed_line = transformed_line.replace("OR ", "")
    transformed_line = transformed_line.replace("NOT ", "-")
    transformed_operators.append(transformed_line)

  with open("milestones/3_operators.satcode", "w") as operators_file:
    operators_file.write("\n".join(transformed_operators))

  # Milestone 4: Enumerated variables.
  # ==================================================================================================
  houses = ["1", "2", "3", "4", "5"]
  colors = ["Red", "Green", "Ivory", "Yellow", "Blue"]
  nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
  pets = ["Dog", "Snails", "Fox", "Horse", "Zebra"]
  drinks = ["Water", "Tea", "OrangeJuice", "Milk", "Coffee"]
  cigarettes = ["OldGold", "Kools", "Chesterfields", "LuckyStrike", "Parliaments"]

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
  proposition_enumeration_reverse = {}
  for index, proposition in enumerate(propositions):
    proposition_enumeration[proposition] = index + 1
    proposition_enumeration_reverse[f"x{index + 1}"] = proposition

  with open("milestones/proposition_enumeration.csv", "w") as propositions_file:
    for proposition, number in proposition_enumeration.items():
      print(f"x{number} = {proposition}", file=propositions_file)

  def replace_literal(literal):
    if literal.startswith("-"): return f"-{proposition_enumeration[literal[1:]]}"
    else: return f"{proposition_enumeration[literal]}"

  enumerated_language = []
  for line in transformed_operators:
    literals = line.split(" ")
    proposition_numbers = [replace_literal(literal) for literal in literals]
    enumerated_language.append(" ".join(proposition_numbers))

  with open("milestones/4_enumerated.satcode", "w") as propositions_file:
    propositions_file.write("\n".join(enumerated_language))

  # Milestone 5: Show the assignment.
  # ==================================================================================================
  if os.path.exists("milestones/proposition_assignment.csv"):
    assignment = pandas.read_csv("milestones/proposition_assignment.csv", sep="=", names=['Proposition', 'Assignment'])
    assignment['Proposition'] = assignment['Proposition'].str.replace(' ', '')
    assignment['Proposition'] = assignment['Proposition'].map(proposition_enumeration_reverse)
    assignment = assignment[assignment['Assignment'] == 1]
    assignment = assignment['Proposition']

    spatial_index = ["Color", "Nationality", "Pet", "Drink", "Cigarettes"]
    spatial_table = pandas.DataFrame(columns=houses, index=spatial_index)

    for spatial_table_row_start_index, spatial_table_row_name in zip(range(0, assignment.shape[0], 5), spatial_index):
      spatial_table_row = assignment[spatial_table_row_start_index:spatial_table_row_start_index+5]
      for house_property in spatial_table_row:
        house_property, spatial_table_column_name = house_property.split("_")
        spatial_table.loc[spatial_table_row_name][spatial_table_column_name] = house_property

    spatial_table.to_csv("milestones/decoded_proposition_assignment.csv")
