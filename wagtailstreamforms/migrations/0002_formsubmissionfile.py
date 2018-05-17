# Generated by Django 2.0.4 on 2018-05-17 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailstreamforms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmissionFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=255, verbose_name='Field')),
                ('file', models.FileField(upload_to='streamforms/', verbose_name='File')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='wagtailstreamforms.FormSubmission', verbose_name='Submission')),
            ],
            options={
                'verbose_name': 'Form submission file',
                'ordering': ['field', 'file'],
            },
        ),
    ]