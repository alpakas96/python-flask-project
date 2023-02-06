# Import necessary modules
from flask import Flask, request
from peewee import *

# Connect to the SQL database
db = SqliteDatabase('my_database.db')

# Create the model for the dataset
class MyModel(Model):
    field1 = CharField()
    field2 = CharField()
    
    class Meta:
        database = db

# Initialize the Flask app
app = Flask(__name__)

# Create endpoint for Create operation
@app.route('/create', methods=['POST'])
def create():
    # Extract the data from the request
    data = request.get_json()
    field1 = data['field1']
    field2 = data['field2']
    
    # Create a new record in the database
    new_record = MyModel(field1=field1, field2=field2)
    new_record.save()
    
    # Return success message
    return {"message": "Record created successfully."}, 201

# Create endpoint for Read operation
@app.route('/read/<id>', methods=['GET'])
def read(id):
    # Retrieve the specified record from the database
    record = MyModel.get(MyModel.id == id)
    
    # Return the record data
    return {"field1": record.field1, "field2": record.field2}, 200

# Create endpoint for Delete operation
@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    # Retrieve the specified record from the database
    record = MyModel.get(MyModel.id == id)
    
    # Delete the record
    record.delete_instance()
    
    # Return success message
    return {"message": "Record deleted successfully."}, 200

# Run the Flask app
if __name__ == '__main__':
    db.connect()
    db.create_tables([MyModel], safe=True)
    app.run()
