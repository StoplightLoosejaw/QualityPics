# Generated by Django 2.2.3 on 2020-02-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200201_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pic',
            name='description_flg',
        ),
        migrations.AddField(
            model_name='pic',
            name='description',
            field=models.TextField(default='Пожалуй, лучшая картинка во всем интернете'),
        ),
    ]
