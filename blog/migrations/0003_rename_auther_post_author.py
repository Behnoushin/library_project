# Generated by Django 5.1.1 on 2024-09-09 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="auther",
            new_name="author",
        ),
    ]
