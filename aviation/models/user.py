from models import db

class User(db.Model):
    name = db.Column(db.String(75))
    email = db.Column(db.String(75), unique = True)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self