#coding=utf-8
#from django import forms
#from infor import ThumbnailImageField
from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import *
from django import forms
from django.core.files import File
import datetime
# Create your views here.

class MessageForm(forms.Form):
    outline = forms.CharField(label = '概要', max_length = 200)
    detail = forms.TextInput()
    #CharField(label = '详述', widget=forms.Textarea )
    contact = forms.CharField(label = '联系方式')
    
def leave_message(req):
    msgs = Message.objects.all()
    if msgs.count >= 3:
        msgs = msgs[0:3]
    if req.method == 'POST':
        post = req.POST
        date = datetime.date.today()
        new_msg = Message(outline = post["outline"],
        detail= post["detail"],
        contact = post["contact"],
        date = date) 
        new_msg.save()
        return render_to_response('success.html') 
    return render_to_response('message.html', {'msgs':msgs}) 
    
def home(req):
    item = ''
    items = Item.objects.all()
    photo = ''
    if items:
        item = items[0]
        photos = Photo.objects.filter(item = item)
        if photos:
            photo = photos[0]
    return render_to_response('home.html', {'item':item, 'photo':photo})

def file_download(req, name):
    filename = 'file/'+str(name)
    f = open(filename)
    data = f.read()
    f.close()
    response = HttpResponse(data,mimetype='application/octet-stream') 
    response['Content-Disposition'] = 'attachment; filename=%s' % name
    return response

def about(req):
    user = User.objects.all()
    company = ''
    company = Company.objects.all()
    content = ''
    if company:
        company = company[0]
        content = File(company.description)
    return render_to_response('about.html', {'user':user, 'file':content, 'company':company})
    
def userdetail(req, num):
    user = User.objects.filter(num__exact=num)
    return render_to_response('userdetail.html', {'user':user})

def activities(req):
    item = Item.objects.all()
    photo = []
    for i in item:
        if Photo.objects.filter(item__exact = i):
            photo.append((Photo.objects.filter(item__exact = i))[0])
    return render_to_response('items.html', {'item':item, 'photo':photo})
    
def itemdetail(req, itemdate, itemname):
    item = Item.objects.get(name__exact = itemname, date__exact = itemdate)
    photo = Photo.objects.filter(item__exact = item)
    return render_to_response('itemdetail.html', {'photo':photo, 'item':item})

def photos(req):
    photo = Photo.objects.all()
    return render_to_response('photos.html', {'photo':photo})

def show_photo(req, itemname, phototitle):
    item = Item.objects.get(name = itemname)
    photo = Photo.objects.filter(item = item, title = phototitle)
    return render_to_response('show_photo.html', {'photo':photo})
