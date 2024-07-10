from flask import Flask, render_template

app = Flask(__name__)

class Task:
    def __init__(self, id, title, difficulty, completed=False):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.completed = completed

tasks = []

@app.route('/add_task', methods=['POST'])
def add_task():
    """
    팀원 1: 할 일 추가 기능
    """
    # 할 일 추가 로직 구현 필요
    pass
