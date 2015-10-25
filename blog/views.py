from django.shortcuts import render, get_object_or_404
from .models import Post
from markdown import markdown

# Create your views here.

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
	context = {'post' : post}
	return render(request, template, context=context)

def index(request):
	posts = sorted(Post.objects.all(), key=lambda x: x.pub_date, reverse=True)
	context = {'posts' : posts}
	return render(request, 'blog/index.html', context=context)
