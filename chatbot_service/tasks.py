from celery import shared_task
from .models import UserQuery


def process_query(query_id):
    query = UserQuery.objects.get(id=query_id)
    # Perform any long-running task like querying a large dataset or retraining the model

    query.response = "Processed Response"
    query.save()