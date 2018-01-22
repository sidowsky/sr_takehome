from constants import *


#prune the cache to ignore foods that violate constraints by themselves
def prune_cache(cache, calories, max_fat, max_carbs, max_protein):
  pruned_cache = {}
  
  for food_id in cache.keys():
    food = cache[food_id]
    ignore = food[ENERC_KCAL] > calories or food[FAT] > max_fat or food[CHOCDF] > max_carbs or food[PROCNT] > max_protein
    
    if ignore:
      continue
    
    pruned_cache[food_id] = food
  
  return pruned_cache

def build_meal(cache, calories, fat_pct, carbs_pct, protein_pct):
  #calc max number of calories for each category
  max_fat = fat_pct / 100.0 * calories;
  max_carbs = carbs_pct / 100.0 * calories;
  max_protein = protein_pct / 100.0 * calories;
  
  relevant_foods = prune_cache(cache, calories, max_fat, max_carbs, max_protein)
  
  return relevant_foods