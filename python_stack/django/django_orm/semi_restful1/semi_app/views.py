from django.shortcuts import redirect, render
from .models import Show
from django.contrib import messages

def index(request):
    return redirect('/shows')

def show(request):
    context={
        'shows': Show.objects.all(),
    }
    return render(request,'index.html',context)


def new(request):
    return render(request,'new.html')

def newrender(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        show = Show.objects.get(id = id)
        show.title = request.POST['title']
        show.Network = request.POST['Network']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Shows successfully updated")
        # redirect to a success route
        


    title=  request.POST['title']
    Network=  request.POST['Network']
    release_date = request.POST['release_date']
    desc= request.POST['desc']
    data = Show.objects.create(title=title,Network=Network,release_date=release_date,desc=desc)
    return redirect(f'/shows/{data.id}')

def view(request, data):
    context={
        'show': Show.objects.get(id=data),
    }
    return render(request,'show.html',context)

def edit(request,data):
    context={
        'show': Show.objects.get(id=data),
    }
    return render(request,'update.html',context)

def editrender(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{request.POST["hid"]}/edit')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        show = Show.objects.get(id = id)
        show.title = request.POST['title']
        show.Network = request.POST['Network']
        show.desc = request.POST['desc']
        show.save()
        messages.success(request, "Shows successfully updated")
        # redirect to a success route
        

    title=  request.POST['title']
    Network=  request.POST['Network']
    release_date = request.POST['release_date']
    desc= request.POST['desc']
    Show.objects.update(title=title,Network=Network,release_date=release_date,desc=desc)
    return redirect('/shows')

def delete(request,data):
    c = Show.objects.get(id=data)
    c.delete()
    return redirect('/shows')


