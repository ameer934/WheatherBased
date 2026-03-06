
# 🌬️ Weather-Based Prediction of Wind Turbine Energy

This project predicts wind turbine energy output based on weather conditions using Machine Learning. It also includes a web interface built with Flask to make predictions easily.

---

## 🚀 Features

- 📊 Train a machine learning model on weather data  
- 🤖 Predict wind turbine energy output  
- 🌐 User-friendly web interface  
- 🧠 Model built using Python and saved for reuse  

---

## 🛠️ Tech Stack

- Python  
- Flask  
- HTML/CSS  
- Machine Learning (Scikit-learn / Pandas / NumPy)

📁 Project Structure (Explained)

The project is divided into two main parts: the Flask web application and the machine learning module.

The flask_app folder contains everything related to the web interface. Inside it, the templates folder stores the HTML pages used in the application, such as the introduction page and the prediction page. The static folder holds static assets like images. The file windApp.py is the main Flask application that runs the server, handles user input, and displays prediction results.

The model_training folder contains the machine learning components of the project. The script train_model.py is used to train the prediction model using the dataset traindata.csv. This part of the project is responsible for learning patterns from weather data to estimate wind turbine energy output.

At the root level of the project, the .gitignore file ensures unnecessary or sensitive files are not uploaded to GitHub. The README.md file provides documentation about the project, and requirements.txt lists all the Python libraries needed to run the application.

## ⚙️ How to Run This Project

### 1️⃣ Clone the Repository

    git clone https://github.com/YOUR-USERNAME/WeatherBased
   

2️⃣ Install Dependencies

    pip install flask pandas numpy scikit-learn

3️⃣ Train the Model (Optional)
   
    python model_training/train_model.py

4️⃣ Run the Flask App
   
    python flask_app/windApp.py

Then open your browser and go to:

      http://127.0.0.1:5000

📈 How It Works

Weather data is used to train a regression model.

The model learns patterns between weather parameters and wind energy output.

The Flask app takes user input and predicts energy generation.

🔒 Notes

.env and model files are not uploaded for security and size reasons.

You can retrain the model using the provided dataset.


## 🎥 Project Demo Video

https://drive.google.com/drive/home 


## 👩‍💻 Author's

Shaik Areef
Shai Ameer Basha
Phaneendra Gangadi

Project developed for learning Machine Learning + Web Integration.

⭐ If you like this project, give it a star!


