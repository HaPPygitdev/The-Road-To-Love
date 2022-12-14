# Generated by Django 4.0 on 2022-02-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0015_voted_delete_userpoll_alter_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='voted',
            name='type',
            field=models.CharField(choices=[('I_MC', 'Identified_MultipleChoice'), ('I_SC', 'Identified_SingleChoice'), ('A_MC', 'Anonymous_MultipleChoice'), ('A_SC', 'Anonymous_SingleChoice')], max_length=4),
        ),
    ]
