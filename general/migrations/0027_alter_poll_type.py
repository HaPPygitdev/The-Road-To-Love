# Generated by Django 4.0.4 on 2022-04-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0026_rename_poll_vote_poll_id_rename_user_vote_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='type',
            field=models.CharField(choices=[('A_MC', 'Anonymous, multiple choice'), ('N_MC', 'Not anonymous, multiple choice')], max_length=4),
        ),
    ]
