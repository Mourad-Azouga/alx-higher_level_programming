#!usr/bin/python3
"""Let's define the class base"""
import json 
import csv
class Base:
    """defines the class"""
    __nb_objects = 0
    def __init__(self, id = None):
        """This method defines the base ad assigns id to it
        Args:
            id (int) = the ID"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representations of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation or list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jfile:

            if list_objs is None:
                jfile.write("[]")
            else:
                list_dici = [obj.to_dictionary() for obj in list_objs]
                jfile.write(Base.to_json_string(list_dici))
    @staticmethod
    def from_json_string(json_string):
        """This method returns a list of JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []     
        else:
            return json.loads(json_string)
        
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance  with all attributes already set:"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []