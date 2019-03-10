from django.shortcuts import render
from blog.models import Blog, Comment, Author, User
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site"""

    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.count()
    num_users = User.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
        'num_users': num_users,
    }

    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog