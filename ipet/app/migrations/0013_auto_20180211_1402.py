# Generated by Django 2.0.1 on 2018-02-11 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_post_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='clinic',
            name='phone_number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='petowner',
            name='phone_number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='likes_likes', to='app.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='post',
            name='reports',
            field=models.ManyToManyField(related_name='reports_reports', to='app.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='app.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reports',
            field=models.ManyToManyField(related_name='reports', to='app.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='vet',
            name='phone_number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.PhoneNumber'),
        ),
    ]
