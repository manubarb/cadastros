# Generated by Django 5.1.1 on 2024-10-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_campo_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='campo',
            name='arquivo',
            field=models.FileField(default=1, upload_to='pdf/'),
            preserve_default=False,
        ),
    ]
