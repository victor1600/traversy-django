## Postgres setup
Follow official documentation at: https://www.postgresql.org/download/linux/ubuntu/

## Set up Django
### requirements:
```python
pip3 install pyscopg2
pip3 install psycopg2-binary
```

### Create db
Open a terminal:
```bash
sudo -u postgres - i
psql
```
Create a new db:

```bash
CREATE DATABASE btredb OWNER postgres;
CREATE DATABASE
```
see the list of db's
```bash
\l
```

Enter your credentials in settings.py.
