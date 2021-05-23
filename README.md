# Project 1: Explore Weather Trends

In this project, we will analyze local and global temperature data and compare the temperature trends where you live to overall global temperature trends.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [ssh key](https://docs.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account)
* [python 3](https://realpython.com/installing-python/)
* [poetry](https://python-poetry.org/docs/)

### Installing

```
cd project_1_explore_weather_trends

poetry install

poetry run python explore_weather_trends.py --global_weather ./data/global_weather_trends.csv --local_weather ./data/dallas_weather_trends.csv --local_city Dallas --rolling_average 10```
```

## Authors

* **Larry Johnson**

