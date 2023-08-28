# Purpose
Predict if a person will have Diabetes or not and make an interactive interface for user inputs
## Web Application
The application was done with a minimalist design to provide an eazy and efficient experience. <br> **You can access the app clicking** [here](https://diabetesapp.streamlit.app/)
## Creator
[@jpedrou](https://github.com/jpedrou)
## Tools Used
<img width="48" height="48" src="https://img.icons8.com/color/48/python--v1.png" alt="python--v1"/> <img width=65 src='https://github.com/jpedrou/DiabetesPrediction/assets/127536464/e159c810-b104-44c7-bba1-86ec218f139e'> <img width="48" height="48" src="https://img.icons8.com/fluency/48/jupyter.png" alt="jupyter"/> <img width="48" height="48" src="https://img.icons8.com/color/48/visual-studio-code-2019.png" alt="visual-studio-code-2019"/>

# About Dataset
The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level. This dataset can be used to build machine learning models to predict diabetes in patients based on their medical history and demographic information. This can be useful for healthcare professionals in identifying patients who may be at risk of developing diabetes and in developing personalized treatment plans. Additionally, the dataset can be used by researchers to explore the relationships between various medical and demographic factors and the likelihood of developing diabetes.

Columns:
- `gender`: Gender refers to the biological sex of the individual, which can have an impact on their susceptibility to diabetes. There are three categories in it male ,female and other.

- `age`: Age is an important factor as diabetes is more commonly diagnosed in older adults.Age ranges from 0-80 in our dataset.

- `hypertension`: Hypertension is a medical condition in which the blood pressure in the arteries is persistently elevated. It has values a 0 or 1 where 0 indicates they don’t have hypertension and for 1 it means they have hypertension.

- `heart_disease`: Heart disease is another medical condition that is associated with an increased risk of developing diabetes. It has values a 0 or 1 where 0 indicates they don’t have heart disease and for 1 it means they have heart disease.

- `smoking_history`: Smoking history is also considered a risk factor for diabetes and can exacerbate the complications associated with diabetes.In our dataset we have 5 categories i.e not current,former,No Info,current,never and ever.

- `bmi`: BMI (Body Mass Index) is a measure of body fat based on weight and height. Higher BMI values are linked to a higher risk of diabetes. The range of BMI in the dataset is from 10.16 to 71.55. BMI less than 18.5 is underweight, 18.5-24.9 is normal, 25-29.9 is overweight, and 30 or more is obese.

- `HbA1c_level`: HbA1c (Hemoglobin A1c) level is a measure of a person's average blood sugar level over the past 2-3 months. Higher levels indicate a greater risk of developing diabetes. Mostly more than 6.5% of HbA1c Level indicates diabetes.

- `blood_glucose_level`: Blood glucose level refers to the amount of glucose in the bloodstream at a given time. High blood glucose levels are a key indicator of diabetes.

- **`diabetes`**: diabetes is the target variable being predicted, with values of 1 indicating the presence of diabetes and 0 indicating the absence of diabetes.
### Note
This database is very unbalanced, which means that it has more samples of people without diabetes than with. It can be a problem for the machine learning Models.

**Unbalanced data**

![g](https://github.com/jpedrou/DiabetesPrediction/assets/127536464/7a5967b5-5ed4-4995-9903-a7d6c9d5955f)
# Model Selection
As this dataset is big and it is a situation that we need a Precision high level, I chose the 4 models that often get a greate result in this type of case:
- SVM (Support Vectors Machine)
- Random Forest
- Gradient Boosting
- Neural Networks
### Note
All the models got a great result looking only at Accuracy, but they are getting difficult to identify which person has Diabetes and it is a big problem for us. This occurs, because the data is very desbalanced (you can see in the image above), that's why the models couldn't perform better. To solve it, We could try to balance this data by two options: subsampling or oversampling it. As this base has little information about people who have diabetes, oversampling it using a specific library is the best choice, in my opinion.
# Oversampling
It is a technique that consists of increasing the number of registers of the class with less frequency until the database has a balanced number between the classes of the target variable. In brief, this method will do some distance calculations to generate new synthetic data.

![sla](https://github.com/jpedrou/DiabetesPrediction/assets/127536464/64aeff65-0a3c-4f64-b685-452b4493ac7c)

