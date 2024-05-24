from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomPasswordChangeForm


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == "POST":
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
    # A backend authenticated the credentials
            return redirect("/")
        else:
         # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


def about(request):

    return render(request, 'about.html')


def attendance(request):
    import requests
    import json
    # import pprint
    x = request.user.username
    url = "http://teleuniv.in/netra/api.php"

    # {'subjectname': 'PPS_LAB', 'percentage': '--', 'practical': 71.05, 'colorcode1': None, 'colorcode2': '#dd8732'}
    # response = requests.get(url)
    data = json.dumps({"method": "314", "rollno": x})
    res = requests.post(url, data)

    d1 = {}
    d2 = {}
    k = 0
    dictionary = json.loads(res.text)
    for i in range(len(dictionary["overallattperformance"]['overall'])):
        if k < 10:
            if (dictionary["overallattperformance"]['overall'][i]['percentage']) != '--':
                d1[dictionary["overallattperformance"]['overall'][i]['subjectname']
                   ] = dictionary["overallattperformance"]['overall'][i]['percentage']
            else:
                d1[dictionary["overallattperformance"]['overall'][i]['subjectname']
                   ] = dictionary["overallattperformance"]['overall'][i]['practical']
        if k >= 10:
            if (dictionary["overallattperformance"]['overall'][i]['percentage']) != '--':
                d2[dictionary["overallattperformance"]['overall'][i]['subjectname']
                   ] = dictionary["overallattperformance"]['overall'][i]['percentage']
            else:
                d2[dictionary["overallattperformance"]['overall'][i]['subjectname']
                   ] = dictionary["overallattperformance"]['overall'][i]['practical']
        k += 1
    return render(request,'attendance.html', {'d1': d1,'d2': d2})


def data(request):
    import requests
    import json
    username = request.user.username
    url = "http://teleuniv.in/netra/api.php"
    data = json.dumps({"method": "32", "rollno": username})
    responce2 = requests.post(url, data)
    dat = {}
    dict2 = json.loads(responce2.text)
    for k in dict2:
        if k in {"id", "psflag", "newlogin", "snewlogin",'parentemail','email','picture'}:
            continue
        else:
            dat[k] = dict2[k]
    return render(request, 'data.html',{'dat':dat,
                                        'data1':dict2
                                        })


def results(request):
    import requests
    import json
    import pprint
    username = request.user.username
    url = "http://teleuniv.in/netra/api.php"

    results = json.dumps({"method": "316", "rollno": username})
    responce3 = requests.post(url, results)
    results1 = {}
    results2 = {}
    dict3 = json.loads(responce3.text)
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
    a = json.dumps(results1, indent=4)
    b = json.dumps(results2, indent=4)
    c = a+b
    return render(request, 'results.html', {
        'results1': results1,
        'results2': results2
        
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        contact = Contact(name=name, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your form has been Submitted")
    return render(request, 'contact.html')


def timetable(request):
    import requests
    import json
    import pprint
    username = request.user.username
    url="http://teleuniv.in/netra/api.php"
    timetable = json.dumps({"method": "317", "rollno": username})
    res = requests.post(url, timetable)

    # Parse the JSON data into a dictionary
    data = json.loads(res.text)


    timetables = {}

    # Loop through the timetable and store each day's timetable in the dictionary
    for day in data['timetable']:
        day_name = day['dayname']
        before_lunch = day['beforelunch']
        lunch = day['lunch']
        after_lunch = day['afterlunch']
        
        # Remove the 'uiflag' field from each subject in the timetable
        before_lunch = [{k: v for k, v in subject.items() if k != 'uiflag'} for subject in before_lunch]
        after_lunch = [{k: v for k, v in subject.items() if k != 'uiflag'} for subject in after_lunch]
        
        # Create a list for the subjects on the current day
        subjects_on_day = []
        
        # Add subjects to the list for before lunch schedule
        for subject in before_lunch:
            subjects_on_day.append(subject['subject'])
        
        # Add lunch break to the list
   
        
        # Add subjects to the list for after lunch schedule
        for subject in after_lunch:
            subjects_on_day.append(subject['subject'])
        
        # Store the list of subjects in the dictionary with the day name as the key
        timetables[day_name] = subjects_on_day
    print(timetables['Monday'])
    return render(request, 'timetable.html',{'tt':timetables})
def rules(request):

    return render(request, 'rules.html')
def todo(request):
    return render(request, 'todo.html')



def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changepassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {'form': form})
