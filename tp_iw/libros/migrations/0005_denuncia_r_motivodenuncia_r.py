# Generated by Django 3.1 on 2020-10-11 12:36

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libros', '0004_comment_r'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotivoDenuncia_r',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia_r',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('aceptada', models.BooleanField(default=False)),
                ('vista', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.comment_r')),
                ('motivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.motivodenuncia_r')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
