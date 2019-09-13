from rest_framework import serializers
from .models import Video, Category, Season


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
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
        # 'owner', 'id',

        fields = ('url', 'season', 'slug',
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
    # owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(
        view_name="season-detail",
        lookup_field="slug"
    )

    # category = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     queryset=Category.objects.all(),
    #     view_name='category-detail',
    #     lookup_field="slug",
    # )

    # episodes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     queryset=Video.objects.all(),
    #     view_name='video-detail',
    #     lookup_field="slug"
    # )

    category = CategorySerializer(many=True)
    episodes = VideoSerializer(many=True)

    class Meta:
        model = Season
        # 'owner', 'id',
        fields = ('url', 'name', 'photo_url', 'slug',
                  'number_of_episodes', 'created', 'category', 'episodes')
        lookup_field = 'slug'

        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }

    def create(self, validated_data):
        categories_data = validated_data.pop('category')

        videos_data = validated_data.pop('episodes')
        season = Season.objects.create(**validated_data)

        # Added video list
        # owner = request.user,
        for video_data in videos_data:
            Video.objects.create(season=season, **video_data)

        # Added category list
        for category_data in categories_data:
            Category.set(category_data)
            # Category.objects.create(**category_data)

        return season

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.photo_url = validated_data.get('photo_url', instance.photo_url)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.season = validated_data.get('season', instance.season)
        instance.number_of_episodes = validated_data.get('number_of_episodes', instance.number_of_episodes)
        instance.category = validated_data.get('category', instance.category)
        instance.episodes = validated_data.get('episodes', instance.episodes)

        # videos_data = validated_data.pop('episodes')
        videos_data = instance.episodes
        # categories_data = validated_data.pop('category')

        # Updated video list
        for video_data in videos_data:
            Video.objects.create(season=instance.season, **video_data)

        # Updated category list
        # for category_data in categories_data:
        #     Category.objects.update(**category_data)

        instance.save(owner=request.user)
        return instance
