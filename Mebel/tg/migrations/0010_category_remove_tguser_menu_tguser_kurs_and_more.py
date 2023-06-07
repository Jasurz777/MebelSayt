# Generated by Django 4.0.6 on 2023-01-20 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0009_alter_tguser_lang_alter_tguser_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=56)),
                ('name_ru', models.CharField(max_length=56)),
            ],
        ),
        migrations.RemoveField(
            model_name='tguser',
            name='menu',
        ),
        migrations.AddField(
            model_name='tguser',
            name='kurs',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='tguser',
            name='subscribe',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tguser',
            name='user_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('ctg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tg.category')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('til', models.IntegerField(default=1)),
                ('ctg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tg.sub')),
            ],
        ),
    ]
