# Job Bot

_A simple telegram bot that aggregates statistical data on the salaries of company employees by time intervals._

# DEMO

Just click and try to use on [Telegram](https://t.me/Jobtest_findbot)

Input data format:

`{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}`  
`{"dt_from": "2022-10-01T00:00:00", "dt_upto": "2022-11-30T23:59:00", "group_type": "day"}`  
`{"dt_from": "2022-02-01T00:00:00", "dt_upto": "2022-02-02T00:00:00", "group_type": "hour"}`

## Installation

Clone the repository:

`git@github.com:Georgyphyton/Job-bot.git`

Go to the project folder:

`cd job-bot`

Install dependencies with Poetry:

`make install`

If you don't have Poetry, use:

`make activate`

## Database preparation

`make db_init`

## Settings

Create an ".env" file in the root project directory: 

`cp .env.sample .env`

Write following constants to the .env file:

1. `TOKEN='your_Bot_Token'` 

You can generate one [here](https://t.me/BotFather)

2. `DATABASE_URL='your_mongodb_database_url_path'`

The following is the standard URI connection scheme:

`mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]`

## Start project

`make run`

Now you can use your bot
