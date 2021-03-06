import csv, re

# This method exports the final data as csv file
def export_csv(poke_dict):
	with open("poke_dict.csv", "w") as file:
		pokemon_writer = csv.writer(file)
		pokemon_writer.writerows(poke_dict)

# This method gets HTML Code as a string and cleans using regular expression
def clean_tags(raw_html):

	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

# Helper function to understand if a string is also a number
def is_integer(str):
	try:
		int(str)
		return True
	except:
		return False

# This method modifies the data for final entry
def arrange_data(pokemon, definition, evo_list, main_image, counter, pokedex_data, training, breeding, base_stats, move_tables):

	if len(evo_list) < 1:
		evo_list = "No Evolution"

	return [counter, pokemon, definition, main_image,
         evo_list, pokedex_data, training, breeding, base_stats, move_tables]

# Running precautions
def run_precaution(pokemon):

	# Extra caution for nidoran genders and flabebe
	if pokemon == "Nidoran♀":
		pokemon = "nidoran-f"
	if pokemon == "Nidoran♂":
		pokemon = "nidoran-m"
	if pokemon == "Flabébé":
		pokemon = "flabebe"

	# Extra caution for farfetch'd and his mates
	namelist = list(pokemon)
	if "'" in namelist:
		oldname = pokemon.split("'")
		pokemon = ""
		for chars in oldname:
			pokemon += chars

	if pokemon == "Mime Jr.":
		pokemon = "mime-jr"
	# Extra caution for Mr. Mime and his bros
	elif "." in namelist:
		oldname = pokemon.split(". ")
		pokemon = oldname[0] + "-" + oldname[1]
	# For the Pokemon Type: Null
	elif ":" in namelist:
		oldname = pokemon.split(": ")
		pokemon = oldname[0] + "-" + oldname[1]
	# Tapu Pokemon
	elif " " in namelist:
		oldname = pokemon.split(" ")
		pokemon = oldname[0] + "-" + oldname[1]

	return pokemon
