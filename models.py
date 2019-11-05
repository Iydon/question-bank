#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File      : models.py
@Time      : 2019/11/05
@Author    : Iydon Liang
@Contact   : liangiydon@gmail.com
@Docstring : <no docstring>
'''

from sqlalchemy import create_engine, ForeignKey, \
	Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Type(Base):
	__tablename__ = "types"
	id = Column(Integer, primary_key=True)
	name = Column(String(64), unique=True)
	pattern = Column(Text)
	questions = relationship('Question', backref='type', lazy='dynamic')

	def __repr__(self):
		return f'<Type {self.id}>'


class Tag(Base):
	__tablename__ = "tags"
	id = Column(Integer, primary_key=True)
	name = Column(String(64), unique=True)
	questions = relationship('Question', backref='tag', lazy='dynamic')

	def __repr__(self):
		return f'<Tag {self.id}>'


class Question(Base):
	__tablename__ = "questions"
	id = Column(Integer, primary_key=True)
	description = Column(Text)
	score = Column(Integer)
	difficulty = Column(Integer)
	answer = Column(Text)
	analysis = Column(Text)
	type_id = Column(Integer, ForeignKey('types.id'))
	tag_id = Column(Integer, ForeignKey('tags.id'))

	def __repr__(self):
		return f'<Question {self.id}>'


if __name__ == "__main__":
	import os

	basedir = os.path.abspath(os.path.dirname(__file__))
	database_url = "sqlite:///" + os.path.join(basedir, "data.sqlite")
	engine = create_engine(database_url)
	DBSession = sessionmaker(bind=engine)

	Base.metadata.create_all(engine)
	session = DBSession()
