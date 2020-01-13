# IPL Stats

A demo project to visualize some ipl stats

Working Directory = `cd ipl`

## Setup
1. Setup environment variables: `touch .env` and configure.
2. postgresql DB Setup and create database. Make sure the `.env` file is updated or it'll take the default config in `config.py`.
3. Make sure you're running `python3`. Install python dependencies: `pip install -r requirements.txt`.

## Run
`python run.py`

## Build with Docker

`docker build -t ani_ipl .`

## Run Docker container

`docker run -d --name ani_ipl_stat -p 8000:8000 ani_ipl`

![](https://i.imgur.com/JN0r03V.png | width=250x)

[Open web browser](http://localhost:8000)
