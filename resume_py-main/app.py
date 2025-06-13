from flask import Flask, render_template

app = Flask(__name__)

# Данные о пользователе (можно заменить на свои)
resume_data = {
    "name": "Варвара Панькова",
    "title": "Python-разработчик",
    "email": "ivan@example.com",
    "phone": "Нельзя звонить",
    "location": "Владивосток, Россия",
    "about": "Опытный Python-разработчик с 50+ лет опыта создания веб-приложений, автоматизации процессов и анализа данных.",
    "skills": [
        "Python", "Flask", "Django", "SQL", "Git", "HTML/CSS", "JavaScript", "REST API", "Верстка"
    ],
    "experience": [
        {
            "position": "Python-разработчик",
            "company": "ООО Фарпост",
            "duration": "2025 - настоящее время",
            "description": "Разработка веб-приложений, интеграция с API, оптимизация производительности и бла бла бла."
        },
        {
            "position": "Стажер-разработчик",
            "company": "ООО Вкусно и точка",
            "duration": "2007 - 2008",
            "description": "Участие в разработке внутренних инструментов, тестирование и документирование."
        }
    ],
    "education": [
        {
            "degree": "Бакалавр Айти Хаба",
            "university": "МГУ им. Золотое Яблоко",
            "year": "2016 - 2030"
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=resume_data)

if __name__ == '__main__':
    app.run(debug=True)