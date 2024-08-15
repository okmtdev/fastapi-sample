# fastapi-sample


```
rye run ruff format src
```

```
docker exec -it fastapi-sample-api-1 bash
root@cdd560e6d86b:/app# alembic -c src/repository/alembic.ini revision --autogenerate -m "create tables"
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
  Generating /app/src/repository/migrations/versions/4d63a77d31b1_create_tables.py ...  done
```