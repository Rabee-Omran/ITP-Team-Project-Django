# Generated by Django 3.1.2 on 2020-10-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20201020_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[(1, 'محاضرة'), (2, 'تسجيل'), (3, 'تفريغ')], max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='subject_type',
            field=models.CharField(choices=[(1, 'نظري'), (2, 'عملي')], max_length=15),
        ),
    ]
