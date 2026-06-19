## 🎓 Student Performance Prediction System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📖 Overview

The **Student Performance Prediction System** is a Machine Learning-based web application that predicts whether a student is likely to **Pass** or **Fail** based on academic performance indicators such as:

* Study Hours
* Attendance Percentage
* Assignment Score
* Previous Marks

The application uses a trained machine learning model and provides prediction results along with the probability of passing through a user-friendly Flask web interface.

---

## ✨ Features

* Predicts student academic performance
* Simple and interactive web interface
* Displays probability of passing
* Input validation for realistic student data
* Machine Learning model integration
* Easy to train and deploy

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Model Storage

* Pickle (.pkl)

---

## 📂 Project Structure

```text
Student-Performance-Prediction-System/
│
├── app.py
├── generate_student_data.py
├── train_model.py
├── student_data.csv
├── student_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/student-performance-prediction.git

cd student-performance-prediction
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

Or using requirements file:

```bash
pip install -r requirements.txt
```

---

## 📊 Train the Model

Generate dataset:

```bash
python generate_student_data.py
```

Train model:

```bash
python train_model.py
```

This will create:

```text
model/student_model.pkl
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## 💡 Usage Example

Enter the following values:

| Input            | Example |
| ---------------- | ------- |
| Study Hours      | 8       |
| Attendance       | 90      |
| Assignment Score | 9       |
| Previous Marks   | 85      |

Output:

```text
Prediction: PASS
Probability of Passing: 95%
```

---

## 🧠 Machine Learning Workflow

1. Generate student performance dataset
2. Preprocess data
3. Train classification model
4. Save model using Pickle
5. Load model in Flask application
6. Predict student result from user input

---

## 🎯 Future Improvements

* Neural Network implementation using TensorFlow/Keras
* Student grade prediction (A, B, C, D)
* Data visualization dashboard
* Database integration
* User authentication
* Deployment on Render/Heroku/AWS

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 🆘 Support

If you encounter any issues:

* Open an issue in the GitHub repository
* Review the project documentation
* Contact the maintainer

---

## 👩‍💻 Maintainer

**Nethi Sri Varsha**

B.Tech CSE (AIML) Student
Malla Reddy Deemed to be University

GitHub: https://github.com/srivarsha3

---

## 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

### ⭐ If you found this project useful, please give it a star on GitHub!

