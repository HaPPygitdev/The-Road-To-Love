# Generated by Django 4.0 on 2022-02-07 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_alter_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(default='Eb72A107db4BaDcf1Ab0383Ce59eB1', max_length=100),
        ),
    ]
