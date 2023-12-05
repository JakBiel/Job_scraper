#DOCKERFILE DO notebook_container Z IMAGE'U jupter/base-notebook:v1

FROM jupyter/base-notebook

WORKDIR /JupyterNotebookFolder

COPY . .

RUN pip install -r requirements.txt

RUN pip install pandas numpy matplotlib seaborn psycopg2-binary unidecode

WORKDIR /JupyterNotebookFolder/jpdata