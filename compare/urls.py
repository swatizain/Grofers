from django.conf.urls import patterns, include
from compare.views import *
urlpatterns = patterns('compare',
		       (r'index', index),
		       (r'add-to-db', add_to_db),
		       )
