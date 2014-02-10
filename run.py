import sys
from app import app

reload(sys)
sys.setdefaultencoding('UTF-8')

if __name__ == "__main__":
    app.run()