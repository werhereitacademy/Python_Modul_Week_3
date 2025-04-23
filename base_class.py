import json,sys
class base_class:

    def __init__(self):
         self.__status = ['completed','Pending']

    def menu_list(self):
        create_menu_list = [
            {
                "text":"Add a new task Press 1",
                "type":"int"
            },
            {
                "text":"Complete a task Press 2",
                "type":"int"
            },
            {
                "text":"Delete a task Press 3",
                "type":"int"
            },
            {
                "text":"List completed tasks Press 4",
                "type":"int"
            },
            {
                "text":"List all tasks with their status Press 5"
                "",
                "type":"int"
            }]
        return create_menu_list
    
    def add_new_task(self):
        try:
            task = input("Please Enter Task")
            status = input("Please Enter status")
            data = self.__read_json_data()
            id = self.__create_sequence_id()
            data.append({"id":id,"task":task,"status":status})
            self.__write_data_in_file(data)
            return "New customer added"
        except Exception as e:
            print(e)
    
    def complete_task(self):
        return "Task has been completed"
    
    def delete_task(self):
        try:
            id = int(input("Please Enter the task id which you want to delete "))
            data = self.__read_json_data()
            filtered_data = [item for item in data if item["id"] != id]
            self.__write_data_in_file(filtered_data)
            return "Successfully deleted"
        except:
            print("There is some Error")
    def view_list_task(self):
        try:
            data = self.__read_json_data()
            text = ''
            for i in data:
               text += "SR.NO: "+str(i['id'])+" Task: "+i['task']+" Status: "+i["status"]+"\n"
            return text
        except Exception as e:
            print("There is some error to read data")

    def __find_missing_numbers(self,seq):
        if not seq:
            return 1
        full_range = set(range(min(seq), max(seq) + 1))
        missing = sorted(full_range - set(seq))
        if not missing:
            return max(seq) + 1
        else:
            return missing[0]
    
    def __create_sequence_id(self):
        data = self.__read_json_data()
        list_id = []
        for ids in data:
            list_id.append(ids["id"])
        return self.__find_missing_numbers(list_id)

    def __read_json_data(self):
        try:
            f = open('data.json')
            data = json.load(f)
            f.close()
            return data
        except Exception as e:
            print("There is some error to reada data")
        
    def __write_data_in_file(self,data):
        try:
            data = sorted(data, key=lambda x: x["id"])
            with open("data.json",'w') as file:
                file.seek(0)
                return json.dump(data, file, indent = 4)
        except:
            return "There is some error to data write in file"