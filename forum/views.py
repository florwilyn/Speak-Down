from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Forum
from .models import Comment

def homepage(request):
	forum = Forum.objects.filter(approved=True).order_by('-date')
	comment = Comment.objects.all().order_by('-date')
	return render(request, 'home.html', {'forum': forum, 'comment': comment})

def send(request):
	if request.method == "POST":
		title = request.POST.get('title', None)
		content = request.POST.get('content', None)
		codename = request.POST.get('codename', None)
		image = request.FILES.get('myfile', None)

		if codename != '':
			forum = Forum(title=title, content=content, user=codename, image=image)
		else: 
			forum = Forum(title=title, content=content, image=image)
		forum.save()
		return redirect('/')

	else:
		return HttpResponse('Request must be POST.')

# def login():
# 	login(user,)