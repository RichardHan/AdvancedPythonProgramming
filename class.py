# Class Declaration
class User(object):
    is_staff = False

    def __init__(self, name='Anonymous'):
        self.name = name
        super(User, self).__init__()

    def is_authorized(self):
        return self.is_staff

test_user = User()
print test_user.name
print test_user.is_authorized()

# Class Inheritance
class SuperUser(User):
    is_staff = True

richard = SuperUser("Richard")
print richard.name
print richard.is_authorized()

# Python way
# No interface
# No real private attributes/functions
# Private attribute start with double underscore (but do not end)
# Special class methods start and end with double underscore.
# like __init__ , __doc__

# import datetime into current namespace
import datetime
print datetime.datetime.now()
print datetime.timedelta(days=30)

# import datetime and addes data and timedelta into namespace
from datetime import datetime , timedelta
print datetime.now()
print timedelta(days=25)