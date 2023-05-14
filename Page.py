from flask import Flask , render_template
 
Page = Flask(__name__)
@Page.route('/')
def home():
    return render_template('head.html')

@Page.route('/about')
def about():
    return render_template('about.html')

@Page.route('/description')
def description():
    return 'this is page description'

if __name__ == '__main__':
    Page.run(debug=True) 