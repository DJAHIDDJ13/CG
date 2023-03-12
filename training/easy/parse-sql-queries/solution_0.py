import sqlite3
import re

# Read the input
query = input()
query = re.sub(r"(\S+\s*=\s*)(\S+)", r"\1'\2'", query)
n = int(input())
header = input()

# Extract the table name from the query
table_name = query.split('FROM')[1].split()[0]

# Create a connection to an in-memory SQLite database
conn = sqlite3.connect(':memory:')

data_rows = [input().split() for _ in range(n)]
data_cols = [*zip(*data_rows)] # transposing the rows

# If the column in question has only digits i'll mark it as a "REAL" datatype in sql otherwise as a char(100)
data_cols = [colname + (" REAL" if all([re.match(r"^\d+(\.\d+)?$", row) != None for row in col]) else " CHAR(100)") for colname, col in zip(header.split(), data_cols)]
sql_types = ", ".join(data_cols)
# Create a table from the input data and rename it to the table name specified in the query
cursor = conn.cursor()
cursor.execute(f'CREATE TABLE {table_name} ({sql_types})')

for row in data_rows:
    values = ", ".join([f"'{value}'" for value in row])
    cursor.execute(f"INSERT INTO {table_name} VALUES ({values})")

# Execute the query and retrieve the results
cursor.execute(query)
results = cursor.fetchall()
query_headers = [i[0] for i in cursor.description]
# Print the results
print(*query_headers, sep=" ")
for row in results:
    print(*[x if isinstance(x, str) else format(x, 'g') for x in row], sep=" ")
