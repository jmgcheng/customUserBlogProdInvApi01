# Generated by Django 4.2.5 on 2023-09-16 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import files.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=files.models.upload_location)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date uploaded')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]