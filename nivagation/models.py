from django.db import models
from django.utils import timezone


class road_construction(models.Model):
    rwe_type = models.TextField(max_length=50, null=True)
    rwe_closure_type = models.TextField(max_length=50, null=True)
    rwe_status = models.TextField(max_length=50, null=True)
    rwe_start_dt = models.TextField(max_length=50, null=True)
    rwe_end_dt = models.TextField(max_length=50, null=True)
    rwe_publish_text = models.TextField(max_length=500, null=True)
    subject_pref_rdname = models.TextField(max_length=50, null=True)
    traffic_delay = models.TextField(max_length=200, null=True)
    speed_limit = models.TextField(max_length=50, null=True)
    lanes_affected = models.TextField(max_length=50, null=True)
