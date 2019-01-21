import json
import urllib.request
from pprint import pprint

contents = urllib.request.urlopen("http://localhost:5000/getEmployeeList").read()

#parsed_json = json.loads(contents)
#pprint (parsed_json)
#print ( parsed_json[0] )
#print ( parsed_json[2:4] )

my_dict = json.loads(contents)
type(my_dict)
print ( my_dict[:3] )
print ( my_dict[1] )
dict = my_dict[1]

#print ( "dict['first_name']: ", dict['first_name'] )

my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

#print("list values: %s" % my_dict["Employees"])

#apod_dict = json.loads(contents)
#print(apod_dict[0].first_name)

#emp=parsed_json[0]
#print (emp)
#print (emp[first_name])

#class Test(object):
#    def __init__(self, data):
        #contents = urllib.request.urlopen("http://localhost:5000/getEmployeeList").read()
        #parsed_json = json.loads(contents)
#	    self.__dict__ = json.loads(data)

#contents = urllib.request.urlopen("http://localhost:5000/getEmployeeList").read()
#test1 = Test(contents)
#print(test1.first_name)
#resp = parsed_json.json()
#print (resp['Employees'])
#print resp['headers']['Host']
#Employee = parsed_json[0]
#print( Employee.get_name() )
#print(parsed_json[0].['first_name'])
