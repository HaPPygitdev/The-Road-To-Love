# Generated by Django 4.0 on 2022-05-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0035_message_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='place_address',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='message',
            name='place_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
