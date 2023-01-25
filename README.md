# Project Title

A backend API for project snow. Development in progress

Utilizes:

- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- PostgreSQL

## Environment setup

**1. Clone the repository**

```
 git clone https://github.com/daniel-daum/project-snow-backend.git
```

**2. Change directories into the project**

```
cd project-snow-backend
```

**3. Setup a python virtual Environment**

Windows:

```
python -m  venv <name-of-you-virtual-env>
```

Linux:

```
python3 -m  venv <name-of-you-virtual-env>
```

**4. Activate the virutal Environment**

Windows:

```
./<name-of-virtual-env>/scripts/activate
```

Linux:

```
source ./<name-of-virtual-env>/bin/activate
```

**5. Upgrade pip & Install the required dependencies**

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

**6. Add environment variables**

There are several required environment variables. Create a .env file in the projects root directory. This API utilizes postgres as its database backend. Provide the required connection keys in the .env file

Required env vars (with fake examples)

- DBNAME: project_snow_database
- DBHOST: localhost
- DBPORT: 5432
- DBTYPE: postgresql
- DBUSER: postgres
- DBPASS: postgres
- ALGO: Choice of hashing algorithm
- KEY: generated secret key ($ openssl rand -hex 32 ...rotate this key frequently)

**7. Run the inital database migration, utilizing Alembic**

```
alembic upgrade head
```

**8. Run data insert scripts**

Automatic data loading script is a work in progress. Currently data is being manually added to the database.

**6. Start the API server**

In the project's root directory run:

```
uvicorn project_snow.main:app --reload
```
