# Generated by Django 3.1 on 2020-09-28 22:04

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libros', '0003_auto_20200928_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_r',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('denuncias', models.ManyToManyField(related_name='comments_review', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='libros.review')),
                ('usuario_r', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]