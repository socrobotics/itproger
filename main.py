import time
import threading


def sleepTime(wait, name):
    print(f'Выводим текст: {name}')
    time.sleep(wait)
    print(f'Выводим текст повторно: {name}')


# td.join() работает пока не завершится неосновной поток

start = time.time()

t_list = []

for i in range(5):
    name = 'SleepTime: ' + str(i + 1)
    print(f'{name} был запущен')
    td = threading.Thread(target=sleepTime, name='SleepTime', args=(3, name))
    td.start()
    t_list.append(td)

# #Чтобы выполнялось не паралельно основному потоку
# for t in t_list:
#     t.join()

# for i in range(5):
#     sleepTime(3, i + 1)

end = time.time()

print('Время обработки: ', (end - start))
print('Завершил потоки')
