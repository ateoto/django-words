# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, unique_for_date='published_on')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id', editable=False)),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('edited_on', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                u'verbose_name_plural': 'Entries',
            },
            bases=(models.Model,),
        ),
    ]
