# Generated by Django 4.0.4 on 2022-05-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('open', 'open'), ('merge', 'merge')], default='open', max_length=5)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
