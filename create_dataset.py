"""Create BigQuery dataset 'test_123' in project clgx-surveillance-sbx-f577."""
from google.cloud import bigquery

PROJECT_ID = "clgx-surveillance-sbx-f577"
DATASET_ID = "test_123"
LOCATION = "US"


def main():
    client = bigquery.Client(project=PROJECT_ID)
    dataset = bigquery.Dataset(f"{PROJECT_ID}.{DATASET_ID}")
    dataset.location = LOCATION
    dataset = client.create_dataset(dataset, exists_ok=True)
    print(f"Created dataset {dataset.project}.{dataset.dataset_id} in {dataset.location}")


if __name__ == "__main__":
    main()
