# Generated by Django 4.0 on 2022-05-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0030_alter_user_gender_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temporary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(blank=True, max_length=200)),
                ('confirm_password', models.CharField(blank=True, max_length=200)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('second_name', models.CharField(blank=True, max_length=100)),
                ('age', models.CharField(blank=True, max_length=3)),
                ('gender', models.CharField(blank=True, choices=[('Men', 'Мen'), ('Women', 'Women')], max_length=10)),
                ('session', models.CharField(blank=True, max_length=200)),
                ('salt', models.CharField(max_length=200)),
            ],
        ),
    ]
