# Generated by Django 3.2.9 on 2021-11-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_rename_parola_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.DateField(),
        ),
    ]
