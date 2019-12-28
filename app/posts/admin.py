# Django

from django.contrib import admin

# Own

from posts.models import Post, Tag, Subscriber


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'active', 'views', 'cover')
    list_display_links = ('cover', 'title')
    list_editable = ('active',)
    search_fields = ('title', 'slug')
    list_filter = ('pub_date', 'modified', 'active', 'tags')
    fieldsets = (
        ('Post', {
            "fields": (
                ('title',),
                ('slug',),
                ('cover',),
                ('summary',),
                ('body',),
                ('tags',),
                ('active',),
            ),
        }),
        ('Metadata', {
            "fields": (
                ('pub_date', 'modified', 'views')
            )
        })
    )
    readonly_fields = ('pub_date', 'modified', 'views')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    fieldsets = (
        ('Tag', {
            "fields": (
                ('name', 'slug'),
            ),
        }),
    )


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'active')
    search_fields = ('name', 'email')
    fieldsets = (
        ('Subscriber', {
            "fields": (
                ('name', 'email', 'active'),
            ),
        }),
    )
