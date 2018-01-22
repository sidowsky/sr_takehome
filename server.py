from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from constants import *
from loaders import load_cache
import mealapi


app = Flask(__name__)
api = Api(app)

cache = load_cache()

  
'''class FoodGroupAPI(Resource):
  def get(self, food_group_id):
    conn = db.connect()
    query = "select * from food_group where id = %d" % int(food_group_id)
        
    result = conn.execute(query)        
    result = {'data': [dict(zip(tuple (result.keys()) ,i)) for i in result.cursor]}
        
    return jsonify(result)

class FoodAPI(Resource):
  def get(self, food_id):
    conn = db.connect()
    query = "select * from food where id = %d" % int(food_id)
        
    result = conn.execute(query)        
    result = {'data': [dict(zip(tuple (result.keys()) ,i)) for i in result.cursor]}
        
    return jsonify(result)

class NutritionAPI(Resource):
  def get(self, food_id):
    conn = db.connect()
    query = "select * from nutrition where food_id = %d" % int(food_id)
        
    result = conn.execute(query)        
    result = {'data': [dict(zip(tuple (result.keys()) ,i)) for i in result.cursor]}
       
    return jsonify(result)

class WeightAPI(Resource):
  def get(self, food_id):
    conn = db.connect()
    query = "select * from weight where food_id = %d" % int(food_id)
        
    result = conn.execute(query)        
    result = {'data': [dict(zip(tuple (result.keys()) ,i)) for i in result.cursor]}
        
    return jsonify(result)'''

class CacheAPI(Resource):
  def get(self):
    result = cache
    
    return jsonify([result[i] for i in result.keys()])

class MealAPI(Resource):
  def get(self, calories, fat_pct, carbs_pct, protein_pct):
    #override = request.args.get('calories',None)
    #print override
    
    #if override:
    #  calories = override
    
    
    result = mealapi.build_meal(cache, float(calories), float(fat_pct), float(carbs_pct), float(protein_pct))
    
    return jsonify([result[i] for i in result.keys()])

#api.add_resource(FoodGroupAPI, '/food_group/<food_group_id>')
#api.add_resource(FoodAPI, '/food/<food_id>')
#api.add_resource(NutritionAPI, '/nutrition/<food_id>')
#api.add_resource(WeightAPI, '/weight/<food_id>')
api.add_resource(MealAPI, '/meal/<calories>/fat/<fat_pct>/carbs/<carbs_pct>/protein/<protein_pct>')
api.add_resource(CacheAPI, '/cache')


if __name__ == '__main__':
   app.run(port=5002)
   