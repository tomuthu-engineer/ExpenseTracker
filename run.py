from APIs import create_app
from load_dotenv import DEBUG , PORT,HOST

if __name__=='__main__':
    app=create_app()
    app.run(debug=DEBUG,port=PORT,host=HOST)