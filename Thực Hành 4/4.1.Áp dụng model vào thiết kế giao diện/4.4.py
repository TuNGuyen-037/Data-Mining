from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Tải mô hình Decision Tree
model = joblib.load('decision_tree_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Lấy dữ liệu từ POST request
    height = data['height']
    weight = data['weight']
    
    # Dự đoán với mô hình Decision Tree
    prediction = model.predict([[height, weight]])  # Mô hình nhận vào dữ liệu (height, weight)
    
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
