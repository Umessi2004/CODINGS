from appl import create_app
from appl import db

appln=create_app()

if __name__=='__main__':
    with appln.app_context():
        db.create_all()
    appln.run(debug=True)