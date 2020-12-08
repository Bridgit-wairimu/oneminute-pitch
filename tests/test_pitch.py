import unittest
from app.models import Comment,User,Pitch
from app import db

class PitchModelTest(unittest.TestCase):


    def setUp(self):
            self.user_postgres = User(username = 'betty',password = 'password', email = 'betty@gmail.com')
            self.new_pitch = Pitch(pitch='dont create a mountain ontop of a mole hill',user = self.user_betty,pitch_id=3 )

    