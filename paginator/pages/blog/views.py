from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    # Обработка выбранного количества элементов на странице
    page_size = request.GET.get('page_size', 5)
    paginator = Paginator(posts, page_size)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})