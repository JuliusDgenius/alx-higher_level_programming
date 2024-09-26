import json

data = '''
{
	"people": [
		{
			"name": "David",
			"age": 20,
			"job": "student"
		},
		{
			"name": "Donald",
			"age": 25,
			"job": "Doctor"
		},
		{
			"name": "Drake",
			"age": 30,
			"job": "Lecturer"
		}
	]
}
'''

print(help(json.load))
