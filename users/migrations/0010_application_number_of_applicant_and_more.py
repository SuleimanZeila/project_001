# Generated by Django 4.2.2 on 2023-08-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_school_id_card_uploadeddocuments_id_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='number_of_applicant',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='uploadeddocuments',
            name='birth_certificate',
            field=models.FileField(blank=True, null=True, upload_to='documents/birth_certificates/'),
        ),
    ]
