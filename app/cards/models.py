from app.db.models import TimeStampedModel

from tortoise import fields


class Card(TimeStampedModel):
    id = fields.UUIDField(pk=True)
    question = fields.CharField(max_length=255)
    answer = fields.CharField(max_length=255)
    hint = fields.CharField(max_length=255)
    image = fields.CharField(max_length=255)
    description = fields.CharField(max_length=255)
    topic = fields.ForeignKeyField(model_name="models.Topic",
                                   related_name="cards",
                                   on_delete=fields.NO_ACTION)

    class Meta:
        table = "cards"
        table_description = "Cards table"
        ordering = ["name"]

    def __str__(self):
        return self.question
