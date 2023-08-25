from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    # Perform operations with the form data
    # You can access the values using data['dropdown1'], data['dropdown2'], etc.
    
    # Example: Print the form data
    print("Dropdown 1:", data['dropdown1'])
    print("Dropdown 2:", data['dropdown2'])
    print("Dropdown 3:", data['dropdown3'])
    print("Dropdown 4:", data['dropdown4'])
    
    # You can return a response to the front-end if needed
    return jsonify({'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run()