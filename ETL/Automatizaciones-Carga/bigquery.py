from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from google.oauth2 import service_account
from google.cloud import storage

"""# Cargamos las credenciales de nuestra cuenta de servicio
credentials = service_account.Credentials.from_service_account_file(
    'hidden-phalanx-412816-bdcd3af97eda.json')"""

# Inicializamos el cliente de BigQuery
client = bigquery.Client()
storage_client = storage.Client()

# Especifica la ruta del archivo en GCS
bucket_name = 'pf_henry_nexusanalytics'
folder_name = 'gold'

bucket = storage_client.get_bucket(bucket_name)

# Función para verificar y crear un dataset
def check_and_create_dataset(dataset_name):
    dataset_id = f"{client.project}.{dataset_name}"
    dataset = bigquery.Dataset(dataset_id)
    try:
        client.get_dataset(dataset_id)  # Verificamos si el dataset existe
        print(f"Dataset {dataset_name} ya existe.")
    except NotFound:
        dataset = client.create_dataset(dataset)  # Creamos el dataset
        print(f"Dataset {dataset_name} creado.")

# Función para verificar y crear una tabla y cargar datos desde un archivo
def check_and_create_table(dataset_name, table_name, file_path):
    blob_business = bucket.blob(f"{folder_name}/{file_path}")

    with open (file_path,"wb") as f:
        file_content_business = blob_business.download_as_bytes()
        f.write(file_content_business)

    table_id = f"{client.project}.{dataset_name}.{table_name}"
    try:
        table = client.get_table(table_id)  # Verificamos si la tabla existe
        print(f"La tabla {table_name} ya existe en {dataset_name}.")
    except NotFound:
        table = bigquery.Table(table_id)
        table = client.create_table(table)  # Creamos la tabla
        print(f"Tabla {table_name} creada en {dataset_name}.")

    # Cargamos los datos desde el archivo
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, 
        skip_leading_rows=1, 
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # Sobrescribe los datos existentes
    )
    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    job.result()  # Esperamos a que se complete la carga de datos

    print(f"Datos cargados a la tabla {table_name} desde el archivo {file_path}.")

def main():
    # Datasets y tablas a crear
    datasets = {
        "Twitter": ["Twitter"],
        "GoogleMaps": ["Metadata_GM", "ReviewsFlorida_GM"],
        "Yelp": ["Business_Yelp", "CheckIn_Yelp", "Review_Yelp"],
    }

    # Verificamos y creamos los datasets y tablas
    for dataset_name, tables in datasets.items():
        check_and_create_dataset(dataset_name)
        for table_name in tables:
            # Aquí debes proporcionar la ruta al archivo CSV correspondiente
            file_path = f"{table_name}.csv"
            check_and_create_table(dataset_name, table_name, file_path)