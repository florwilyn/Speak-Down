from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from forum.models import Forum


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            context['error'] = 'Invalid Username or Password'
            context['username'] = username
    return render(request, 'sign_in.html', context=context)

def sign_out(request):
    logout(request)
    return redirect('sign_in')

def homepage(request):
	forum = Forum.objects.filter(approved=False).order_by('-date')
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