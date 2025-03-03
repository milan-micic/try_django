from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

article_obj = Article.objects.get(id=2)
article_queryset = Article.objects.all()

context = {
  "object_list": article_queryset,
  "id": article_obj.id,
  "title": article_obj.title,
  "content": article_obj.content
}

HTML_STRING = render_to_string('home-view.html',context=context)

def home_view(request):
  return HttpResponse(HTML_STRING)