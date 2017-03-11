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
    print ("find-----\n", request.POST['element'])
    array = request.session['baseArray']
    arrayMinIndex = 0 
    arrayMaxIndex = len(array) - 1
    arrayAveIndex = math.floor(len(array) / 2)

    arrayMins = []
    arrayMaxes = []
    found = False




    print ("array-----\n", array)
    print ("arrayMin-----\n", arrayMinIndex)
    print ("arrayMax-----\n", arrayMaxIndex)
    print ("arrayAve-----\n", arrayAveIndex)

    if len(array) == 0:
        # array has no elements
        return redirect('/')
    elif arrayMinIndex == arrayMaxIndex:
        #only one element in the array
        return redirect('/')
    elif array[arrayMaxIndex] == int(request.POST['element']):
        # max is equal to target
        return redirect('/')
    else: 
        while not found:
            if int(request.POST['element']) == array[arrayAveIndex]:
                # found
                return redirect('/')
            elif array[arrayAveIndex] < int(request.POST['element']):
                arrayMinIndex = arrayAveIndex
                #arrayMaxIndex statys the same since its the last
                arrayAveIndex = math.floor(arrayMaxIndex / arrayMinIndex)
            elif  int(request.POST['element']) < array[arrayAveIndex]:
                arrayMinIndex = arrayAveIndex
                #arrayMaxIndex statys the same since its the last
                arrayAveIndex = math.floor(arrayMaxIndex / arrayMinIndex)


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


