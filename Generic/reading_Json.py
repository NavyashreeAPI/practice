from json import *

def read_json_locator():
    file=open("../Excel/Locator.json")
    data=load(file)
    return data