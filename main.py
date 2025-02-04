from MVC import controller
from MVC import model
from MVC import viwe


mod = model.Timetable()
control = controller.TimetamleController(mod)
vi = viwe.TimeViwe(control)

vi.display_def_action()

""" userName = input('Введите свое имя: ')
curse1 = mod.add_time('HTML', '20 Феврала', userName)
curse2 = mod.add_time('CSS', '16 Октября', userName)
curse3 = mod.add_time('Python', '3 Сентября', userName)
urse3 = mod.add_time('Python', '13 Сентября', userName)

mod.update_time_course('HTML','33 Декабря', userName)
mod.update_time_course('HРML','33 Декабря', userName)

print(mod.get_times()) """