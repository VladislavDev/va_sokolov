from django.contrib import admin

from .models import Feed, FeedImage

class FeedImageInline(admin.StackedInline):
    model = FeedImage
    extra = 0
    
class FeedsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ('text',)}),
        ('Publication', {"fields": ('pub_date', 'author')}),
    )
    inlines = [FeedImageInline]
    

admin.site.register(Feed, FeedsAdmin)