# Generated by Django 3.0.8 on 2020-08-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(upload_to='event_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(),
        ),
    ]