from flask import render_template, request, Blueprint
from flaskblog.models import Post
main = Blueprint('main', __name__)


@main.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(per_page=5, page=page)

    return render_template("Home.html", posts=posts)


@main.route("/admin")
def admin():
    return render_template("Resume.html")