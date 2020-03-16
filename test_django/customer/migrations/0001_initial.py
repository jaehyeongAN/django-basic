# Generated by Django 3.0.4 on 2020-03-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=64, verbose_name='고객명')),
                ('customeremail', models.CharField(max_length=128, verbose_name='고객이메일')),
                ('password', models.CharField(max_length=32, verbose_name='비밀번호')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '고객정보',
                'verbose_name_plural': '고객정보',
                'db_table': 'django_customer',
            },
        ),
    ]
