from django.http import request
from django.shortcuts import render
    
def index(requests):
    return render(requests, "index.html")

def show(requests):
    name = requests.POST['name']
    Dojo_Location = requests.POST['Dojo_Location']
    Fav_language = requests.POST['Fav_language']
    comm = requests.POST['comm']
    context = {
        "name" : name,
        "Dojo_Location": Dojo_Location,
        "Fav_language": Fav_language,
        "comm":comm
    }
    return render(requests, "show.html",context)