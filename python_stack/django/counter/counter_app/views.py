from django.http import request
from django.shortcuts import render, HttpResponse,redirect
def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    else:
        request.session['counter']+=1

    context={
        'counter': request.session['counter']
    }
    return render(request,'index.html',context)

def destroy(request):
    del request.session['counter']
    return redirect('/')