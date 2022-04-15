#!/bin/sh
git add .
git commit -m "update"
git push heroku main
heroku logs -n 20
