# Import necessary modules
# Import necessary modules
from flask import Flask, request
from peewee import *

# Connect to the SQL database
db = SqliteDatabase('painting_database.db')

# Create the model for the dataset
class Painting(Model):
    title = CharField()
    artist = CharField()
    year = IntegerField()
    headwear = CharField()
    
    class Meta:
        database = db

# Initialize the Flask app
app = Flask(__name__)

# Create endpoint for Create operation
@app.route('/create', methods=['POST'])
def create():
    # Extract the data from the request
    data = request.get_json()
    title = data['title']
    artist = data['artist']
    year = data['year']
    headwear = data['headwear']
    
    # Create a new record in the database
    new_painting = Painting(title=title, artist=artist, year=year, headwear=headwear)
    new_painting.save()
    
    # Return success message
    return {"message": "Painting added to database."}, 201

# Create endpoint for Read operation
@app.route('/read/<id>', methods=['GET'])
def read(id):
    # Retrieve the specified record from the database
    painting = Painting.get(Painting.id == id)
    
    # Return the record data
    return {"title": painting.title, "artist": painting.artist, "year": painting.year, "headwear": painting.headwear}, 200

# Create endpoint for Delete operation
@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    # Retrieve the specified record from the database
    painting = Painting.get(Painting.id == id)
    
    # Delete the record
    painting.delete_instance()
    
    # Return success message
    return {"message": "Painting deleted from database."}, 200

# Run the Flask app
if __name__ == '__main__':
    db.connect()
    db.create_tables([Painting], safe=True)
    app.run()