from django.db import models
from django.contrib import admin

class SquidUser(models.Model):
	ip = models.IPAddressField(unique=True)
	name = models.CharField(max_length=64)
	enabled = models.BooleanField(default=False)
	size = models.IntegerField(default=0)


class SquidUserAdmin(admin.ModelAdmin):
	list_display = ('name', 'ip')

admin.site.register(SquidUser, SquidUserAdmin)

