# Generated by Django 3.1.2 on 2020-10-29 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20201020_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.yearnum')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]