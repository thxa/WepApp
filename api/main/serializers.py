from rest_framework import serializers
from .models import Video, Category, Season


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    season = serializers.HyperlinkedRelatedField(
        queryset=Season.objects.all(),
        view_name="season-detail",
        lookup_field="slug"
    )

    url = serializers.HyperlinkedIdentityField(
        view_name="video-detail",
        lookup_field="slug"
    )

    class Meta:
        model = Video
        fields = ('url', 'id', 'owner', 'season', 'slug',
                  'name', 'photo_url', 'video_url', 'created')
        lookup_field = 'slug'

    # extra_kwargs = {
    #     'url': {'lookup_field': 'slug'}
    # }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # videos = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    # episodes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    url = serializers.HyperlinkedIdentityField(
        view_name="category-detail",
        lookup_field="slug"
    )

    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'slug')
        lookup_field = 'slug'

        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }


# https://www.django-rest-framework.org/api-guide/relations/
class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(
        view_name="season-detail",
        lookup_field="slug"
    )

    # category = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     queryset=Category.objects.all(),
    #     view_name='category-detail',
    #     lookup_field="slug"
    # )

    # episodes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     queryset=Video.objects.all(),
    #     view_name='video-detail',
    #     lookup_field="slug"
    # )
    category = CategorySerializer(many=True, read_only=True)
    episodes = VideoSerializer(many=True)

    class Meta:
        model = Season
        fields = ('url', 'id', 'owner', 'name', 'photo_url', 'slug',
                  'number_of_episodes', 'created', 'category', 'episodes')
        lookup_field = 'slug'

        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }

        # def create(self, validated_data):
        #     videos_data = validated_data.pop('episodes')
        #     categories_data = validated_data.pop('category')
        #     season = Season.objects.create(**validated_data)
        #
        #     # Added video list
        #     for video_data in videos_data:
        #         Video.objects.create(season=season, **video_data)
        #
        #     # Added category list
        #     for category_data in categories_data:
        #         Category.objects.create(**category_data)
        #
        #     return season
        #
        # def update(self, instance, validated_data):
        #     videos_data = validated_data.pop('episodes')
        #     season = Season.objects.create(**validated_data)
        #     for video_data in videos_data:
        #         Video.objects.create(season=season, **video_data)
        #     return season
