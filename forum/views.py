from django.shortcuts import render
from django.shortcuts import render, redirect

def homepage(request):
	return render(request, 'home.html')

def send(request):
	if request.method == "POST":
		title = request.POST.get('title', None)
		content = request.POST.get('content', None)
		codename = request.POST.get('codename', None)

		forum = Forum(title=title, content=content, user=codename)
		forum.save()
		return render(request, 'home.html')

	else:
		return HttpResponse('Request must be POST.')