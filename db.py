class Links(db.Model): 
    ID = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed  = db.Column(db.Integer, default= 0)
    date_created = db.Column(db.DataTime, default = datetime.utcnow)