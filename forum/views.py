from django.shortcuts import render
<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Forum

def homepage(request):
	forum = Forum.objects.all();
	return render(request, 'home.html', {'forum': forum})

def send(request):
	if request.method == "POST":
		title = request.POST.get('title', None)
		content = request.POST.get('content', None)
		codename = request.POST.get('codename', None)

		forum = Forum(title=title, content=content, user=codename)
		forum.save()
		return redirect('/')

	else:
		return HttpResponse('Request must be POST.')
=======

def homepage(request):
	return render(request, 'home.html')

>>>>>>> 6f8334cd8230b93795afd270e036cf1a5c373ed9
