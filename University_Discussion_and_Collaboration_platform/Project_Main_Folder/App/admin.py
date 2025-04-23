

# Register your models here.
from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp', 'is_read')
    list_filter = ('user', 'is_read')
    search_fields = ('user__username', 'message')

    def save_model(self, request, obj, form, change):
        # Automatically set the user if not provided
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('notifications.urls')),
    
]