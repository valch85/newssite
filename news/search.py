from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from .models import *
connections.create_connection(hosts=['localhost'], timeout=20)


class NewsPostIndex(DocType):
    news_name = Text()
    pub_date = Date()
    news_desc = Text()


    class Meta:
        index = 'newssite-index'


#def gendata():
#    for news_name in News.objects.all():
#        yield {
#            "_index": "newssite-index",
#            "_type": "document",
#            "doc": {"news_name": news_name},
#        }
#
#
#def bulk_indexing():
#    NewsPostIndex.init()
#    es = Elasticsearch()
#    bulk(client=es, actions=gendata())

def bulk_indexing():
    NewsPostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(News.indexing(b) for b in News.objects.iterator()))

