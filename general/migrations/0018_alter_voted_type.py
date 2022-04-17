# Generated by Django 4.0 on 2022-02-07 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0017_alter_voted_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voted',
            name='type',
            field=models.CharField(choices=[('A_SC', 'Anonymous_SingleChoice'), ('A_MC', 'Anonymous_MultipleChoice'), ('I_SC', 'Identified_SingleChoice'), ('I_MC', 'Identified_MultipleChoice')], max_length=4),
        ),
    ]
