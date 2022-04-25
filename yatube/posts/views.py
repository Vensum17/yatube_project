from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, any_str):
    return HttpResponse(f'Здесь будут посты, отфильтрованные по группам '
                        f'Ваш текст ссылки: {any_str}')