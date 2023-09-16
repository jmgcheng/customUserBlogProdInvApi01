import os
from django.conf import settings
from uuid import uuid4
from django.db import models
from django.shortcuts import redirect


def upload_location(instance, filename):
    owner_id = str(instance.owner.id)
    old_name = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]  # Get the file extension
    timestamp = uuid4().hex[:10]  # Generate a timestamp (you can adjust the length as needed)
    new_filename = f"{old_name}-{timestamp}{extension}"  # Add the timestamp to the filename
    file_path = f'files/{owner_id}/{new_filename}'
    return file_path


class File(models.Model):
    file = models.FileField(upload_to=upload_location, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, verbose_name="date uploaded")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='files')

    def __str__(self):
        return self.file.file.name
    