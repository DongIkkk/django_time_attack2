from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print(serializer)
            serializer.save(author=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)