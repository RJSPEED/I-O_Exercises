import json

def req_to_json(filename):
    requirements = {}

    with open(filename) as file_object:
        for line in file_object:
            """Split the values on each line by 1st instance of =="""
            package_name, version_number = line.strip().split('==', 1)
            """Store values in requirements dictionary."""
            requirements[package_name] = version_number
            
    """Output to a new json file."""
    with open('requirements.json', 'w') as file_object:        
            json.dump(requirements, file_object, indent=2)


req_to_json("requirements.txt")