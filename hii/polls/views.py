from django.shortcuts import render,redirect
from polls.froms import UserFrom
from django.http import HttpResponse
from polls.models import User

# Create your views here.
def insert(request):
    if request.method=="POST":
        form=Userfrom(request.POST)
        if form.is_valid:
            try:
                form.save()
                return HTTpResponse("<h1>data sent to database..</h1>")
            except:
                pass
    form=UserForm()
    return render(request,'htm.html',{"form":form})

def show(request):
    users.User.objects.all()
    return render(request,'show.html',{'users':users})
def delete(request,id):
    user=User.objects.get(id==id)
    user.delet()
    return redirect('/show')

def edit(request,id):
    user.User.objects.get(id=id)
    return render(request,'edit.html',{'user':user})