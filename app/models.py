from pydantic import BaseModel, HttpUrl

from . import db


class Link(BaseModel):
    url: HttpUrl


class ToJSONMixin:

    def to_json(self):
        return {column.name: str(getattr(self, column.name)) for column in self.__table__.columns}


class ShortURL(db.Model, ToJSONMixin):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(1024), unique=True, nullable=False)
    url_id = db.Column(db.String(50), unique=True, nullable=False, index=True)

    def __repr__(self):
        return '%r' % self.url_id
