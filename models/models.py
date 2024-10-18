from app import db
from sqlalchemy import Enum
import enum


class Level(enum.Enum):
    LEVEL_100 = '100'
    LEVEL_200 = '200'
    LEVEL_300= '300'
    LEVEL_400 = '400'
    LEVEL_500 = '500'

class Unit(enum.Enum):
    pass#When I get the list for units in church'

class Attendee(db.Model):
    id = db.Column(db.Integer,primary_key = True,unique=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    department = db.Column(db.String(40))
    address = db.Column(db.String(80))
    unit_in_church = db.Column(db.String(40))
    first_time = db.Column(db.Boolean())
    member = db.Column(db.Boolean())
    level = db.Column(Enum(Level))

    def __init__(self,first_name,last_name,department,address,unit_in_church,first_time,member,level):
        self.first_name = first_name
        self.last_name  = last_name
        self.department = department
        self.address = address
        self.unit_in_church = unit_in_church
        self.first_time = first_time
        self.member = member
        self.level = level
