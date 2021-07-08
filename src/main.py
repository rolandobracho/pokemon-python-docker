print("Inicio.")
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import json
     
def get_all_pokemons(url):
	allpokemos = []
	return get_all_pokemons_helper(url, allpokemos)

def get_all_pokemons_helper(url, allpokemos):
	if url == None:
		return allpokemos
	data = requests.get(url).json()
	allpokemos = allpokemos + data["results"]
	return get_all_pokemons_helper(data["next"], allpokemos)

def get_first_pokemons(url):
	return requests.get(url).json()

def question_one(url):
	list_pokemon = get_all_pokemons(url)
	#list_pokemon = get_first_pokemons(url) #solo para pruebas
	countAt = len(list(filter(lambda x: 'at' in x["name"], list_pokemon)))
	return len(list(filter(lambda x: x["name"].count('a') == 2, list_pokemon)))

def uniques_all_pokemon_species(all_pokemon):
	list_seen_pokemon = set()
	[x for x in all_pokemon if x["name"] in list_seen_pokemon or list_seen_pokemon.add(x["name"])]
	return len(list_seen_pokemon)

def question_two(url, name):
	data = requests.get(url + name).json()
	all_pokemon_species = []
	for d in data["egg_groups"]:
		egg_groups = requests.get(d["url"]).json()
		all_pokemon_species = all_pokemon_species + egg_groups["pokemon_species"]
	uniques_pokemon = uniques_all_pokemon_species(all_pokemon_species)
	return uniques_pokemon

def question_three(url, name_type, id_type_max):
	data = requests.get(url + name_type).json()
	list_weights = set()
	for d in data["pokemon"]:
		pokemon_id = d["pokemon"]["url"].split("/")[-2:][0]
		if pokemon_id <= id_type_max :
			pokemon = requests.get(d["pokemon"]["url"]).json()
			list_weights.add(pokemon["weight"])
			min_weight = min(list_weights)
			max_weight = max(list_weights)
	return [max_weight , min_weight]


url = os.getenv("url")
name_question_two = os.getenv("name_question_two")
name_type = os.getenv("name_type")
id_type_max = os.getenv("id_type_max")

count = question_one(url + "pokemon/")
count_two = question_two( url + "pokemon-species/", name_question_two)
count_three = question_three( url + "type/", name_type, id_type_max)

print("Respuesta uno: " , 	count)
print("Respuesta dos: " , 	count_two)
print("Respuesta tres: " , 	count_three)