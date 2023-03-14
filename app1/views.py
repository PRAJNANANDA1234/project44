from django.shortcuts import render

# Create your views here.
def mamma(request):
    d={'name':'Geetanjali','age':46}
    return render(request,'mamma.html',context=d)