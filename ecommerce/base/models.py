from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# why we want django to treat it as an class not as an model ?# Because we want to use it as a base class for other models to inherit common fields and behaviors without creating a separate database table for BaseModel itself.