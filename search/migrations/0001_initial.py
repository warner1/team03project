from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('articleid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('date', models.CharField(blank=True, max_length=45, null=True)),
                ('articletype', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('teamid', models.AutoField(primary_key=True, serialize=False)),
                ('teamname', models.CharField(max_length=45)),
                ('teamname_eng', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='teamid',
            field=models.ForeignKey(blank=True, db_column='teamid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='search.Teams'),
        ),
    ]
