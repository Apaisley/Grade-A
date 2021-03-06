# Generated by Django 3.0.2 on 2020-03-06 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('catagory', models.CharField(choices=[('PL', 'Pollen'), ('FP', 'Feminized Pollen'), ('SD', 'Seeds'), ('FS', 'Feminized Seeds'), ('AS', 'Auto Flowering Seeds'), ('FL', 'Flower'), ('CS', 'Concentrates'), ('ES', 'Edibles')], max_length=30)),
                ('variety', models.CharField(choices=[('SA', 'Sativa'), ('IN', 'Indica'), ('HY', 'Hybrid')], max_length=2)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('quantity', models.IntegerField()),
                ('Image', models.ImageField(default='Null', upload_to='')),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('effects', models.CharField(choices=[('UP', 'Uplifted'), ('HA', 'Happy'), ('RE', 'Relaxed'), ('EN', 'Energetic'), ('CE', 'Creative'), ('FO', 'Focused'), ('TA', 'Talkative'), ('EU', 'Euphoric'), ('GI', 'Giggly'), ('HU', 'Hungry'), ('AR', 'Aroused'), ('TI', 'Tingy'), ('SL', 'Sleepy')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grade_A.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='Review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Grade_A.Review'),
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Grade_A.Cart')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Grade_A.Products')),
            ],
        ),
        migrations.AddIndex(
            model_name='products',
            index=models.Index(fields=['name'], name='Grade_A_pro_name_0f1ca8_idx'),
        ),
    ]
