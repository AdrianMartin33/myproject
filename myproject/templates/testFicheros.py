todos = open('todos.txt', 'a')
print('Sacar la basura.', file=todos)
print('Dar de comer al gato.', file=todos)
print('Terminar los ejericios de Python.', file=todos)
todos.close()
todos = open('todos.txt')
for tasks in todos:
    print(tasks, end='')
todos.close()
