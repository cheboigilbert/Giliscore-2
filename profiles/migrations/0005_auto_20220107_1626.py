# Generated by Django 3.2.9 on 2022-01-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220103_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfconLeague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.CreateModel(
            name='Baseball',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.CreateModel(
            name='Bundeslga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.CreateModel(
            name='EuropaLeague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.CreateModel(
            name='Formula1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.CreateModel(
            name='Laliga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.CreateModel(
            name='NBA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.CreateModel(
            name='NFL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.CreateModel(
            name='Worldcup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/club')),
            ],
        ),
        migrations.RenameField(
            model_name='englishpremierleague',
            old_name='Teamicon',
            new_name='icon',
        ),
    ]
