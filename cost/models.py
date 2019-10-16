from cost import db

class Calculation(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
   
    cost_price=db.Column(db.Integer,nullable=False)
    discount=db.Column(db.Integer,nullable=False)
    mark_up=db.Column(db.Integer(),nullable=False)
    selling_price=db.Column(db.Integer(),nullable= False)


    def __repr__(self):
        return "product {}".format(self.name)