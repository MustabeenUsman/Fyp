# Generated by Django 3.2.10 on 2022-05-15 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRED', '0004_audio_books_quotes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Audio',
            new_name='Audios',
        ),
    ]