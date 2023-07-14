# import render_template and request from flask
from flask import Flask, render_template, request

app = Flask(__name__, static_folder="static")
app.use_static_for_root = True

# Set methods parameter as ["GET", "POST"]
@app.route("/")
def home():
    # If request.method is "GET" the return render_template('index.html')
    return render_template('index.html')

    
    
        # Else get the sender, receiver, amount using request.form.get() method
    
        
        # Print sender, receiver, amount on console
    
        
        # Return render_template('index.html)
        

if __name__ == '__main__':
    app.run(debug = True)