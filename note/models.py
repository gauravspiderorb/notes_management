from django.db import models

# Create your models here.

class ModelNote(models.Model):
    # fields of the model
    title = models.CharField(
        max_length=200,
        help_text=(
            "title of note"
        )
    )
    description = models.TextField(
        help_text=(
            "description of note"
        )
    )

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "note"
        verbose_name = "Note"
        verbose_name_plural = "Note"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
