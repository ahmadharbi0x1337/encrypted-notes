"""
Flask application runner script.
Allows app to be started using `python run.py` or `flask run`.
"""

from app import create_app

# Create the app instance
app = create_app()

if __name__ == "__main__":
    # Only run developement server when executed directly.
    app.run(debug=True)