from django.shortcuts import render, redirect
from forum.models import Forum

def homepage(request):
	forum = Forum.objects.filter(approved=False)
	return render(request, 'admin.html', {'forum': forum})

def approve(request):
	if request.method == "POST":
		_id = request.POST.get('requests_id', None)

		post_forum = Forum.objects.get(id=_id)
		post_forum.approved = True
		post_forum.save()
		return redirect('admin_page')

	else:
		return HttpResponse('Request must be POST.')

def delete(request):
	if request.method == "POST":
		_id = request.POST.get('requests_id', None)

		post_forum = Forum.objects.get(id=_id)
		post_forum.delete()
		return redirect('admin_page')

	else:
		return HttpResponse('Request must be POST.')