# newssite
newssite written in python (django)

in dirrectory `docker_stuff` you will find docker-compose file with necessary components (mysql, elasticsearch servers)
tu use: `docker-compose up -d`

for comments I have used Disqus so for yours account need to change `s.src` param in `news -> templates -> news -> details.html`

you also need to install requements: `pip install -r requirements.txt`