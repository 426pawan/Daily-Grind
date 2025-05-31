from flask import Flask, render_template, request, redirect, url_for, abort, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'  # Needed for flashing messages

db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Todo {self.sno} - {self.title}>"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form.get('title').strip()
        desc = request.form.get('desc').strip()
        if not title or not desc:
            flash('Title and Description cannot be empty!', 'warning')
        else:
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
            flash('Todo added successfully!', 'success')
        return redirect(url_for('hello_world'))

    allTodo = Todo.query.order_by(Todo.date_created.desc()).all()

    # Simple search functionality (optional)
    search_query = request.args.get('q', '').strip()
    if search_query:
        allTodo = Todo.query.filter(
            (Todo.title.ilike(f'%{search_query}%')) |
            (Todo.desc.ilike(f'%{search_query}%'))
        ).order_by(Todo.date_created.desc()).all()

    return render_template('index.html', allTodo=allTodo)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.get_or_404(sno)
    if request.method == 'POST':
        title = request.form.get('title').strip()
        desc = request.form.get('desc').strip()
        if not title or not desc:
            flash('Title and Description cannot be empty!', 'warning')
            return redirect(url_for('update', sno=sno))
        todo.title = title
        todo.desc = desc
        db.session.commit()
        flash('Todo updated successfully!', 'success')
        return redirect(url_for('hello_world'))
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.get_or_404(sno)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted successfully!', 'success')
    return redirect(url_for('hello_world'))

# Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(debug=True)