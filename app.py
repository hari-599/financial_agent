# app.py
from flask import Flask, render_template, request
from flask_caching import Cache
from model import get_agent
import markdown as md

app = Flask(__name__)

# Simple in-memory caching
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

@app.route('/', methods=['GET', 'POST'])
def index():
    response_html = ""
    recommendation =None
    
    if request.method == 'POST':
        user_input = request.form['user_input'].strip()
        if not user_input:
            return render_template('index.html', response="Please enter a query.")

        # Check if cached
        cached_response = cache.get(user_input)
        if cached_response:
            return render_template('index.html', response=cached_response)

        try:
            agent = get_agent()
            result = agent.run(user_input)
            markdown_response = result.content if hasattr(result, 'content') else result
            response_html = md.markdown(markdown_response, extensions=["tables", "fenced_code"])
            
            # Cache result
            cache.set(user_input, response_html, timeout=300)  # Cache for 5 minutes
        except Exception as e:
            response_html = f"<p style='color:red;'>An error occurred: {str(e)}</p>"

    return render_template('index.html', response=response_html,recommendation=recommendation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
