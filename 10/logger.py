from datetime import datetime as dt
#
# Почему формат файла ".csv" - фиг пойми, взял просто из примеров
def log_to_file(arg1, arg2, operation, result):
    path = 'logging.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a')
    f.write(f'{time_sign}--> {arg1} {operation} {arg2} = {result}\n')
    f.close()
#
# Вызов и использование:
# В Контроллере, вот в этот (и в другие три) блок кода:
    # if value_model == 1: ###
    #     model.init(value_a, value_b)
    #     result = model.do_it()
    #     user.view_data(result)
# вставить строку (только операцию "+" настроить в каждом случае):
#   logger.log_to_file(x, y, "+", result)
# ...а также, конечно, импорт Логгера в начале Контроллера
#
# Тест-код, чтобы испытать метод "log_to_file", раскомментить и запустить
# log_to_file(123.45, 456.78, '+', 789.12)
# aa = 1.11 + 2.22j
# bb = 3.33 + 4.44j
# cc = aa + bb
# log_to_file(aa, bb, '+', cc)
