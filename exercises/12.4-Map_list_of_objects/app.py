import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age #birthDate

name_list = list(map(lambda person: "Hello, my name is " + person["name"] + " and I am " + str(calculateAge(person["birthDate"])) + " years old"  , people))
#name_list = list(map(lambda person:  person["name"] , people))
#age_list = list(map(lambda age: age["birthDate"], people))
#result = list(map(calculateAge,age_list))
#for i in range(0,len(name_list)):
#	print('Hello, my name is ' + name_list[i] +' and I am ' + str(result[i]) +' years old') 
	#tiene que ser con rango para matchear los index de name y age
print(name_list)

