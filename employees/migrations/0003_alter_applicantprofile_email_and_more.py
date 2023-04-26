# Generated by Django 4.2 on 2023-04-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0002_alter_applicantprofile_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicantprofile",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="resume",
            field=models.FileField(upload_to="media/resumes/"),
        ),
        migrations.AddConstraint(
            model_name="jobapplication",
            constraint=models.UniqueConstraint(
                fields=("job_listing", "applicant"), name="unique_job_application"
            ),
        ),
    ]