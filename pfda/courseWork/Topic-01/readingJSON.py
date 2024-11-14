# Reading JSON Object
# Author Sarabjeet 


import json


data ={
    'name':'Sarab',
     'age' : 21,
     "student" : True
}

# reading as a JSON object
jsonString = json.dumps(data)

print(data)

#printing JSON objext
print(jsonString)