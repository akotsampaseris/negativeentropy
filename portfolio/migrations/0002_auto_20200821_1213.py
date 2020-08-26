# Generated by Django 3.1 on 2020-08-21 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='websitecategory',
            options={'verbose_name': 'Website Category', 'verbose_name_plural': 'Website Categories'},
        ),
        migrations.AddField(
            model_name='website',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='website',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.websitecategory'),
        ),
        migrations.AlterField(
            model_name='website',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='websitecategory',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
