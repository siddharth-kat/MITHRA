import requests
import json
import pprint
x = int(input('Enter your Hall Ticket number :  '))
url = "http://teleuniv.in/netra/api.php"
attendence = json.dumps({"method": "314", "rollno": x})
data = json.dumps({"method": "32", "rollno": x})
results = json.dumps({"method": "316", "rollno": x})
responce1 = requests.post(url, attendence)
responce2 = requests.post(url, data)
responce3 = requests.post(url, results)
att = {}
dat = {}
results1 = {}
results2 = {}
dict1 = json.loads(responce1.text)
dict2 = json.loads(responce2.text)
dict3 = json.loads(responce3.text)
for i in range(len(dict1["overallattperformance"]['overall'])):
    if (dict1["overallattperformance"]['overall'][i]['percentage']) != '--':
        att[dict1["overallattperformance"]['overall'][i]['subjectname']
            ] = dict1["overallattperformance"]['overall'][i]['percentage']
    else:
        att[dict1["overallattperformance"]['overall'][i]['subjectname']
            ] = dict1["overallattperformance"]['overall'][i]['practical']
for k in dict2:
    if k in {"id", "psflag", "newlogin", "snewlogin"}:
        continue
    else:
        dat[k] = dict2[k]
for j in range(len(dict3["internalmarks"][0]["semesters"][0]["internals"][0]["theory"])):
    results1[dict3["internalmarks"][0]["semesters"][0]["internals"][0]["theory"][j]["subject"]
             ] = dict3["internalmarks"][0]["semesters"][0]["internals"][0]["theory"][j]["tot"]
for j in range(len(dict3["internalmarks"][0]["semesters"][0]["internals"][0]["labs"])):
    results1[dict3["internalmarks"][0]["semesters"][0]["internals"][0]["labs"][j]["subject"]
             ] = dict3["internalmarks"][0]["semesters"][0]["internals"][0]["labs"][j]["T"]
for j in range(len(dict3["internalmarks"][0]["semesters"][0]["internals"][1]["theory"])):
    results2[dict3["internalmarks"][0]["semesters"][0]["internals"][1]["theory"][j]["subject"]
             ] = dict3["internalmarks"][0]["semesters"][0]["internals"][1]["theory"][j]["tot"]
for j in range(len(dict3["internalmarks"][0]["semesters"][0]["internals"][1]["labs"])):
    results2[dict3["internalmarks"][0]["semesters"][0]["internals"][1]["labs"][j]["subject"]
             ] = dict3["internalmarks"][0]["semesters"][0]["internals"][1]["labs"][j]["T"]
with open('MITHRA\\attend1.json', 'a') as json_file:
    json.dump(att, json_file, indent=4)
with open('MITHRA\\data1.json', 'a') as json_file:
    json.dump(dat, json_file, indent=4)
with open('MITHRA\\results1.json', 'a') as json_file:
    json.dump(results1, json_file, indent=4)
    json.dump(results2, json_file, indent=4)
