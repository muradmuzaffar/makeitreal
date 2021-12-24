# Generated by Django 3.2.9 on 2021-12-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_question_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='question_2',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='What is worth of your project? How can it help our society?'),
        ),
        migrations.AddField(
            model_name='project',
            name='question_3',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='What is your main goal? How do you see your project in the future(2 years, 5 years)?'),
        ),
    ]