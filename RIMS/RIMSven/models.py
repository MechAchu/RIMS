from RIMSven import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    using = db.relationship('Tools', backref='Using', lazy=True)

    def __repr__(self):
        return f"Users('{self.id}', '{self.first_name}', '{self.last_name}', '{self.grade}')"

class Tools(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(20), unique=True, nullable=False)
    borrow = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"Tools('{self.id}', '{self.name}', '{self.size}', '{self.location}', '{self.borrow}')"

class Consumables(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(20), unique=True, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Consumables('{self.id}', '{self.name}', '{self.size}', '{self.location}', '{self.amount}')"
