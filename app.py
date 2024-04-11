from flask import  Flask, render_template
import data_functions
app = Flask(__name__)

@app.route('/')
def index():
    csv_data= data_functions.get_csv_data()
    return render_template('index.html', csv_data= csv_data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port= int("3000"))

