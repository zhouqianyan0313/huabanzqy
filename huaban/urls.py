#coding=utf-8
from django.conf.urls.defaults import * 
from infor import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
# Include these import statements... from django.contrib import admin admin.autodiscover()
# And include this URLpattern... 
urlpatterns = patterns('',
    url('^$', views.home),
    url('^about/$', views.about),
    url('^userdetail/([^/]+)/$', views.userdetail),
    url('^activities/$', views.activities),
    url('^item/([^/]+)/([^/]+)/$', views.itemdetail),
    url('^download/file/([^/]+)/$', views.file_download),
    url('^message/$', views.leave_message),
    #url('^add_photo/$', views.add_photo),
    url('^show_photo/([^/]+)/([^/]+)/$', views.show_photo, name = 'See The Photo'),
    
    url('^photos/$', views.photos, name = 'All The Photos'),
)

urlpatterns += patterns('',    
    (r'^admin/', include(admin.site.urls)),
    (r'^media/photos/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.PHOTO_PATH}),
)
