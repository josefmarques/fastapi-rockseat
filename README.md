python3 -m venv venv
source/venv/bin/activate ou . venv/bin/activate
pip install pylint
pylint --generate-rcfile > .pylintrc (para formatação de código)
## instalar extensão vscode pylint
## No arquivo .pylintrc alterei max-line-length=120 e adocionei as linhas abaixo:

[MAIN]

disable=
      C0116, #missing-function-docstring
      E0015, #unrecognized-option
      C0114, #missing-module-docstring
      C0209, #consider-using-f-string
      C0115, #missing-class-docstring

pip install fastapi
pip install uvicorn
pip freeze > requirements.txt

pip install SQLAlchemy
pip install aiopg
pip install sqlalchemy psycopg2-binary
pip install asyncpg
