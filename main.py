from flask import Flask, request, render_template

app = Flask(__name__)

# Lista para almacenar las tareas
tareas = [{'task_name': 'Estudiar física'}]

# Ruta principal - Mostrar tareas
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tareas=tareas)

# Ruta para agregar tarea
@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    
    # Validación de que la tarea no esté vacía
    if task_name and len(task_name.strip()) > 0:
        tareas.append({'task_name': task_name, 'completed': False})
    
    return render_template('index.html', tareas=tareas)

# Ruta para marcar tarea como hecha
@app.route('/mark_done', methods=['POST'])
def mark_done():
    task_name_to_mark = request.form.get('task_name_to_mark')
    
    # Buscar la tarea y marcarla como completada
    for task in tareas:
        if task['task_name'] == task_name_to_mark:
            task['completed'] = True
    
    return render_template('index.html', tareas=tareas)

# Ruta para eliminar tarea
@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_name_to_delete = request.form.get('task_name_to_delete')
    
    # Eliminar la tarea
    global tareas
    tareas = [task for task in tareas if task['task_name'] != task_name_to_delete]
    
    return render_template('index.html', tareas=tareas)

if __name__ == '__main__':
    app.run(debug=True)