#coding=utf-8
from django.db import models
from django.db.models import permalink

class Message(models.Model):
    date = models.DateField()
    outline = models.CharField(max_length = 200)
    detail = models.TextField()
    contact = models.CharField(max_length = 100, blank = True)
    
    class Meta:
        ordering = ['-date']
        
    def __unicode__(self):
        return self.outline

class Company(models.Model):
    name = models.CharField(max_length = 250)
    ceo = models.CharField(max_length = 200, blank = True)
    fax = models.CharField(max_length = 100, blank = True)
    number = models.CharField(max_length = 100)
    addr = models.CharField(max_length = 500)
    zipcode = models.CharField(max_length = 100, blank = True)
    description = models.FileField(upload_to = 'file', blank = True)
    
    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        return self.name

class User(models.Model):
    num = models.CharField(max_length = 100)
    name = models.CharField(max_length = 200)
    position = models.CharField(max_length = 250)
    email = models.EmailField(unique = True, verbose_name = 'Email')
    
    class Meta:
        ordering = ['num']
        
    def __unicode__(self):
        return self.name
    

class Item(models.Model):
    date = models.DateField()
    name = models.CharField(max_length = 250)
    description = models.TextField()
    
    class Meta:
        ordering = ['-date']
        
    def __unicode__(self):
        return u'%s %s' % (self.date, self.name)
    
    @permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': self.id})
        
class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'media/photos/%Y/%m/%d', blank = True)
    caption = models.CharField(max_length = 250, blank = True)
    
    class Meta:
        ordering = ['title']
        
    def __unicode__(self):
        return self.title
        
    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'object_id': self.id})
        


'''
from django.db import models
from django.db.models import permalink
from infor.ThumbnailImageField import ThumbnailImageField

# Create your models here.    
class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(max_length=40)

    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return self.name
    
    @permalink
    def get_absolute_url(self):
        return ('item_detail', None, {'slug': self.slug})
   
class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=40)
    
    class Meta:
        ordering = ['title']
    
    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', None, {'slug': self.slug})
        '''