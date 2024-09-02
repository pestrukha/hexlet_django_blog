from django.shortcuts import render, get_object_or_404
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from .models import Article
from .forms import ArticleForm


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('articles') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class HomeRedirectView(View):
    def get(self, request, *args, **kwargs):
        # Используем reverse для получения URL по имени маршрута
        target_url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        return redirect(target_url)


# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         # Получаем параметры из URL
#         tags = kwargs.get('tags', '')
#         article_id = kwargs.get('article_id', '')
#
#         # Формируем текст для отображения
#         display_text = f"Статья номер {article_id}. Тег {tags}"
#
#         # Контекст с названием приложения и текстом
#         context = {
#             'app_name': 'Hexlet Django Blog',
#             'display_text': display_text,
#         }
#         # Используем шаблон templates/articles/index.html
#         return render(request, 'articles/index.html', context)
