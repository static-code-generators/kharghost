from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_view (request, post_id):
	post = get_object_or_404(Post)
	if (request.user.is_authenticated()):
		template = "blog/base_writer.html"
	else:
		template = "blog/base_reader.html"
	context = {'post' : post, 'template' : template}
	return render(request, 'blog/post_view.html', context=context)