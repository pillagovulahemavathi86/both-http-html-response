from django.shortcuts import render

# Create your views here.
def html1(request):
    return render(request,'html1.html')


def html2(request):
    return render(request,'html2.html')
