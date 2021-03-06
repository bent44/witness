from django.shortcuts import render
from django.views import View
from.forms import SubmitUrlForm
from django.http import JsonResponse

# class view of home page with methods for interacting with SubmitURLForm located @ forms.py
class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {"form": the_form}
		return render(request, "home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data.get('url'))

		context = {"form": form}
		return render(request, "home.html", context)



# view of credits page
def credits_view(request, *args, **kwargs):
	
	
	return render(request, "credits.html", {})

# class view of URl page with methods for interacting with SubmitURLForm located @ forms.py
class UrlView(View):

	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {"form": the_form}
		return render(request, "url.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data.get('url'))

		context = {"form": form}
		return render(request, "url.html", context)