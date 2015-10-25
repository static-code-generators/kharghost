from django.shortcuts import render, get_object_or_404
from .models import Post
from markdown import markdown

# Create your views here.

def post_view (request, post_id):
	post = get_object_or_404(Post, id=post_id)
	if (request.user.is_authenticated()):
		template = "blog/base_writer.html"
	else:
		template = "blog/base_reader.html"

	if request.user.is_authenticated() and request.method == "POST":
		edit_text = request.POST['text']
		post.markdown_text = edit_text
		post.html_text = markdown(post.markdown_text)
		post.save()
	context = {'post' : post, 'template' : template}
	return render(request, 'blog/post_view.html', context=context)