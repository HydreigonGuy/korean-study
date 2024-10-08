# Generated by Django 2.2.12 on 2024-10-08 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.BooleanField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('Profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Profile')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.EnglishWord')),
            ],
        ),
        migrations.CreateModel(
            name='Accuracy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_guesses', models.IntegerField(default=0)),
                ('total_guesses', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Profile')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.EnglishWord')),
            ],
        ),
    ]