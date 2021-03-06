# Generated by Django 2.1.7 on 2019-07-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duyuru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duyuru_baslik', models.CharField(max_length=150, verbose_name='Duyuru Başlığı')),
                ('duyuru_mesaj', models.TextField(verbose_name='Duyuru Mesajı')),
                ('duyuru_tarihi', models.DateField(verbose_name='Duyuru Tarihi')),
                ('duyuru_slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Duyuru',
                'verbose_name_plural': 'Duyurular',
                'ordering': ('-duyuru_tarihi',),
            },
        ),
    ]
