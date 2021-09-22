from django.shortcuts import render
from django.http import HttpResponse
import json

bookData = open('buyer_site\EmployeeData.json').read()
data = json.loads(bookData)


def index(request):
    context = {'data': data}
    return render(request, 'buyer_site/index.html', context)
