# Generated by Django 2.2.1 on 2019-05-06 23:18

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('steps', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=255)),
                ('quantity', models.CharField(blank=True, max_length=10, null=True)),
                ('bought', models.BooleanField(blank=True, default=False, null=True)),
                ('user', models.ForeignKey(on_delete='cascade', related_name='shopping_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('ingredient', models.ForeignKey(on_delete='cascade', to='app.Ingredient')),
                ('recipe', models.ForeignKey(on_delete='cascade', related_name='ingredient_quantity', to='app.Recipe')),
            ],
            options={
                'db_table': 'app_ingredient_recipe',
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ManyToManyField(related_name='ingredients', through='app.IngredientRecipe', to='app.Recipe'),
        ),
        migrations.CreateModel(
            name='DailyRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(db_index=True, default=django.utils.timezone.now)),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete='cascade', related_name='daily_recipe', to='app.Recipe')),
                ('user', models.ForeignKey(on_delete='cascade', related_name='daily_recipe', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'day')},
            },
        ),
    ]