# Generated by Django 5.0.4 on 2024-04-21 13:33

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_careerinformations_careerinformation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='book/')),
                ('raiting', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Courseplaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, choices=[('auido_class', 'audio_class'), ('live_class', 'live_class'), ('recorded_class', 'recorded_class')], max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='mentor/')),
                ('descriptio', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to='main.category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('0', 'basic_pack'), ('1', 'standart_pack'), ('2', 'premium_pack')], max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxLengthValidator(5), django.core.validators.MinLengthValidator(1)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='main.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='CareerInformation',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Prduct',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='course',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='Subscribe',
        ),
        migrations.AddField(
            model_name='course',
            name='certificate',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='durations',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='course/'),
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxLengthValidator(5), django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='banner/'),
        ),
        migrations.AddField(
            model_name='courseplaylist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseplaylist', to='main.course'),
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]