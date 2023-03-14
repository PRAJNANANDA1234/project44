from django.shortcuts import render

# Create your views here.
def papaa(request):
    d={'name':'Pramod','age':54}
    return render(request,'mamma.html',context=d)