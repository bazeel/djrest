from django.contrib import admin
from .models import List, Message


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    fields = ('user', 'success', 'date_created', 'date_sent')
    readonly_fields = ('user', 'success', 'date_created', 'date_sent')


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('id', 'listid', 'list', 'title', 'user', 'success', 'date_created', 'date_sent', 'response')
    list_filter = ('success', 'date_created', 'date_sent')
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'list__id', 'title']

    def listid(self, obj):
        return obj.list.id
    listid.short_description = 'list id'


class ListAdmin(admin.ModelAdmin):
    model = List
    inlines = [MessageInline]
    filter_horizontal = ['users', ]


admin.site.register(Message, MessageAdmin)
admin.site.register(List, ListAdmin)
