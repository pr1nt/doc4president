# Generated by Django 2.0.4 on 2018-05-07 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Templator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/', verbose_name='Attachment')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Templator.Record', verbose_name='Message')),
            ],
        ),
    ]
