#!/bin/bash

exec gunicorn -b 0.0.0.0:5003 "app:create_app()" --reload

"$@"
