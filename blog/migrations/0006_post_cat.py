# Generated by Django 2.1 on 2018-12-01 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_postcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.PostCategory'),
        ),
    ]