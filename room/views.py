from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from PIL import Image
from users.models import Account

def billing(request):
    return render(request,'room/billing.html',{'title':'biling'})

def newroom(request):
    if request.user.is_authenticated:
        a=[]
        l=[]
        fs=request.user.fs
        ls=request.user.ls
        if fs==True:
            a.append('media/fan_on.png')
            l.append('set_fan')
        else:
            a.append('media/fan_off.png')
            l.append('set_fan')
        if ls==True:
            a.append('media/light_on.png')
            l.append('set_light')
        else:
            a.append('media/light_off.png')
            l.append('set_light')
        for i in a:
            img=Image.open(i)
            if img.height>100 or img.width>100:
                output_size=(100,100)
                img.thumbnail(output_size)
                img.save(i)
        zipped=zip(l,a)
        context={
            'images':zipped
        }
        return render(request,'room/room.html',context)
    else:
        return render(request,'room/room.html')

def set_fan(request):
    if (request.user.fs == True):
        request.user.fs=False
        request.user.save()
    else:
        request.user.fs=True
        request.user.save()
    return redirect('newroom')

def set_light(request):
    if (request.user.ls == True):
        request.user.ls=False
        request.user.save()
    else:
        request.user.ls=True
        request.user.save()
    return redirect('newroom')

