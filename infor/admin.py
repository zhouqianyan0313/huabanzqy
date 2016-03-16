from django.contrib import admin 
from models import *

class CompanyAdmin(admin.StackedInline):
    model = Company

class UserAdmin(admin.StackedInline):
    model = User
    
class MessageAdmin(admin.StackedInline):
    model = Message

class PhotoInline(admin.StackedInline):
    model = Photo
    
class ItemAdmin(admin.ModelAdmin):
    inline = [PhotoInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Company)