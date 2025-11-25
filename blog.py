from flask import Flask,render_template,url_for

app = Flask(__name__)

posts = [
    {
        'author':'reyan khan',
        'title': 'post 1',
        'content': 'first blog post',
        'posted_on':'October 12, 2025'
    },
    {
        'author':'abc',
        'title': 'post 2',
        'content': 'Demo post',
        'posted_on':'October 15, 2025'
    }
]

#routes
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title ='About')


if __name__ == "__main__":
    app.run(debug=True)