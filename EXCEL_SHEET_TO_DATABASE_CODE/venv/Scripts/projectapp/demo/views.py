from django.shortcuts import render
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
# Create your views here.
def  home(request):
    return render(request, 'dashboard.html')
"""
def simple_upload(request):
    if request.method == "POST":
        person_resources = PersonResource()
        dataset = Dataset()
        new_person = request.Files['myfiles']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, "Please upload a valid xlsx file")
            return render(request,'dashboard.html')
        

        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            value = Person(
                data[0],
                data[1],
                data[2],
                data[3]
            )
            value.save()

        return render(request,'dashboard.html')    
        

"""
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from tablib import Dataset
from .resources import PersonResource
from .models import Person

def simple_upload(request):
    if request.method == "POST":
        person_resource = PersonResource()
        dataset = Dataset()

        new_person = request.FILES.get('myfiles')

        if not new_person.name.endswith('xlsx'):
            messages.info(request, "Please upload a valid xlsx file")
            return render(request, 'dashboard.html')

        # Load data from Excel file
        imported_data = dataset.load(new_person.read(), format='xlsx')

        # Loop through each row in the imported data
        for row in imported_data:
            # Assuming the first row contains headers, so skipping it
            if row[0] == 'name':
                continue
            
            # Create a new Person object using data from the current row
            person = Person(
                name=row[0],
                email=row[1],
                location=row[2]
            )
            # Save the Person object to the database
            person.save()

        messages.success(request, "Data uploaded successfully")
        return render(request, 'dashboard.html')
    else:
        # Handle other HTTP methods such as GET
        return HttpResponse("Unsupported method")
