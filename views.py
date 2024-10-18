from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from lightgbm import LGBMClassifier
from django.http import JsonResponse
from .models import Feedback
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import redirect

# Load the dataset
data = pd.read_csv("diabetic/static/diabetic/diabetes (1).csv")
X = data.drop("Outcome", axis=1)
Y = data["Outcome"]

# Train the models
knn_model = KNeighborsClassifier()
knn_model.fit(X, Y)

lgbm_model = LGBMClassifier()
lgbm_model.fit(X, Y)

voting_classifier = VotingClassifier(estimators=[
    ('knn', knn_model),
    ('lgbm', lgbm_model)
], voting='soft')
voting_classifier.fit(X, Y)

# for call home.html
def home(request):
    return render(request, 'home.html')

# for call predict.html
# for display result on the same page
def predict(request):
    if request.method == 'POST':
        float_features = [request.POST[f'n{i}'] for i in range(0, 9)]
        
        # Check the length of float_features
        print("Number of input features:", len(float_features))
        
        # Assuming the first input is the name
        name = float_features[0]

        # Convert all features to float
        final_features = [float(feature) for feature in float_features[1:]]

        # Make sure final_features has 8 elements
        if len(final_features) != 8:
            # Handle the case where there are not enough input features
            return HttpResponse("Please provide all 8 input features.")

        # Make predictions
        prediction_KNN = knn_model.predict([final_features])
        prediction_LGBM = lgbm_model.predict([final_features])
        prediction_FINAL = voting_classifier.predict([final_features])

        pred_KNN = "KNN Model Claims: You have Diabetes, please consult a Doctor." if prediction_KNN == 1 else "KNN Model Claims: You don't have Diabetes."
        pred_LGBM = "LGBM Model Claims: You have Diabetes, please consult a Doctor." if prediction_LGBM == 1 else "LGBM Model Claims: You don't have Diabetes."
        pred_FINAL = "KNN+LGBM Model Claims: You have Diabetes, please consult a Doctor." if prediction_FINAL == 1 else "KNN+LGBM Model Claims: You don't have Diabetes."

        pred_FINAL_1 = "On Considering the above inputs, We are Really Sorry to say that you Have diabetes. Please do Consult a Doctor." if prediction_FINAL == 1 else "You Are Healthy so Stay Home,Stay Safe, Excercise Well and Stay Fit."

        return render(request, 'report.html', {
            'Name': name,
            'KNN': pred_KNN,
            'LGBM': pred_LGBM,
            'FINAL': pred_FINAL,
            'Pregnacies': final_features[0],
            'Glucose': final_features[1],
            'BP': final_features[2],
            'Skin': final_features[3],
            'Insulin': final_features[4],
            'BMI': final_features[5],
            'DPF': final_features[6],
            'Age': final_features[7],
            'res': pred_FINAL_1,
        })
    else:
        return render(request, 'predict.html')

# for display result on the same page
def report(request):
    # Add any necessary logic here to prepare data for the report
    name = request.GET.get('Name')
    pred_KNN = request.GET.get('KNN')
    pred_LGBM = request.GET.get('LGBM')
    pred_FINAL = request.GET.get('FINAL')
    pregnancies = request.GET.get('Pregnacies')
    glucose = request.GET.get('Glucose')
    bp = request.GET.get('BP')
    skin = request.GET.get('Skin')
    insulin = request.GET.get('Insulin')
    bmi = request.GET.get('BMI')
    dpf = request.GET.get('DPF')
    age = request.GET.get('Age')
    pred_FINAL_1 = request.GET.get('res')
    
    # Render the report.html template with the provided parameters
    return render(request, 'report.html', {
        'Name': name,
        'KNN': pred_KNN,
        'LGBM': pred_LGBM,
        'FINAL': pred_FINAL,
        'Pregnacies': pregnancies,
        'Glucose': glucose,
        'BP': bp,
        'Skin': skin,
        'Insulin': insulin,
        'BMI': bmi,
        'DPF': dpf,
        'Age': age,
        'res': pred_FINAL_1,
    })

@csrf_exempt
def feedback_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        feedback = Feedback.objects.create(name=name, email=email, message=message)
       # return JsonResponse({'status': 'success'})
    #else:
        #return JsonResponse({'error': 'GET requests are not supported for this endpoint'}, status=405)
    return render(request, 'feedback.html')