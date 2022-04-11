from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL 

class Dojo:
  db = "dojo_survey_schema"
  def __init__(self,data):
    self.id = data['id']
    self.name = data['name']
    self.location = data ['location']
    self.language = data['language']
    self.comment = data['comment']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
  
  @classmethod
  def create(cls,data):
    query = "INSERT into dojos (name, location, language,comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s); "
    result = connectToMySQL(cls.db).query_db(query,data)
    return result
  
  @classmethod
  def get(cls):
    query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
    result = connectToMySQL(cls.db).query_db(query)
    return Dojo(result[0])
        
  @staticmethod
  def validate (dojo):
    validate = True
    if len (dojo['name']) < 1:
      flash("Must include a name.")
      validate = False
    if len (dojo['location']) < 1:
      flash("Must choose a dojo location.")
      validate = False
    if len (dojo['language']) < 1:
      flash("Must choose a favorite language.")
      validate = False
    if len (dojo['comment']) < 1:
      flash("Must include a comment.")
      validate = False
    return validate