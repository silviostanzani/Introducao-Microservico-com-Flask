class Employee:
    def __init__(self,firstName,lastName):
        self.__firstName = firstName
        self.__lastName = lastName

    def toJSON(self):
        #json_string = '{"first_name": 'self.__firstName', "last_name": 'self.__lastName' }'
        #json_string = '{"Employees": {'firstName': self.__firstName, 'lastName': self.__lastName}}'
        #return json_string
        return {"Employees": {'firstName': self.__firstName, 'lastName': self.__lastName}}


    def get_name(self):
        strReturn=self.__firstName + " " + self.__lastName
        return strReturn
        #return self.__firstName + " " + self.__lastName
