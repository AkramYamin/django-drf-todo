# Generated by Django 3.2.9 on 2021-11-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_task_is_done'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('owner', 'title'), name='unique_category_per_user'),
        ),
    ]