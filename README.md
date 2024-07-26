# Job Scrapper - project

## Why did I create this project?

This project is a result of my learning and practicing about scrapping with Python's library of Scrapy.

## What does this project do?

This project uses Scrapy spider (included in a special docker container) to scrap data from nofluffjobs.com portal (for more details, to scrap Python job offers), to validate the scrapped data and save it to a PostgreSQL database (located in a separate docker container). Next, the results are taken to Jupyter Notebook docker container, where the further analysis of the scrapped data is preformed and visualised with plots.

## How to run locally?

To run this project, a few activities will be necessary:

- Clone the project
- Go to the project directory. Type in the terminal (all commands from this chapter will be for Windows OS):

```bash
gci -Name
```

- You should see this:

```bash
db
job_scraper_app
JupyterNotebookFolder
.gitignore
docker-compose.yaml
README.md
```

- Now, if you want to run the project using a new dedicated virtual environment, please type the command below in your terminal (I presume, that you have already installed Python in your global virtual environment). If you want to use your global virtual environment to run this project, please skip these 2 steps below.

```bash
python -m venv my_new_virtual_environment
```
and:

```bash
.\my_new_virtual_environment\Scripts\activate
```

- After that, we will need to download and install a few docker images from the internet. Please execute these 3 commands:


```bash
docker pull jupyter/base-notebook
```
```bash
docker pull python
```
```bash
docker pull postgres
```



- Then, type the following command to initialize all the 3 containers that the project includes:

```bash
docker-compose up
```

- To go directly to the scrapped data analyze, when the Jupyter Notebook container running, please open your browser and type in a new tab:

```bash
localhost:8888
```

- This command will open the container's content that includes JupiterFileKuba.ipynb file with the scrapped data analyze. In order to check the results of the analyze in the browser tab, please click on the "Run" tab of the displayed page and choose the suboption of "Run All Cells"

![IMG IPYNB1](https://github.com/JakBiel/README_img/blob/main/jupyter_scr.PNG)

- The step above will generate plots with various analysis of the data.

## Schema of the project - directory tree

```bash
lab2
│   .gitignore # This file excludes from GIT all the files needed locally only like e.g. virtual environmen etc.
│   docker-compose.yaml # The file to simultaneous management of all the docker container used in the project
│   README.md # The file with project's documentation
│
├───db # The folder for the database docker PostgreSQL container. The volume with data-backup is in the hidden subfolder "data"
│       Dockerfile # Dockerfile used for creation of the PostgreSQL container
│       init.sql # File used to inform the PostgreSQL container how to initialize the database
│       .gitignore # This file excludes from GIT the volume with data-backup that is in the hidden subfolder "data"
│
├───job_scrapper_app # The folder for the docker container designed for Scrapy job scrapper application
│   │   Dockerfile # Dockerfile used for creation of the Scrappy application container
│   │   requirements.txt # List of programs to be pre-installed in order to correctly execute the whole Scrapy application
│   │   scrapy.cfg # It defines what the project name is and where the project's settings are located
│   │
│   └───job_scraper # The folder with the Scrapy project itself. The project is Scrapy job scrapper application
│       │   items.py # It defines the definition of scrapped items
│       │   middlewares.py # The project's middlewares. It is with default settings, not changed from the project's beginning
│       │   pipelines.py # It defines, how the scrapped items are validated and loaded to the database container
│       │   settings.py # It defines settings about modules like: database container, pipelines, encoding type, bot names etc.
│       │   __init__.py # Automatically generated file for package code management. Here, it is empty. 
│       │
│       └───spiders # The folder including the created Scrapy spider
│           new_offers_spider.py # The file with the job scrapper Scrapy spider
│           __init__.py # Automatically generated file for package code management. Here, it is empty. 
│
└───JupyterNotebookFolder # The folder for the JupyterNotebook docker container designed for JupyterNotebook analyzes
    │   requirements.txt # List of programs to be pre-installed in order to correctly execute the whole Jupyter application
    │   Dockerfile # Dockerfile used for the creation of the JupyterNotebook docker container
    │
    └───jpdata
        │   JupiterFileKuba.ipynb # The file with analyzes of data scrapped by job scrapper application
        │
        └───.ipynb_checkpoints # The folder with the saving checkpoints of .ipynb files
                JupiterFileKuba-checkpoint.ipynb # The file with the saving checkpoints of JupiterFileKuba.ipynb file

```

## Tip - How to view the scrapped data in a convenient way?

Using programs like e.g. DBeaver can be useful in order to analyze the scrapped data that is stored in PostgreSQL Docker container.

## Contributing

Here, I want to say thank you to my mentor Wojtek for his great contribution in code review and supporting me everytime when I got stucked somewhere in the project.

## Authors and acknowledgment

It is all my work, with a review and recommendations of my mentor Wojtek.

## License

No special license issued so far, I present it as a result of my work only.

## Project status

It is initaly finished (as 05.10.2023). Unknown if it is going to be developed in the future.

