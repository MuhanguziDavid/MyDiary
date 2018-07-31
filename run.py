"""Api enpoint logic"""
from api import app
import config

if __name__ == '__main__':
    app.run(port=5000, debug=True)
