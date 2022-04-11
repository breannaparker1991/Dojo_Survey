from unittest import result
from wsgiref import validate
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
    
  @staticmethod
  def validate (dojo_survey):
    validate = True
    if len (dojo_survey['name']) < 1:
      flash("Must include a name.")
      validate = False
    if len (dojo_survey['location']) < 1:
      flash("Must choose a dojo location.")
      validate = False
    if len (dojo_survey['language']) < 1:
      flash("Must choose a favorite language.")
      validate = False
    if len (dojo_survey['comment']) < 1:
      flash("Must include a comment.")
      validate = False
    return validate