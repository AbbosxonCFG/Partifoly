# Generated by Django 5.0.4 on 2024-04-22 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_review_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='descriptio',
            new_name='description',
        ),
    ]
