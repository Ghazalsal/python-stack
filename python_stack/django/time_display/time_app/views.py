from django.shortcuts import render
from time import gmtime, localtime, strftime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request,'index.html', context)
