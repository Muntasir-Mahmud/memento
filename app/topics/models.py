from app.db.models import TimeStampedModel

from tortoise import fields


class Topic(TimeStampedModel):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.CharField(max_length=255)

    class Meta:
        table = "topics"
        table_description = "Topics table"
        ordering = ["name"]

    def __str__(self):
        return self.name
