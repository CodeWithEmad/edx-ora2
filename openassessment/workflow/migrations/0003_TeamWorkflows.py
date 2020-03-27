# Generated by Django 2.2.10 on 2020-03-27 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0002_remove_django_extensions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamAssessmentWorkflow',
            fields=[
                ('assessmentworkflow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='workflow.AssessmentWorkflow')),
                ('team_submission_uuid', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('workflow.assessmentworkflow',),
        ),
    ]
