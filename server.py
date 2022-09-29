from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
#this is always at the top



@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<insertword>')
def say(insertword):
    print(insertword)
    return f"Hi {insertword}!"

@app.route('/repeat/<int:insertnumber>/<insertword>')
def repeat(insertnumber, insertword):
    print(insertnumber, insertword)
    return insertword * insertnumber


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
#this is always at the bottom
