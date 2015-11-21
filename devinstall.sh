#!/bin/bash

virtualenv env-statiq
source env-statiq/bin/activate
pip install -r package.pip

cd static
npm install