import os
from flask import Flask, request, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    # ИСПРАВЛЕНИЕ 1: Использование переменных окружения
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))
    
    # ИСПРАВЛЕНИЕ 2: Debug mode off в production
    app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    
    @app.route('/')
    def index():
        # ИСПРАВЛЕНИЕ 3: Безопасное экранирование ввода
        name = request.args.get('name', 'Guest')
        return render_template('index.html', name=name)
    
    @app.route('/eval')
    def eval_code():
        # ИСПРАВЛЕНИЕ 4: Удалена опасная функция eval()
        return 'This endpoint is disabled for security', 403
    
    @app.route('/admin')
    def admin():
        # ИСПРАВЛЕНИЕ 5: Добавлена проверка аутентификации
        auth_token = request.headers.get('Authorization')
        expected_token = os.environ.get('ADMIN_TOKEN')
        if not auth_token or auth_token != f'Bearer {expected_token}':
            return 'Unauthorized', 401
        return 'Admin panel'
    
    return app