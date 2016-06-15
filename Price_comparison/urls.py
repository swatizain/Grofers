from django.conf.urls import patterns, include
from compare.views import *
from django.contrib import admin
urlpatterns = patterns('',
		       (r'^admin/', include(admin.site.urls)),
			   (r'^compare/', include('compare.urls')),
		       )
	