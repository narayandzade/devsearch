# Generated by Django 4.2.2 on 2023-06-14 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profiles_username'),
        ('projects', '0010_project_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profiles'),
        ),
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='uploads/default.png', null=True, upload_to='uploads/'),
        ),
    ]
