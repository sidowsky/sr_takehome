from sqlalchemy import create_engine
from constants import get_nutrient_idx

def load_cache():
  db = create_engine('sqlite:///usda.sql3')
  
  cache = {}

  query = "SELECT food.id,food.long_desc,food_group.name,nutrient.tagname,nutrition.amount,weight.gm_weight,weight.gm_weight*nutrition.amount/100.0 as gm_amount,weight.description FROM food, food_group, nutrient, nutrition, weight  where food.food_group_id = food_group.id and food.id = nutrition.food_id and nutrient.id = nutrition.nutrient_id and weight.food_id = food.id and food.id < 1100 and weight.sequence_num = 1 and nutrient.tagname in ('ENERC_KCAL','CHOCDF','PROCNT','FAT','LACS','SUGAR','CAFFN') order by food.id, nutrient.tagname"

  conn = db.connect()
  result = conn.execute(query)

  nidx = get_nutrient_idx()

  rows = result.cursor.fetchall()
  
  for row in rows:
    fid = row[0]
    desc = row[1]
    group = row[2]
    nutrient = row[3]
    amount = row[4]
    gm_weight = row[5]
    gm_amount = row[6]
    serving_desc = row[7]
  
    if fid not in cache:
      cache[fid] = [fid,desc,group,serving_desc,gm_weight,0,0,0,0,0,0,0]

    cache[fid][nidx[nutrient]] = gm_amount
  
  return cache