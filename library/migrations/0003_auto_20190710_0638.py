# Generated by Django 2.2.3 on 2019-07-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20190710_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='book',
        ),
        migrations.AddField(
            model_name='writer',
            name='book',
            field=models.ManyToManyField(related_name='books', to='library.Book', verbose_name='book'),
        ),
    ]
