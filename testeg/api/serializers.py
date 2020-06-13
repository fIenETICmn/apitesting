from rest_framework import serializers
from testeg.models import User,Category, Product

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('author','name','price','detail_text','published_date', 'category',)
