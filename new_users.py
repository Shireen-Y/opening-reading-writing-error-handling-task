
class New_users():
    def __init__(self, name):
        self.name = name

    def output_text_file(self, file_name):
        try:
            with open(file_name, 'w+') as file_to_create:
                file_to_create.write(f"The name of the user is {self.name}")
        finally:
            print('Execution done! Program is now closing')