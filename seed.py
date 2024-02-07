from app import app
from models import db, Bird

with app.app_context():

    print("Deleting exisiting birds...")
    Bird.query.delete()

    print("Creating bird objects...")
    robin = Bird(name='Robin Robinson', species='Robin')
    bob = Bird(name='Bob Sawyer', species='Cardinal')
    jonny = Bird(name='Jonny Law', species='Hummingbird')
    rachel = Bird(name='Rachel Greene', species='Chicken')

    print('Add bird objects to transaction...')
    db.session.add_all([robin, bob, jonny,rachel])

    print("Committing transaction...")
    db.session.commit()

    print('Complete.')