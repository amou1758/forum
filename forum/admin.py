# coding=utf-8

from django.contrib import admin
from forum.models import ForumUser, Plane, Node, Topic, Reply, Favorite, Notification, Transaction, Vote


class ForumUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'nickname')
    list_filter = ('is_active', 'is_staff', 'date_joined')


class PlaneAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    list_filter = ('created',)


class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created')
    search_fields = ('name',)
    list_filter = ('created',)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title', 'content')
    list_filter = ('created',)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('content', 'created')
    search_fields = ('content',)
    list_filter = ('created',)


admin.site.register(ForumUser, ForumUserAdmin)
admin.site.register(Plane, PlaneAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Favorite)
admin.site.register(Notification)
admin.site.register(Transaction)
admin.site.register(Vote)
