from django.shortcuts import render

from django.http import HttpResponse, Http404

from .models import Course

import csv


#from django.contrib.auth.decorators import login_required

# Create your views here.

def coursesIndex(request):
    return HttpResponse("Oi")


improve a little the search stuff and add the rest of the material

#Debug view to get request ip
def getIp(request):

    response = 'HTTP_X_FORWARDED_FOR: ' + str(request.META.get('HTTP_X_FORWARDED_FOR'))
    response += "<br><br>"
    response += 'REMOTE_ADDR: ' + str(request.META.get('REMOTE_ADDR'))

    return HttpResponse(response)


def searchCourses(request):

    #If there is no query in search and it is valid, just return the search modal
    if not "q" in request.GET or not request.GET['q']:
        return render(request, "searchCourses.html", {
            'noSearch': True
        })

    #If there is a query, get the titles that contains the query (case insensitive)
    return render(request, "searchCourses.html", {
        'results': Course.objects.filter(title__icontains=request.GET['q'])
    })



def loadCourses(request):
    if not request.user.is_superuser:
        raise Http404

    if request.method == "GET":
        return render(request, "loadCourses.html")


    #Read gotten file in case it is not get method 
    if not "course_file" in request.FILES:
        return HttpResponse("No file sent.")


    #Load upload file as string
    courseData = request.FILES["course_file"].read().decode('utf-8', 'replace')

    #return HttpResponse(courseData)

    #Load data in a csv module
    csvData = csv.reader(courseData.split("\n"))

    # return render(request, "coursesDebug.html", {
    #      'courses': csvData
    # })

    #Iterate thru csv data and create courses
    #Create artifact to skip the first line (header)
    itercsv = iter(csvData)
    next(itercsv)


    #Iterate thru the rows data
    for row in itercsv:
        #Try to create new course 
        try:
            newCourse = Course(title=row[0], description=row[1], url=row[2], thumbnailUrl=row[3], level=row[4])
            newCourse.save()
        except Exception as e:
            print(e)


    return HttpResponse("Done")

    # return render(request, "coursesDebug.html", {
    #     'courses': csvData
    # })


    # for row in csvData:
    #     responseData += " ".join(row) + "<br><br>"

    #keep working on csv data

# ...         print ', '.join(row)

#     for row in courseData.split("\n"):
#         responseData += row + "<br><br>"
        #for rowElem in row.split(","):
            #responseData += rowElem + "<br><br>"

        
    #responseData = courseData.split("\n").join("<br><br>")


    #print(len(courseData.split("\n")))

    # responseData = courseData.split("\n")

    # print(responseData)

    # reader = csv.DictReader(request.FILES["course_file"])
    # for row in reader:
    #     print(row)


    #courseData = request.FILES["course_file"].read()

    #csvData = csv.reader(request.FILES["course_file"])

    #for row in csvData:
        #print(row)

    #print(courseData)


    return HttpResponse(responseData)

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
