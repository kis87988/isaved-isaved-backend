from app.__init__ import db
db = db


class UserTagTable(db.Model):
    """ Initialize the user_tag_table from MySQL database

    +----------------+---------------+------+-----+---------+----------------+
    | Field          | Type          | Null | Key | Default | Extra          |
    +----------------+---------------+------+-----+---------+----------------+
    | userID         | int(11)       | NO   |     | NULL    |                |
    | itemID         | int(11)       | NO   | PRI | NULL    | auto_increment |
    | Link           | varchar(1000) | YES  |     | NULL    |                |
    | CreateTime     | datetime      | NO   |     | NULL    |                |
    | Tag            | varchar(1000) | YES  |     | NULL    |                |
    | Title          | varchar(1000) | YES  |     | NULL    |                |
    | LastUpdateTime | datetime      | NO   |     | NULL    |                |
    +----------------+---------------+------+-----+---------+----------------+
    """

    userID = db.Column(db.Integer, unique=False, nullable=False, primary_key=False)
    itemID = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Link = db.Column(db.String(1000))
    Tag = db.Column(db.String(1000))
    Title = db.Column(db.String(1000))
    CreateTime = db.Column(db.DateTime)
    LastUpdateTime = db.Column(db.DateTime)

    def __str__(self):
        return str(self.userID) + ' ' + str(self.itemID) + ' ' + str(self.Link) + ' ' + str(self.Tag) +' ' +  str(self.Title) + ' ' + str(self.CreateTime) + ' ' + str(self.LastUpdateTime)
