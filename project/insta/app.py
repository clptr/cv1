from application import create_app
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    # PORT = os.environ.get('PORT')
    # DEBUG = os.environ.get('DEBUG')
    # HOST - os.environ.get('HOST')
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=True)

if __name__ == "__main__":
    main()