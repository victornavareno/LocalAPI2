from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Local(db.Model):
    __tablename__ = 'locals'  # Explicitly set the table name

    id_local = db.Column(db.Integer, primary_key=True)  # Correct primary key column
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    events = db.Column(db.ARRAY(db.Integer), nullable=True)

    def to_dict(self):
        """Convert model instance to a dictionary for JSON response."""
        return {
            'id_local': self.id_local,
            'name': self.name,
            'city': self.city,
            'address': self.address,
            'events': self.events,
        }
