# Generated by Django 3.1.6 on 2021-02-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_author_email',
            field=models.EmailField(default='', max_length=254, verbose_name='email'),
        ),
    ]