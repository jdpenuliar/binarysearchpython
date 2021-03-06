from django.shortcuts import render, HttpResponse, redirect
import math

# Create your views here.
def index(request):
    if 'baseArray' in request.session:
        baseArray = request.session['baseArray']
    else:
        baseArray = []

    if 'stepsArray' in request.session:
        stepsArray = request.session['stepsArray']
    else:
        stepsArray = []

    if 'maxNumGuesses' in request.session:
        maxNumGuesses = request.session['maxNumGuesses']
    else:
        maxNumGuesses = 'no array yet' 
        
    if 'numGuesses' in request.session:
        numGuesses = request.session['numGuesses']
    else:
        numGuesses = 'no array yet'

    data = {
            'baseArray': baseArray,
            'stepsArray': stepsArray,
            'maxNumGuesses': maxNumGuesses,
            'numGuesses': numGuesses,
            }
    return render(request, 'binarySearch/index.html', data)

def findElement(request):

    if 'baseArray' not in request.session:
        return redirect("/")

    array = request.session['baseArray']
    arrayMinIndex = 0 
    arrayMaxIndex = len(array) - 1
    arrayAveIndex = math.floor(len(array) / 2)
    found = False
    stepsArray = [
            {
                "minIndex": arrayMinIndex,
                "maxIndex": arrayMaxIndex,
                "aveIndex": arrayAveIndex,
                }
            ]
    count = 0
    if len(array) == 0:
        # array has no elements
        print ("first try---\n")
    elif arrayMinIndex == arrayMaxIndex:
        #only one element in the array
        print ("one element---\n")

    elif arrayMaxIndex < arrayMinIndex:
        print ("element is not present")
    else: 
        while found == False:
            count += 1
            if int(request.POST['element']) == array[arrayAveIndex]:
                found = True
                request.session['stepsArray'] = stepsArray
                request.session['numGuesses'] = count
                break;
            elif array[arrayMaxIndex] == int(request.POST['element']):
                # max is equal to value of current array of max index 
                print ("max element---\n")
            elif array[arrayMinIndex] == int(request.POST['element']):
                # max is equal to array of of min index 
                print ("min element---\n")
            elif int(request.POST['element']) < array[arrayAveIndex]:
                arrayMaxIndex = arrayAveIndex
            elif int(request.POST['element']) > array[arrayAveIndex]:
                arrayMinIndex = arrayAveIndex
            arrayAveIndex = math.floor((arrayMaxIndex + arrayMinIndex) / 2)
            stepsArray.append(
                    {
                        "minIndex": arrayMinIndex,
                        "maxIndex": arrayMaxIndex,
                        "aveIndex": arrayAveIndex,
                        }
                    )
        else:
            print ("done---\n")
    return redirect('/')

def setArray(request):
    tempArray = []
    if request.method == "POST":
        for count in range(0, int(request.POST['baseArray'])):
            tempArray.append(count)
        request.session['baseArray'] = tempArray
        ''' 
        x = math.ceil(math.log2(len(tempArray)))
        print ("x---\n", x)
        if x % 2 == 0:
            request.session['maxNumGuesses'] = x + 1
        else:
            request.session['maxNumGuesses'] = x + 2
        '''
        request.session['maxNumGuesses'] = math.ceil(math.log2(len(tempArray))) + 1
    return redirect('/')

def resetArray(request):
    if 'baseArray' in request.session:
        del request.session['baseArray']

    if 'stepsArray' in request.session:
        del request.session['stepsArray']

    if 'maxNumGuesses' in request.session:
        del request.session['maxNumGuesses']

    if 'numGuesses' in request.session:
        del request.session['numGuesses']

    return redirect('/')
