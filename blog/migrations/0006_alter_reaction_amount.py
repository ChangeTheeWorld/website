# Generated by Django 5.0.7 on 2024-07-21 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_reaction_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]