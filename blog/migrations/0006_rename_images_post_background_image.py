# Generated by Django 4.0.4 on 2022-06-01 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_category_options_post_subtitle_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='images',
            new_name='background_image',
        ),
    ]