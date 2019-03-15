from main.models import Video, Category, Season
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'name', 'photo_url', 'url', 'season', 'created', 'slug')


    def create(self, validated_data):
        """
        Create and return a new `Video` instance, given the validated data.
        """
        return Video.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Video` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.photo_url = validated_data.get('photo_url', instance.photo_url)
        instance.url = validated_data.get('url', instance.url)
        instance.category = validated_data.get('category', instance.category)
        instance.season = validated_data.get('season', instance.season)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'seasones')


class SeasonSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=True)
    # episodes = serializers.StringRelatedField(many=True)
    category = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    episodes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Season
        fields = ('id', 'name', 'slug', 'photo_url', 'created', 'category', 'episodes')
