Diabetic Prediction Ensemble Model
Overview
This project is an ensemble model for predicting diabetes using machine learning algorithms K-Nearest Neighbors (KNN) and LightGBM. The web application is built using Django for the backend and HTML, CSS, and jQuery for the frontend. The model takes nine input attributes to predict the likelihood of a person having diabetes.

Features
Machine Learning Models: Utilizes KNN and LightGBM to create an ensemble model for prediction.
Web Framework: Built with Django for robust backend support.
Frontend: User-friendly interface designed with HTML, CSS, and jQuery.
Prediction Input: Accepts nine input attributes to provide an accurate prediction.
Input Attributes
The model uses the following nine attributes to predict diabetes:

Pregnancies: Number of times pregnant.
Glucose: Plasma glucose concentration.
Blood Pressure: Diastolic blood pressure (mm Hg).
Skin Thickness: Triceps skin fold thickness (mm).
Insulin: 2-Hour serum insulin (mu U/ml).
BMI: Body mass index (weight in kg/(height in m)^2).
Diabetes Pedigree Function: A function that scores likelihood of diabetes based on family history.
Age: Age of the person.
Activity Level: Level of physical activity.
Installation
Prerequisites
Python 3.x
Django
pip (Python package installer)
Virtual environment tool (optional but recommended)
Setup
Clone the repository: git clone https://github.com/yourusername/diabetic-prediction-ensemble-model.git and cd diabetic-prediction-ensemble-model
Create a virtual environment: python -m venv env and source env/bin/activate (On Windows use env\Scripts\activate)
Install the required packages: pip install -r requirements.txt
Run migrations: python manage.py migrate
Start the Django development server: python manage.py runserver
Open your web browser and navigate to: http://127.0.0.1:8000/
Usage
Home Page: The home page provides a form for the user to input the nine attributes required for prediction.
Input the Data: Enter values for pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, age, and activity level.
Get Prediction: Submit the form to get the prediction result.
Project Structure
/diabetic_prediction/: Django project settings and configuration.
/prediction_app/: Main application containing models, views, and templates.
models.py: Contains the Django models.
views.py: Contains the view functions to handle requests and responses.
templates/: Contains the HTML templates for the frontend.
static/: Contains static files such as CSS and JavaScript.
/machine_learning/: Directory for machine learning model scripts and data processing.
requirements.txt: Lists all the Python packages required for the project.
Machine Learning Model Details
Training the Models
K-Nearest Neighbors (KNN):

A simple, instance-based learning algorithm used for classification.
Works by finding the k-nearest data points and predicting the label based on the majority vote.
LightGBM:

A gradient boosting framework that uses tree-based learning algorithms.
Known for its efficiency and speed in handling large datasets.
Ensemble Approach
The predictions from both KNN and LightGBM models are combined to form an ensemble prediction.
This approach leverages the strengths of both models to improve prediction accuracy.
Model Training Script
train_models.py: Contains the script to train and save the machine learning models.
Ensure you have the necessary libraries installed (e.g., scikit-learn, lightgbm) and your dataset prepared for training.
Dataset
The dataset used for training the models should include the nine attributes mentioned above and the target variable indicating diabetes status.
Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are reviewed and merged when appropriate.

Fork the repository: git fork https://github.com/yourusername/diabetic-prediction-ensemble-model.git
Create your feature branch: git checkout -b feature/YourFeature
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/YourFeature
Open a pull request.

![image](https://github.com/Kunali25/Ensemble/assets/128252521/b87ffab5-412f-4f08-8278-3480bec9d5b2)

![image](https://github.com/Kunali25/Ensemble/assets/128252521/7ddb2538-0c99-4cf0-98de-a1bb84fcf1d7)

![image](https://github.com/Kunali25/Ensemble/assets/128252521/c59c36c8-9b62-4ccb-8d6e-fecc23433f7c)

![image](https://github.com/Kunali25/Ensemble/assets/128252521/e6f353ab-6ff2-463d-a6ae-8dcf6cd970c6)




Contact
If you have any questions or suggestions, feel free to contact me at kunaliyyappan25@@example.com.
