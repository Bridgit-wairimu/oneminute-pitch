import unittest
from app.models import Comment,User,Pitch
from app import db

class CommentModelTest(unittest.TestCase):


    def setUp(self):
            self.user_postgres = User(username = 'kayleen',password = 'password', email = 'kayleen@gmail.com')
            self.new_comment = Comment(comment='nice work',user = self.user_kayleen,pitch_id=1 )

    

   
