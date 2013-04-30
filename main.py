from app import app, db
from models import *
from views import *

def run():
    import os
    host = "0.0.0.0"
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port, debug=True)


if __name__ == '__main__':
    run()
