# Generated by Django 4.2.1 on 2023-05-29 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StockRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ստեղծվել է')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='փոփոխվել է')),
                ('name', models.CharField(max_length=25, verbose_name='անվանում')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ստեղծող')),
            ],
            options={
                'verbose_name': 'պահեստախուց',
                'verbose_name_plural': 'պահեստախցեր',
            },
        ),
    ]
