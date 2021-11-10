from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

# Create your views here.
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): # 템플릿 : 모델명_form
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', 'tags']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser) :
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else :
            return redirect('/blog/')

class PostUpdate(LoginRequiredMixin, UpdateView): # 템플릿 : 모델명_form >> 따라서 별도로 설정해주어야 함
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', 'tags']
    template_name = 'blog/post_update_form.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class PostList(ListView):
    model = Post
    ordering = '-pk'
    #template_name = 'blog/post_list.html'   #cbv는 직접적으로 적어줄 필요는 없지만 template_name인 경우 내가 정해둔 템플릿으로 적용 가능
    # post_list.html 지동으로 연결

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
    #template_name = 'blog/post_detail.html'
    # post_detail.html 자동으로 연결


def category_page(request, slug):
    if slug == 'no_category' :
        category = '미분류'
        post_list = Post.objects.filter(category=None) #일치하는

    else:
        category = Category.objects.get(slug=slug) #카테고리 가지고 오기
        post_list = Post.objects.filter(category=category)

    return render(request, 'blog/post_list.html',
            {
                'post_list' : post_list,
                'categories' : Category.objects.all(),
                'no_category_post_count' : Post.objects.filter(category=None).count(),
                'category' : category
            }
        )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug) #카테고리 가지고 오기
    post_list = tag.post_set.all() #다대다 #Post.objects.filter(tags=tag) #다대일

    return render(request, 'blog/post_list.html',
            {
                'post_list' : post_list,
                'categories' : Category.objects.all(),
                'no_category_post_count' : Post.objects.filter(category=None).count(),
                'tag' : tag
            }
        )

'''def index(request):
    posts = Post.objects.all().order_by('-pk') # model에 저장된 post 모두 (all) 가져오기
    # .order_by('-pk') -pk 최신순 정렬
    # .order_by('pk') pk 작성순 정렬

    return render(request,'blog/post_list.html',
                  {
                      'posts' : posts,
                  }
                  )'''

'''def singel_post_page(request, pk):
    post = Post.objects.get(pk = pk) # 해당되는 pk post 가져오기

    return render(request,'blog/post_detail.html',
                  {
                      'post' : post,
                  }
                  )'''