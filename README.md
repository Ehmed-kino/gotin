# Gotin

## Prerequisites


### docker

you can install it from

1 - If you're a mac user https://docs.docker.com/docker-for-mac/

2 - if you're Windows user https://docs.docker.com/docker-for-windows/

### docker-compsoe

Run the following ```pip install docker-compose```

## How to run the app

1- Run ```docker-compose up```

2- Or sometimes the web application start before the database

so you have to run every service separately.

run ```docker-compose up db```

in another tab in the terminal

run ```docker-compose up web```

then got to http://localhost:8000/words

