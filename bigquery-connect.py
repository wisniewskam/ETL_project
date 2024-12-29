from google.cloud import bigquery

client = bigquery.Client()
sql_query = "SELECT * FROM project_name.dataset.table"
results = client.query(sql_query).to_dataframe()

print(results)