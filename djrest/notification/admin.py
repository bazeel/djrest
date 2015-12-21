from django.contrib import admin
from .models import UserList, MessageLog, Message


class MessageLogAdmin(admin.ModelAdmin):
    model = MessageLog
    list_display = ('id', 'message_id', 'message', 'title', 'user', 'success', 'date_created', 'date_sent', 'response')
    list_filter = ('success', 'date_created', 'date_sent')
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'message__id', 'title']

    def message_id(self, obj):
        return obj.message.id
    message_id.short_description = 'message id'


class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ('id', 'userlist_id', 'title', 'date_created', 'processed')

    def userlist_id(self, obj):
        return obj.user_list.id
    userlist_id.short_description = 'user list id'


class UserListAdmin(admin.ModelAdmin):
    model = UserList
    list_display = ('id', 'title', 'date_created')
    filter_horizontal = ['users', ]


admin.site.register(UserList, UserListAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageLog, MessageLogAdmin)