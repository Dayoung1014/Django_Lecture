from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk') # model에 저장된 post 모두 (all) 가져오기
    # .order_by('-pk') -pk 최신순 정렬
    # .order_by('pk') -pk 작성순 정렬

    return render(request,'blog/index.html',
                  {
                      'posts' : posts,
                  }
                  )

def singel_post_page(request, pk):
    post = Post.objects.get(pk = pk) # 해당되는 pk post 가져오기

    return render(request,'blog/singel_post_page.html',
                  {
                      'post' : post,
                  }
                  )