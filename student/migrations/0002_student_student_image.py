# Generated by Django 3.1.7 on 2021-03-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]