# Generated by Django 4.0 on 2022-02-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_alter_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(default='c4c582e50e0aBEfa1ebD35f3Df0CF3', max_length=100),
        ),
    ]
