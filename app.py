from flask import Flask

app = Flask(__name__)

@app.route('/')
def my_index_view():
    return 'Дом нот'

if __name__ == '__main__':
    app.run()
