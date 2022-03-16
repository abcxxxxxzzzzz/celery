from __future__ import absolute_import
from .celery import app as celery_tasks


__all__ = ('celery_tasks',)
