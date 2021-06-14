from django.shortcuts import redirect, render
import random
from datetime import datetime
def index(request):
    
    gold= request.session['gold']
    text= request.session['text']
    context ={
        'gold': request.session['gold'],
        'text': request.session['text']
    }
    return render(request, "index.html", context)

def index2(request):
    if request.POST['forms'] == "farm": 
        num=random.randint(10,20)
        request.session['gold'] += num
        request.session["text"].append(f"Earned {num} from the Farm!"+'(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        print(request.session['gold'])
        
    if request.POST['forms'] == "cave": 
        num=random.randint(5,10)
        request.session['gold'] += num
        request.session["text"].append(f"Earned {num} from the cave!"+'(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        print(request.session['gold'])

    if request.POST['forms'] == "house": 
        num=random.randint(2,5)
        request.session['gold'] += num
        request.session["text"].append(f"Earned {num} from the house!"+'(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        print(request.session['gold'])

    if request.POST['forms'] == "casino":         
        num=random.randint(-50,50)
        request.session['gold'] += num
        request.session["text"].append(f"Earned {num} from the casino!"+'(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        print(request.session['gold'])
    return redirect('/')

