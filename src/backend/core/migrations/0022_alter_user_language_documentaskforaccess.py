# Generated by Django 5.2.3 on 2025-06-18 10:02

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0021_activate_unaccent_extension"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentAskForAccess",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        help_text="primary key for the record as UUID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="id",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="date and time at which a record was created",
                        verbose_name="created on",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="date and time at which a record was last updated",
                        verbose_name="updated on",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("reader", "Reader"),
                            ("editor", "Editor"),
                            ("administrator", "Administrator"),
                            ("owner", "Owner"),
                        ],
                        default="reader",
                        max_length=20,
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ask_for_accesses",
                        to="core.document",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ask_for_accesses",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Document ask for access",
                "verbose_name_plural": "Document ask for accesses",
                "db_table": "impress_document_ask_for_access",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("user", "document"),
                        name="unique_document_ask_for_access_user",
                        violation_error_message="This user has already asked for access to this document.",
                    )
                ],
            },
        ),
    ]
