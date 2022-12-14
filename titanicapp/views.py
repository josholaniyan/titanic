from django.shortcuts import render
from django.contrib import messages


# Create your views here.
# our home page view
def home(request):    
    return render(request, 'titanicapp/index.html')


# custom method for generating predictions
def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    import pickle
    model = pickle.load(open("titanicapp/titanic_modeling.sav", "rb"))
    scaled = pickle.load(open("titanicapp/scaler.sav", "rb"))
    prediction = model.predict(scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]]))
    
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"
        

# our result page view
def result(request):
    pclass = int(request.GET['pclass'])     
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    if age>120:
        messages.error(request,'Age cannot be greater than 120')
        return render(request,'titanicapp/index.html')
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])
    result = getPredictions(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)

    return render(request, 'titanicapp/result.html', {'result':result})

def error(request):
    return render(request, 'titanicapp/error.html')
