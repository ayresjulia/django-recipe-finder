from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('child_first_name', models.CharField(max_length=50)),
                ('child_last_name', models.CharField(max_length=50)),
                ('allergies', models.CharField(max_length=300)),
                ('recipes', models.CharField(max_length=300)),
            ],
        ),
    ]
