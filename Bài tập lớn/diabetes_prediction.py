import streamlit as st
import numpy as np
import joblib

# Tải mô hình đã huấn luyện
MODEL_PATH = 'best_model.pkl'  # Đường dẫn tới file model
best_model = joblib.load(MODEL_PATH)  # Sử dụng joblib.load thay cho pickle.load

# Giao diện Streamlit
st.title("Dự Đoán Nguy Cơ Mắc Bệnh Tiểu Đường")

# Nhập dữ liệu người dùng
weight = st.number_input("Cân nặng (kg):", min_value=1.0, max_value=200.0, value=70.0, step=0.1)
height = st.number_input("Chiều cao (cm):", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
blood_glucose = st.number_input("Chỉ số đường huyết (mg/dL):", min_value=50.0, max_value=300.0, value=100.0, step=0.1)
physical_activity = st.number_input("Hoạt động thể chất (phút/ngày):", min_value=0, max_value=300, value=30, step=1)
bmi = st.number_input("Chỉ số BMI:", min_value=10.0, max_value=50.0, value=24.0, step=0.1)

diet = st.selectbox("Chế độ ăn uống:", ["Lành mạnh", "Không lành mạnh"])
medication_adherence = st.selectbox("Tuân thủ thuốc:", ["Tốt", "Kém"])
stress_level = st.selectbox("Mức độ căng thẳng:", ["Thấp", "Trung bình", "Cao"])
hydration_level = st.selectbox("Trạng thái uống nước đầy đủ:", ["Có", "Không"])
sleep_hours = st.number_input("Thời gian ngủ (giờ/ngày):", min_value=0.0, max_value=24.0, value=8.0, step=0.1)

# Chuyển đổi đầu vào dạng số
diet_mapping = {"Lành mạnh": 0, "Không lành mạnh": 1}
medication_adherence_mapping = {"Tốt": 0, "Kém": 1}
stress_level_mapping = {"Thấp": 0, "Trung bình": 1, "Cao": 2}
hydration_level_mapping = {"Có": 0, "Không": 1}

diet = diet_mapping[diet]
medication_adherence = medication_adherence_mapping[medication_adherence]
stress_level = stress_level_mapping[stress_level]
hydration_level = hydration_level_mapping[hydration_level]

# Xử lý đầu vào thành mảng
input_data = np.array([[weight, height, blood_glucose, physical_activity, bmi, 
                        diet, medication_adherence, stress_level, hydration_level, sleep_hours]])

# Dự đoán và hiển thị kết quả
if st.button("Dự đoán"):
    prediction = best_model.predict(input_data)
    risk = "Nguy cơ cao" if prediction[0] == 1 else "Nguy cơ thấp"
    st.write(f"Kết quả dự đoán: **{risk}**")
