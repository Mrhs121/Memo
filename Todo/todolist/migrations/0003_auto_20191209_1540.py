# Generated by Django 2.1.4 on 2019-12-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_informations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informations',
            options={'verbose_name': '待办事项', 'verbose_name_plural': '待办事项'},
        ),
        migrations.AlterField(
            model_name='informations',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
