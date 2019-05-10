from .models import Video, Category, Season
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):
    # season = serializers.StringRelatedField()
    season = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = Video
        fields = ('id', 'name', 'photo_url', 'url', 'season', 'created', 'slug')
        extra_kwargs = {'client': {'required': False}}
        validators = []


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'seasones')


# https://www.django-rest-framework.org/api-guide/relations/
class SeasonSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=True)
    # episodes = serializers.StringRelatedField(many=True)
    category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    # episodes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    episodes = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Season
        fields = ('id', 'name', 'slug', 'photo_url',
                  'number_of_episodes', 'created', 'category', 'episodes')