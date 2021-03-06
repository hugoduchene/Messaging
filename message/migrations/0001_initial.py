# Generated by Django 3.1.1 on 2020-10-06 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('id_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation_creator', to=settings.AUTH_USER_MODEL)),
                ('id_recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation_recipient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_message', models.DateTimeField(default=django.utils.timezone.now)),
                ('content_message', models.TextField(default="he wanted to make a joke and he didn't write anything down. you're huge man !")),
                ('id_conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.conversation')),
                ('id_giving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_giving', to=settings.AUTH_USER_MODEL)),
                ('id_receiving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_receiving', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
