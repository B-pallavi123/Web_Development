

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who sent the message
    message = models.TextField()  # The message content  
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of the message
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')  # Parent message for replies
     
    def __str__(self):
        return f"{self.user.username}: {self.message}"
    


'''from django.db import models
from django.contrib.auth.models import User

class Email_Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who will receive the notification
    message = models.CharField(max_length=255)  # Notification message
    read = models.BooleanField(default=False)  # Whether the notification has been read
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of notification creation

    def __str__(self):
        return self.message'''
