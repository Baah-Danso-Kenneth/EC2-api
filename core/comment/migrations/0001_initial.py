# Generated by Django 4.0 on 2024-01-11 03:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_user', '0004_user_posts_liked'),
        ('core_post', '0002_alter_post_created_alter_post_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('edited', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_user.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_post.post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]