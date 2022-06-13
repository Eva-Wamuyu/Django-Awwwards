# Generated by Django 4.0.5 on 2022-06-11 21:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='avatars_kuiof2.png', upload_to='Awards')),
                ('user_bio', models.CharField(blank=True, max_length=255)),
                ('contact_information', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('project_cover', models.ImageField(upload_to='Awards')),
                ('description', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('usability', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('content', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.project')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='votes', to='account.vote'),
        ),
        migrations.AddField(
            model_name='profile',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='projects_posted', to='account.project'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]