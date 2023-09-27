# Job Scrapper - project

## Why did I create this project?

This project is a result of my learning and practicing about scrapping with Python's library of Scrapy.

## What does this project do?

This project uses Scrapy spider to scrap data from nofluffjobs.com portal (for more details, to scrap Python job offers), to validate the scrapped data and save it to a PostgreSQL database. Next, the results are taken to Jupyter Notebook, where the further analysis of the scrapped data is preformed and visualised with plots.

## Installation / How to prepare to use

To start using this project, a few activities will be necessary:
1. Downloading the project folder and opening it with your terminal
2. Installing with your "pip" (or another used) installer things like
    - Python
    - Docker, including images like:
        -jupyter/base-notebook
        -python
        -postgres
        -dpage/pgadmin4
3. Creating a few Docker containers using the various commented instruction in the main "Dockerfile" file
4. Starting the Docker containers in the following order: the PostgreSQL one, the Jupyter Notebook, the scrapy_app one
5. Open the Jupyter Notebook Docker container and start all the cells in order to generate plots with various analysis of the data.

Ad.1 - using programs like DBeaver can be useful in order to analyze the scrapped data that is stored in PostgreSQL Docker container. 

## Schema of the project

This project has an almost 100% typical stucture of a standard Scrapy project. However, it has a few differences from the pattern.
First, the folder with the main python code files itself is embedded deeper, inside ./job_scraper/job_scraper folder. The second, as a part of the practicing and experimemnting process, there are a few redundant folders here. Like e.g. "lab2" folder contains two virtual environment. The valid one is however "venv".

The project contains also my backup of the PostgreSQL Docker container database, but in order to use it, you will need to create the PostgreSQL container with a proper command ordering using the backup from the project files. The backup is stored in the folder "data" in the main "lab2" folder.

## Contributing
Here, I want to say thank you to my mentor Wojtek for his great contribution in code review and supporting me everytime when I got stucked somewhere in the project.

## Authors and acknowledgment
It is all my work, with a review and recommendations of my mentor Wojtek.

## License
No special license issued so far, I present it as a result of my work only.

## Project status
It is initaly finished (as 18.09.2023). Unknown if it is going to be developed in the future.
