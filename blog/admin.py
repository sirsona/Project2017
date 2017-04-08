from django.contrib import admin


# Register your models here.
from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	"""docstring for SignUpForm"""
	list_display = ["__str__","timestamp","updated"]
	form = SignUpForm
	# class Meta :
	# 	model = SignUp
	# 	form = ["first_name","last_name","email"]
	# # def __init__(self, arg):
	# 	super(SignUpForm, self).__init__()
		
admin.site.register(SignUp,SignUpAdmin)
# admin.site.register(Album)