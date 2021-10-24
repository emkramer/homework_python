class field():
    __pos_hare = 0
    __pos_turtle = 0
    def __init__(self,n, m, x):
        if n <= m:
            print('неверные данные')
        self.__step_hare = n
        self.__step_turtle = m
        self.__length = x
        
    def get_pos_hare(self):
        return self.__pos_hare
    def get_pos_turtle(self):
        return self.__pos_turtle
    
    def step(self):
        hare_new_pos = self.__pos_hare+self.__step_hare
        if hare_new_pos > self.__length:
            hare_new_pos -= self.__length
        self.__pos_hare = hare_new_pos

        turtle_new_pos = self.__pos_turtle+self.__step_turtle
        if turtle_new_pos > self.__length:
            turtle_new_pos -= self.__length
        self.__pos_turtle = turtle_new_pos

f = field (int(input('Укажите шаг кролика :')), int(input('Введите шаг черепыхи:')), int(input('Укажите длинну поля:')))
i = 0
first_meet = 0
while(i<100):
    f.step()
    i += 1 
    if f.get_pos_hare() == f.get_pos_turtle():
        print('Они встретились через', i - first_meet,'шагов')
        first_meet = i

if first_meet == 0:
    print('Количества циклов недостаточно, чтобы они встретились.')
