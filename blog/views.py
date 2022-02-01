from django.shortcuts import render,get_object_or_404 # this import standard with django
from .models import Post,Comment
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import CommentForm

# Create your views here.
def home(request):
    context = {
        'title':'Home'
    }
    return render(request,'blog/home.html',context)

def about(request):
    context = {
        'title':'About'
    }
    return render(request,'blog/about.html',context)

def newpost(request):
    context = {
        'title':'New Post'
    }
    return render(request,'blog/newpost.html',context)

#def blog(request):
#    context = {
#        'posts':Post.objects.all()
#    }
#    return render(request,'blog/blog.html',context)

# here we are going to make a 'class view' that will render a page that allows user to CRUD posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # ordering posts from newest to oldest
    paginate_by = 5

# here we are creating a class view that will display only the posts made by a certain user when 
# their name is clicked on the main page
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5
    #ordering = ['-date_posted'] # because we are overriding this class view with the get_query_set below, that means
                                 # that the ordering will be overridden too. We have to specify the ordering using
                                 # 'order by' in the query set below
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        posts = Post.objects.filter(author=user).order_by('-date_posted')
        return posts


#class PostDetailView(DetailView):
#    model = Post
#    template_name ='blog/post_details.html'

def PostDetailView(request,pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_details.html', context)

'''
class PostDetailView(DetailView):
    model = Post
    template_name ='blog/post_details.html'
    context_object_name='post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(id=self.pk)
        num_comments = Comment.objects.filter(=eachProduct).count()
        return context

    # here we are querying all the comments associated with a post object, then forwarding that query set to the template
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(post=self.get_object()).order_by('-date_posted')
        data['comments'] = comments
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(author=self.request.user,Post=self.get_object(),content=request.POST.get('content'))
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
'''

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    # this form_valid function sets the author of the updated post to be the current logged in user
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # this test_func function checks to make that the current logged in user is the author of a post before allowing to update
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    
    # this test_func function checks to make that the current logged in user is the author of a post before allowing to update
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name ='blog/add_comment.html'
    fields = ['content']

    '''Big issue here with submitting the new comment!'''
    def form_valid(self,form):
        form.instance.post_id = self.kwargs.get('id')
        return super().form_valid(form)