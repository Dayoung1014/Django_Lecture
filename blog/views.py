from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    #template_name = 'blog/post_list.html'   #cbv는 직접적으로 적어줄 필요는 없지만 template_name인 경우 내가 정해둔 템플릿으로 적용 가능
    # post_list.html 지동으로 연결

class PostDetail(DetailView):
    model = Post
    #template_name = 'blog/post_detail.html'
    # post_detail.html 자동으로 연결

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