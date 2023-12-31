# Generated by Django 4.2.5 on 2023-09-30 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_tag_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='', verbose_name='images/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.category')),
                ('tags', models.ManyToManyField(related_name='images', to='home.tag')),
            ],
        ),
        migrations.DeleteModel(
            name='DemoTable',
        ),
        migrations.RemoveField(
            model_name='photographerprofile',
            name='photographer',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='Uplaod',
        ),
        migrations.DeleteModel(
            name='Photographer',
        ),
        migrations.DeleteModel(
            name='PhotographerProfile',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
