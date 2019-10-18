# newssite
Newssite written in python3 + django

For comments used Disqus, to chane account credentials `s.src` param in `news -> templates -> news -> details.html`

Dirrectory `docker_stuff` contain docker-compose file that runs mysql & elasticsearch servers
- to run `docker-compose up -d`

- install requements by run: `pip install -r requirements.txt`

- activate env `source .env/bin/activate`

- migrate data base `python manage.py migrate`

- create django admin user `python manage.py createsuperuser`

- to create and populate the Elasticsearch index and mapping use the search_index command: `./manage.py search_index --rebuild`

- start project: `python manage.py runserver 8000`