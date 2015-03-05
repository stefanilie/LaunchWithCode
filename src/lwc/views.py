from django.shortcuts import render


def home(request):
	context = {}
	template = "come.html"
	return render(request, template, context)