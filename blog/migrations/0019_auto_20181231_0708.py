# Generated by Django 2.1 on 2018-12-31 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_postcategory_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_author',
            new_name='name',
        ),
    ]
