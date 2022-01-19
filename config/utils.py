import json
import random


def get_from_json(json_response, field_name, property_name):
    content = str(json_response)
    content = content.replace("' ", ' ')
    content = content.replace("'s ", 's ')
    content = content.replace("'", '"')
    decoded_response = json.loads(content)
    field_property = decoded_response[property_name]
    field_text = field_property[field_name]
    return field_text


def get_from_json_specific_field(json_response, property_name):
    content = str(json_response)
    content = content.replace("' ", ' ')
    content = content.replace("'s ", 's ')
    content = content.replace("'", '"')
    decoded_response = json.loads(content)
    field_property = decoded_response[property_name][0]
    return field_property


def get_random_number(param):
    return str(random.randint(1, param))
