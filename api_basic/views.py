from django.shortcuts import render
from api_basic.models import Article
from api_basic.serializers import ArticleSerializer
# Package for api
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# @api_view(['GET', 'POST'])
@csrf_exempt
def Article_list(request):
    if request.method == 'GET':
        # return all record Article
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # crete Article
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def article_detail(request, pk):
    """
    Retrieve, update or delete a code Article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    method = request.method
    if method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    elif method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)

