from django.shortcuts import render, HttpResponse, redirect
def stdata(request): 
    import requests
    import json
    username = request.user.username
    url = "http://teleuniv.in/netra/api.php"
    data = json.dumps({"method": "32", "rollno": username})
    responce2 = requests.post(url, data)
    dat = {}
    dict2 = json.loads(responce2.text)
    for k in dict2:
        if k in {"id", "psflag", "newlogin", "snewlogin"}:
            continue
        else:
            dat[k] = dict2[k]
    return({"dat":dat})