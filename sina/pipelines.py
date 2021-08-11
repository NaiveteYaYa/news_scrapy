# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Text, DateTime, String, Integer
from sqlalchemy.orm import sessionmaker

base = declarative_base()


class Date(base):
    __tablename__ = 'data'
    id = Column(Integer(), primary_key=True)
    times = Column(Text())
    title = Column(Text())
    content = Column(Text())
    type = Column(Text())


class SinaPipeline:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root@localhost:3306/sina', encoding='utf-8')
        base.metadata.create_all(self.engine)
        self.DBsession = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        new = Date()
        new.title = item['title']
        new.times = item['times']
        new.content = item['desc']
        new.type = item['type']

        session = self.DBsession()
        session.add(new)
        session.commit()


        return item
