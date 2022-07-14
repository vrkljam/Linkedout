# Generated by Django 4.0.6 on 2022-07-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkoapp', '0029_portrait_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='portrait',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='portrait',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='portrait',
            name='photo_url',
            field=models.TextField(null=True),
        ),
    ]
