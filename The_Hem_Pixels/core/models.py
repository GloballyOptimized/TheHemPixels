from django.db import models
import uuid
from datetime import datetime

class Portfolio(models.Model):
    image_id = models.UUIDField(primary_key=True , default=uuid.uuid4)
    image = models.ImageField(upload_to='Portfolio_Data')
    uploaded_at = models.DateTimeField(default=datetime.now)
