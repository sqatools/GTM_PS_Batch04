import os
from datetime import datetime

class CommonUtils:

    def get_unique_name(self):
        return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")


    def create_unique_folder_logs(self):
        logs_path = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(logs_path):
            os.mkdir(logs_path)
        unique_folder_path = os.path.join(f"{logs_path}", self.get_unique_name())
        os.mkdir(unique_folder_path)
        return unique_folder_path



if __name__ == '__main__':
    obj = CommonUtils()
    print(obj.get_unique_name())
    print(obj.create_unique_folder_logs())