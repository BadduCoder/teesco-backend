# Generated by Django 3.0.5 on 2020-05-07 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('org', '0005_auto_20200506_2047'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media_platform', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('share_link', models.CharField(max_length=30)),
                ('share_text', models.CharField(max_length=65536)),
                ('share_img', models.ImageField(upload_to='uploads/tasks/share_img')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='org.Org')),
            ],
        ),
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='uploads/tasks/screenshots')),
                ('points', models.IntegerField()),
                ('review_by_ai', models.CharField(choices=[('accepted', 'Accepted'), ('pending', 'Review Pending'), ('rejected', 'Rejected')], max_length=50)),
                ('review_by_human', models.CharField(choices=[('accepted', 'Accepted'), ('pending', 'Review Pending'), ('rejected', 'Rejected')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
            ],
        ),
    ]
