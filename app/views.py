from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':100,'b':200,'c':2000}
    return render(request,'conditions.html',context=d)


def conditions_for_loop(request):
    d={'name':'ASHU'}
    return render(request,'conditions_for_loop.html',context=d)
