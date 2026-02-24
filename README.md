# Creació entorn virtual per instal·lar llibreries

```bash
python -m virtualenv venv
source venv/Script/activate
```

# Instal·lacions

```bash
pip install fastapi uvicorn sqlalchemy psycopg2 fastapi-utils pymysql python-dotenv
```

# Freeze dels requirements
```bash
pip freeze > requirements.txt
```

# Arrencar el servidor

```bash
uvicorn entrypoint:app --reload
```
Funciona com a "healthcheck".

* Servidor: `http://127.0.0.1:8000`
* Documentació: `http://127.0.0.1:8000/docs`

# Iniciar Git i primer commit

```bash
git init
git add .
git commit -m "first commit"

```
També he creat un arxiu .gitignore per ignorar la carpeta de l'entorn virtual i els arxius compilats/caché de python generats automàticament.