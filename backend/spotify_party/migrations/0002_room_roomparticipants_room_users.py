# Generated by Django 4.2 on 2023-05-12 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("spotify_party", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "code",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                (
                    "host",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hosted_rooms",
                        to="spotify_party.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RoomParticipants",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("joined_at", models.DateTimeField(auto_now_add=True)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spotify_party.room",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spotify_party.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="room",
            name="users",
            field=models.ManyToManyField(
                related_name="joined_rooms",
                through="spotify_party.RoomParticipants",
                to="spotify_party.user",
            ),
        ),
    ]