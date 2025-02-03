import json

class Timetable:
    
    def __init__(self):
        self.__times = []
    
    def get_times (self):
        return self.__times
    
    def add_time (self, course, mounthDay, fileName ):
        data = {}
        data['course'] = course
        data['mounthDay'] = mounthDay
        self.__times.append(data)
        self.update_json(fileName)
    
    def update_time_course (self,course, mounthDay):
        for i in range(len(self.__times)):
            if self.__times[i]['course'] == str(course):
                self.__times[i]['mounthDay'] = str(mounthDay)
                return self.__times[i]['mounthDay']
    
    
    def update_json (self, fileName):
        with open(fileName,'w', encoding='utf-8') as fp:
            json.dump(self.__times,fp, ensure_ascii=False,indent=4)