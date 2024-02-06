from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update_excel():
    data = request.json['data']
    df = pd.DataFrame(data[1:], columns=data[0])  # Assuming the first row is headers
    excel_path = 'file://hpalmuft-gp01.ec.win.colpal.com/Results/'  # Update this path
    df.to_excel(excel_path, index=False)
    return jsonify({"message": "Excel file updated successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
