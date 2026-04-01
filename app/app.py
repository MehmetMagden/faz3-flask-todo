from flask import Flask, request, redirect, render_template
import psycopg2
import os


app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "tododb"),
        user=os.environ.get("DB_USER", "todouser"),
        password=os.environ.get("DB_PASSWORD", "todopass")
    )
    
def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS todos(
            id SERIAL PRIMARY KEY,
            task TEXT NOT NULL,
            done BOOLEAN DEFAULT FALSE
        )      
                
                
                
    """)
    conn.commit()
    cur.close()
    conn.close()
    
@app.route("/")
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, task, done FROM todos ORDER BY id")
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO  todos (task) VALUES(%s)", (task,))
        conn.commit()
        cur.close()
        conn.close()
    return redirect("/")

@app.route("/done/<int:todo_id>")
def done(todo_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE todos SET done = NOT done WHERE id = %s", (todo_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
