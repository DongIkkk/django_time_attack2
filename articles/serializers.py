from rest_framework import serializers
from articles.models import Article


# 방법 1
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content']
# 이렇게 하면 결과창에 author 안나옴

# 방법 2
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
    
#     extra_kwargs = {
#         'author': {'read_only': True}
#     }

# 방법 3
# 메소드 필드로 지정해주기