import csv

import pandas as pd
from celery import shared_task
from django.core.files.storage import default_storage

from .models import DistrictArea


@shared_task
def add_districts(file):
    print("Starting to process districts")
    try:
        with default_storage.open(file, "rb") as f:

            data = pd.read_csv(f)
        objs_to_create = [
            DistrictArea(name=row["name"], area=row["area"])
            for index, row in data.iterrows()
        ]
        created_objs = DistrictArea.objects.bulk_create(objs_to_create, batch_size=100)
        print(f"\n\nCreated {len(created_objs)} districts\n\n")

    except Exception as e:
        print(f"Error reading file: {e}")

    print("Finished processing districts")
