from django.conf.urls.defaults import *
from ui.werber.views import squidusers

urlpatterns = patterns('',
	url(r'^$', squidusers),
)

