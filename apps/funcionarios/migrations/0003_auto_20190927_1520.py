# Generated by Django 2.2.5 on 2019-09-27 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20190926_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='empresas',
            new_name='empresa',
        ),
    ]
