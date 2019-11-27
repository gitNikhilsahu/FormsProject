from django.shortcuts import render
from WebApp import forms
# Create your views here.
def EmpView(request):
    form = forms.EmpForm()
    MyDict = {'form':form}
    return render(request, 'WebApp/Welcome.html', MyDict)