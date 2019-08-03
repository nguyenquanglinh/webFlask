from flask import Flask, render_template
from db import get_all_user,add_user,delete_by_name
app = Flask(__name__)


@app.route('/')
def index():
    a=get_all_user()
    return render_template('index.html',user=a)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 