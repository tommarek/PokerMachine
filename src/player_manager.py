#!/usr/bin/python3

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.sqlalchemy_declarative import Base, Player

class PlayerNotFound(Exception): pass

class PlayerManager():
    _session = None
    def __init__(self, dbfile):
        try:
            engine = create_engine(f"sqlite:///db/{dbfile}")
            Base.metadata.bind = engine
            DBSession = sessionmaker(bind=engine)
            self._session = DBSession()
        except Exception as e:
            raise

    @contextmanager
    def session_scope(self):
        try:
            yield self._session
            self._session.commit()
        except:
            self._session.rollback()
            raise

    def add_new_player(self, pid):
        with self.session_scope() as session:
            p = session.query(Player).filter(Player.pid == pid).first()
            if not p:
                p = Player(pid=pid)
                session.add(p)
            return p

    get_player = add_new_player

    def update_stats(self, pid, stats):
        with self.session_scope() as session:
            query = session.query(Player).filter_by(pid=pid)
            query.update(stats)

