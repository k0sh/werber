from django.template import loader, Context
from django.http import HttpResponse
from mysite.werber.models import SquidUser

def squidusers(request):
	users = SquidUser.objects.all()
	t = loader.get_template("main.html")
	c = Context({'users' : users})
	return HttpResponse(t.render(c))

