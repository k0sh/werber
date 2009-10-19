from django.conf.urls.defaults import *
from mysite.werber.views import squidusers

urlpatterns = patterns('',
	url(r'^$', squidusers),
)

