# Generated by Django 2.2.2 on 2019-07-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0013_comment_sub_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to=''),
        ),
    ]
