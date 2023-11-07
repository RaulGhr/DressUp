from flask_sqlalchemy import SQLAlchemy
import random

db = SQLAlchemy()


class ClothesModel(db.Model):
    __tablename__ = 'ClothesModel'
    id = db.Column(db.Integer, primary_key=True)
    imagine = db.Column(db.String(100), nullable=False)
    nume = db.Column(db.String(50), nullable=False)
    tip = db.Column(db.String(20), nullable=False)
    loc = db.Column(db.String(15), nullable=False)

    def __init__(self, imagine, nume, tip, loc):
        self.id = random.randint(1, 10 ** 10 - 1)
        self.imagine = imagine + '.png'
        self.nume = nume
        self.tip = tip
        self.loc = loc

    def toDictionar(self):
        return {
            "id": self.id,
            "imagine": self.imagine,
            "nume": self.nume,
            "tip": self.tip,
            "loc": self.loc
        }

    def __repr__(self):
        return f'ID {self.id} Imagine {self.imagine} Nume {self.nume} Tip {self.tip} Loc {self.loc}'


class OutfitModel(db.Model):
    __tablename__ = 'OutfitModel'
    id = db.Column(db.Integer, primary_key=True)
    imagine = db.Column(db.String(100), nullable=False)
    imagineRealitate = db.Column(db.String(100))
    nume = db.Column(db.String(50), nullable=False)
    tip = db.Column(db.String(20), nullable=False)
    headId = db.Column(db.Integer)
    upperId = db.Column(db.Integer)
    lowerId = db.Column(db.Integer)
    shoesId = db.Column(db.Integer)

    def __init__(self, imagine, imagineRealitate, nume, tip, headId, upperId, lowerId, shoesId):
        self.id = random.randint(1, 10 ** 10 - 1)
        self.imagine = imagine
        self.imagineRealitate = imagineRealitate
        self.nume = nume
        self.tip = tip
        self.headId = headId
        self.upperId = upperId
        self.lowerId = lowerId
        self.shoesId = shoesId

    def toDictionar(self):
        return {
            "id": self.id,
            "imagine": self.imagine,
            "imagineRealitate": self.imagineRealitate,
            "nume": self.nume,
            "tip": self.tip,
            "headId": self.headId,
            "upperId": self.upperId,
            "lowerId": self.lowerId,
            "shoesId": self.shoesId

        }

    def __repr__(self):
        return f'ID {self.id} Imagine {self.imagine} Nume {self.nume} Tip {self.tip}'
