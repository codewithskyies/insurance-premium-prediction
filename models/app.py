
from fastapi import FastAPI
from fastapi.responses import JSONResponse


# from schema.user_input import UserInput

from schema.user_input import UserInput

from predict import predict_output, MODEL_version,model
#ml flow

Model_version='1.0.0'

app = FastAPI()


tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]


# human readable       
@app.get('/')
def home():
    return {'message':'Insurance Premium Prediction API'}

# machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': Model_version,
        'model_loaded': model is not None
    }








@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    prediction = predict_output(user_input)

    return JSONResponse(
        status_code=200,
        content={'predicted_category': str(prediction)}
    )

















# @app.get('/')
# def home():
#     return {"message": "Insurance premium Prediction"}

# @app.get('/health')
# def health_check():
#     return {
#         "status": "ok",
#         "version": Model_version
#     }

# @app.post('/predict')
# def predict_premium(data: UserInput):

#     UserInput = ([{
#         'bmi': data.bmi,
#         'age_group': data.age_group,
#         'lifestyle_risk': data.lifestyle_risk,
#         'city_tier': data.city_tier,
#         'income_lpa': data.income_lpa,
#         'occupation': data.occupation
#     }])

#     prediction = predict_output(UserInput)

#     return JSONResponse(status_code=200, content={'predicted_category': prediction})




