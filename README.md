Sample App to showcase continous integration with travisCI

[![Build Status](https://travis-ci.org/nesh-dev/moringa-CI-intgration-example.svg?branch=master)](https://travis-ci.org/nesh-dev/moringa-CI-intgration-example) [![Coverage Status](https://coveralls.io/repos/github/nesh-dev/moringa-CI-intgration-example/badge.svg?branch=master)](https://coveralls.io/github/nesh-dev/moringa-CI-intgration-example?branch=master)


### Installation and Setup

- Clone the repo

    `git clone https://github.com/nesh-dev/Store-Manager-API.git`

- Switch the develop branch

    `git fetch origin develop`

- Navigate to the folder

    `cd Store-Manager-API`

- create a virual env

    `virtualenv env`

- Activate the env

    `source/env/activate`

- Install the required packages

    `pip install -r requirements.txt`

- Install Postgresql

    `CREATE DATABASE standup`

- Run configurations
  configurations for the app are contained in the sample.env you can copy and paste the structure  and add it to a .env file

   `$ cp sample.env .env`

- navigate back to root and run app
    `make serve`
