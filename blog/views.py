from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from markdown import markdown
import re
# Create your views here.

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data).replace('\n', ' ')

def post_view(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	if (request.user.is_authenticated()):
		template = "blog/writer.html"
	else:
		template = "blog/reader.html"

	if request.user.is_authenticated() and request.method == "POST":
		edit_text = request.POST['text']
		post.markdown_text = edit_text
		post.html_text = markdown(post.markdown_text, safe_mode='escape', extensions=['magic'])
		post.save()

	context = {'post' : post, 'user' : request.user}
	return render(request, template, context=context)

def index(request):
	posts = sorted(Post.objects.all(), key=lambda x: x.pub_date, reverse=True)
	summaries = []
	for post in posts:
		summary = striphtml(post.html_text)[:400]
		summaries.append(summary)
	posts_zip = list(zip(posts, summaries))
	context = {'posts' : posts_zip, 'user' : request.user}
	return render(request, 'blog/index.html', context=context)

@login_required(login_url = '/login/')
def create_post(request):
	if request.method == 'POST':
		post = Post()
		post.title = request.POST['title']
		post.author = request.user
		post.pub_date = timezone.now()
		post.markdown_text = request.POST['text']
		post.html_text = markdown(post.markdown_text, safe_mode='escape', extensions=['magic'])
		post.save()
		return HttpResponseRedirect('/posts/' + str(post.id) + '/')
	context = {'user' : request.user}
	return render(request, 'blog/create_post.html', context=context)

def login_page(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		print(user, username, password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'blog/login.html')
	return render(request, 'blog/login.html')

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')
