# Generated by Django 3.2.9 on 2021-11-05 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]