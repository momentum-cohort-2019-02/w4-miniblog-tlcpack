# Generated by Django 2.1.7 on 2019-03-08 19:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Blog'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=django.utils.timezone.now, help_text='Please add a friendly comment', max_length=10000),
            preserve_default=False,
        ),
    ]
