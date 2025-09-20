# Text to SQL

A project that converts natural language queries into SQL statements.

## Features
- Translate plain English questions into SQL queries
- Supports multiple SQL dialects
- Easy to extend and customize

## Installation
```bash
git clone https://github.com/202201255/Text_to_SQL.git
cd Text_to_SQL
pip install -r requirements.txt


from text_to_sql import convert

query = "Show all users who registered in 2023"
sql = convert(query)
print(sql)
