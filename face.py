from bd import create_todo, add_task, all_tasks

create_todo()

def add_task_interface():
    title = input('Введите заголовок задачи: ')
    description = input('Введите описание задачи: ')
    add_task(title, description)
    print('Задача добавлена успешно!')

def show_tasks():
    tasks = all_tasks()
    if not tasks:
        print('Список задач пуст.')
    else:
        print('Список задач:')
        for task in tasks:
            print(f'{task[0]}. {task[1]} - {task[3]}')

if __name__ == '__main__':
    while True:
        print('\nМеню:')
        print('1. Добавить задачу в список задач.')
        print('2. Показать список задач.')
        print('3. Выйти из программы.')
        choice = input('Выберите действие: ')

        if choice == '1':
            add_task_interface()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            print('Выход из программы.')
            break
        else:
            print('Неверное действие. Попробуйте снова.')