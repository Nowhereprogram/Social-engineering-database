from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# 加载数据
data = pd.read_excel('data.xlsx')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    search_by = request.form['search_by']

    if search_by not in data.columns:
        return "没有查询到结果", 400

    results = data[data[search_by].astype(str).str.contains(query, na=False, case=False)]
    return render_template('results.html', query=query, search_by=search_by, results=results.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
