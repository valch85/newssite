# newssite
newssite written in python3 (django)

for comments I have used Disqus so for yours account need to change `s.src` param in `news -> templates -> news -> details.html`

in dirrectory `docker_stuff` you will find docker-compose file with necessary components (mysql & elasticsearch servers)
- to run `docker-compose up -d`

- you also need to install requements by run: `pip install -r requirements.txt`

- activate env `source .env/bin/activate`

- migrate data base `python manage.py migrate`

- create django admin user `python manage.py createsuperuser`
