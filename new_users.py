
class New_users():
    def __init__(self, name):
        self.name = name


# Creating new text file

def new_file(new_user_file):
    create_file = open(new_user_file, 'w')
    return create_file
