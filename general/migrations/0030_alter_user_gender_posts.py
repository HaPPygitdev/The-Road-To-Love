# Generated by Django 4.0 on 2022-05-13 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0029_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Men', 'Мen'), ('Women', 'Women')], max_length=10),
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('place', models.CharField(blank=True, choices=[('cafe', 'Cafe'), ('cinema', 'Cinema')], default='cafe', max_length=10, verbose_name='Place')),
                ('full_text', models.TextField(max_length=500, verbose_name='Статья')),
                ('author_p', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='general.user')),
            ],
        ),
    ]