from django.db import models
from django.contrib import admin

class SquidUser(models.Model):
	name = models.CharField(max_length=64)
	ip = models.CharField(max_length=16, unique=True)
	enabled = models.BooleanField(default=True)
	size = models.IntegerField(default=0)


class SquidUserAdmin(admin.ModelAdmin):
	list_display = ('name', 'ip')

admin.site.register(SquidUser, SquidUserAdmin)

