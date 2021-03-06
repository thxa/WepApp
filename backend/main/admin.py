from django.contrib import admin
from .models import Video, Category, Season


class InLineVideo(admin.TabularInline):
    model = Video
    extra = 1


class SeasonAdmin(admin.ModelAdmin):
     inlines = [InLineVideo]
     # fields = ()#'id', 'name', 'slug', 'created', 'episodes')
     search_fields = ('name', 'slug')
     list_display = ('name', 'slug', 'created')#, 'category')
     list_display_links = ()
     list_filter = ('name', 'slug', 'created', 'category')


class VideoAdmin(admin.ModelAdmin):
     search_fields = ('name', 'slug')
     # fields = ()#'id', 'name', 'slug', 'created', 'episodes')
     list_display = ('name', 'slug', 'created')
     list_display_links = ()
     list_filter = ('name', 'slug', 'created')


class CategoryAdmin(admin.ModelAdmin):
     search_fields = ('name', 'slug')
     # fields = ()#'id', 'name', 'slug', 'created', 'episodes')
     # list_display = ('name', 'slug', 'created')
     list_display_links = ()
     # list_filter = ('name', 'slug', 'created')


admin.site.register(Season, SeasonAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Category, CategoryAdmin)
