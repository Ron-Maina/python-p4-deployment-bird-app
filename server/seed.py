# Import your Flask app instance
from app import app

# Import the existing SQLAlchemy instance (use the same name as in your app initialization)
from models import db,Bird

# Inside the app context, you can use the existing SQLAlchemy instance
with app.app_context():
    # Your database operations here
    print('Deleting existing birds...')
    db.session.query(Bird).delete()

    print('Creating bird objects...')
    chickadee = Bird(
        name='Black-Capped Chickadee',
        species='Poecile Atricapillus',
        image='/images/black-capped-chickadee.jpeg'
    )
    grackle = Bird(
        name='Grackle',
        species='Quiscalus Quiscula',
        image='/images/grackle.jpeg'
    )
    starling = Bird(
        name='Common Starling',
        species='Sturnus Vulgaris',
        image='/images/starling.jpeg'
    )
    dove = Bird(
        name='Mourning Dove',
        species='Zenaida Macroura',
        image='/images/dove.jpeg'
    )

    print('Adding bird objects to transaction...')
    db.session.add_all([chickadee, grackle, starling, dove])
    print('Committing transaction...')
    db.session.commit()
    print('Complete.')