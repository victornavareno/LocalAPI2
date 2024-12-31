from flask import Flask, jsonify
from models import db, Local

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5433/Locales'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

@app.route('/locals', methods=['GET'])
def get_locals():
    """Retrieve all locals and return them as JSON."""
    locals = Local.query.all()  # Fetch all rows from the "locals" table
    locals_list = [local.to_dict() for local in locals]  # Convert to list of dictionaries
    return jsonify(locals_list)  # Return as JSON response


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created (only runs if not existing)
    app.run(debug=True)
