from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def index():
    # This function renders the HTML template named 'index.html'.
    # We pass a variable 'title' to the template.
    page_title = "Welcome to My Simple Flask App"
    return render_template('index.html', title=page_title)

# Optional: Define another simple route
@app.route('/about')
def about():
    # Render the same template but with a different title
    return render_template('index.html', title="About This Project")

# Run the application
# The 'debug=True' option automatically reloads the server when you make changes.
if __name__ == '__main__':
    app.run(debug=True)