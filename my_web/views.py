from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def index(response):
    #return HttpResponse("Czy będzie 5?")
    title_article = "Artykuły"
    articles = Article.objects.all()
    options = ["opcja1", "opcja2", "opcja3"]

    return render(response, "articles.html",
                  {
                      "title_article_view": title_article,
                      "options": options,
                      "articles": articles
                  })
def test_orm(response):
    query = Article.objects.get(id=1)
    query = Article.objects.get(id=3)
    return HttpResponse(query)