from django.shortcuts import render, HttpResponse, redirect

import math

# Create your views here.

def index(request):
    if 'baseArray' in request.session:
        baseArray = request.session['baseArray']
    else:
        baseArray = []
    data = {
            'baseArray': baseArray,
            'haha': 20 
            }
    return render(request, 'binarySearch/index.html', data)

def findElement(request):
    print ("find-----\n", request.POST)
    array = request.session['baseArray']
    arrayMinIndex = 0 
    arrayMaxIndex = len(array) - 1
    arrayAveIndex = math.floor(len(array) / 2)

    arrayMins = []
    arrayMaxes = []


    print ("array-----\n", array)
    print ("arrayMin-----\n", arrayMinIndex)
    print ("arrayMax-----\n", arrayMaxIndex)
    print ("arrayAve-----\n", arrayAveIndex)
    return redirect('/')

def setArray(request):
    tempArray = []
    if request.method == "POST":
        for count in range(0, int(request.POST['baseArray'])):
            tempArray.append(count)
    request.session['baseArray'] = tempArray
    return redirect('/')

def resetArray(request):
    del request.session['baseArray']
    return redirect('/')


