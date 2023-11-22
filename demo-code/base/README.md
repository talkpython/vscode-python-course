# Podcast API demo

This podcast web API was put together as the demo application for the [Visual Studio Code for Python Developers]() course at [Talk Python training](https://training.talkpython.fm/).

## Prerequisites

* [Python 3.11+](https://www.python.org/downloads/)
* [Visual Studio Code](https://code.visualstudio.com/download)

## Starting the API 🚀

Create virtual environment

```shell
python -m venv .venv
```

Activate virtual environment. VS Code should prompt you for this, but you can do this manually.

```shell
source .venv/bin/activate
```

Install project dependencies

```shell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the project. Using the '-g' switch will load the sample data into [tinydb](https://tinydb.readthedocs.io/)

```shell
python -m podcastapi -g
```
