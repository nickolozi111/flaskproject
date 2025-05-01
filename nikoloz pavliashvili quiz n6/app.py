from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = ["Buy groceries", "Clean the house", "Read a book"]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = request.form['task']
        if new_task:
            tasks.append(new_task)
        return redirect(url_for('index'))
    return render_template('add_task.html')

if __name__ == '__main__':
    app.run(debug=True)
