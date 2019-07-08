# Generated by Django 2.2.3 on 2019-07-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_category_imgae_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Close'), (1, 'Open')], default=1),
        ),
    ]