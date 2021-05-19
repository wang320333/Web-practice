import os

from flask import render_template

from models import app
from views.demo import demo_blueprint
from views.user import user_blueprint

app.register_blueprint(demo_blueprint)
app.register_blueprint(user_blueprint)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    return render_template(
        "index.html",
        title="Jinja Demo",
        description="Smarter page templates with Flask & Jinja.",
    )


if __name__ == '__main__':
    app.run(debug=False)
