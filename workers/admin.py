from django.contrib import admin
from .models import Worker

class WorkerAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'hire_date',)
	list_display_links = ('id', 'name',)
	search_fields = ('name',)
	list_per_page = 25

# Register your models here.
admin.site.register(Worker, WorkerAdmin)
