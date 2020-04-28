from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image


def room(request):
    a=['media/light_on.png','media/light_off.png','media/fan_on.png','media/fan_off.png']
    l=['https://cloud.boltiot.com/remote/deb60ce8-66d4-4740-a7b3-99cd47d2a015/digitalWrite?pin=1&state=HIGH&deviceName=BOLT13168172',
       'https://cloud.boltiot.com/remote/deb60ce8-66d4-4740-a7b3-99cd47d2a015/digitalWrite?pin=1&state=LOW&deviceName=BOLT13168172',
       'https://cloud.boltiot.com/remote/deb60ce8-66d4-4740-a7b3-99cd47d2a015/digitalWrite?pin=2&state=HIGH&deviceName=BOLT13168172',
       'https://cloud.boltiot.com/remote/deb60ce8-66d4-4740-a7b3-99cd47d2a015/digitalWrite?pin=2&state=OFF&deviceName=BOLT13168172']
    for i in a:
        img=Image.open(i)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(i)
    zipped=zip(l,a)
    context={
        'zipped':zipped
    }

    return render(request,'room/room.html',context)

def billing(request):
    return render(request,'room/billing.html',{'title':'biling'})
