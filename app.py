from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Connection Config
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="Wabbit10Interstellar",  
        database="task_manager_db"  
    )
    return conn

# Home route to display tasks
@app.route('/', methods=['GET'])
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Add new task route
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['task_content']  # Get task content from the form
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (content) VALUES (%s)', (task_content,))
    conn.commit()  # Commit the transaction
    conn.close()
    return redirect(url_for('index'))

# Delete task route
@app.route('/delete/<int:id>')
def delete_task(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id=%s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)