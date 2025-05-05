import streamlit as st
import pandas as pd
import os
os.system('pip install joblib')
import joblib

# Configure Streamlit app
st.set_page_config(page_title="Student Dropout Predictor", layout="centered")

# Load model artifact
@st.cache_resource
def load_model():
    best_model = joblib.load("gb_dropout_model.pkl")
    return best_model

# Load the model
best_model = load_model()

# Selected features (updated as requested)
selected_features = [
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Tuition_fees_up_to_date',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_1st_sem_evaluations',
    'Scholarship_holder',
    'Application_mode',
    'Gender',
    'Debtor',
    'Age_at_enrollment',
    'course_category',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_2nd_sem_enrolled'
]

# Custom CSS for styling
st.markdown("""
<style>
    .header-style {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .section-header {
        font-size: 20px;
        font-weight: bold;
        margin: 15px 0px 10px 0px;
        padding-bottom: 5px;
        border-bottom: 2px solid #2E86AB;
    }
    .risk-high {
        color: #E63946;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .risk-medium {
        color: #F4A261;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .risk-low {
        color: #2A9D8F;
        font-weight: bold;
        font-size: 1.2rem;
    }
    .metric-card {
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .recommendation-box {
        background-color: #2A9D8F;
        border-left: 5px solid #2A9D8F;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0px;
    }
    .stProgress > div > div > div > div {
        background-color: #2E86AB;
    }
</style>
""", unsafe_allow_html=True)

# Streamlit app logic
def main():
    st.title("🧑‍🎓 Student Details")
    st.markdown("Analyze the risk of a student dropping out based on their academic and personal details.")
    
    # Add some visual separation
    st.markdown("---")

    # Form for user input
    with st.form("dropout_form"):
        # Student Basic Information Section
        st.markdown('<p class="header-style">👤 Student Basic Information</p>', unsafe_allow_html=True)
        
        student_name = st.text_input("Full Name", placeholder="Enter student's full name")
        col1, col2 = st.columns(2)
        
        with col1:
            gender = st.selectbox("Gender", [("Male", 1), ("Female", 0)], format_func=lambda x: x[0])[1]
        with col2:
            age = st.number_input("Age at Enrollment ?", min_value=17, max_value=60, value=20)
        
        # Additional Information Section
        st.markdown('<p class="section-header">📝 Additional Information</p>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            tuition = st.selectbox("Tuition Fees Status ?", [("Paid on time", 1), ("Delayed payment", 0)], 
                                 format_func=lambda x: x[0])[1]
            scholarship = st.selectbox("Scholarship Holder ?", [("Yes", 1), ("No", 0)], 
                                     format_func=lambda x: x[0])[1]
        with col2:
            debtor = st.selectbox("Has Tuition Debt ?", [("Yes", 1), ("No", 0)], 
                                format_func=lambda x: x[0])[1]
            app_mode = st.selectbox("Application Mode", [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57],
                                  help="Method used to apply to the program (Categorical) " \
                                  "1 - 1st phase - general contingent 2 - Ordinance No. 612/93 5 - 1st phase - special contingent (Azores Island) " \
                                  "7 - Holders of other higher courses 10 - Ordinance No. 854-B/99 15 - International student (bachelor) " \
                                  "16 - 1st phase - special contingent (Madeira Island) 17 - 2nd phase - general contingent " \
                                  "18 - 3rd phase - general contingent 26 - Ordinance No. 533-A/99, item b2) (Different Plan) " \
                                  "27 - Ordinance No. 533-A/99, item b3 (Other Institution) 39 - Over 23 years old 42 - Transfer 43 - Change of course " \
                                  "44 - Technological specialization diploma holders 51 - Change of institution/course 53 - Short cycle diploma holders " \
                                  "57 - Change of institution/course (International)")

        with col3:
            course = st.selectbox("Program Category ", 
                                ['Science & Technology', 'Business & Management', 'Health Science', 'Social Science'])

        # Semester 1 Academic Information
        st.markdown('<p class="section-header">📘 Semester 1 Academic Performance</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            grade_1st = st.slider("Average Grade (0-20 scale)", 0.0, 20.0, 12.0, step=0.5, 
                                help="Average grade across all courses in 1st semester")
            approved_1st = st.number_input("Units Approved", 0, 20, 8, 
                                         help="Number of curricular units approved in 1st semester")
        with col2:
            enrolled_1st = st.number_input("Units Enrolled", 0, 20, 10, 
                                         help="Number of curricular units enrolled in 1st semester")
            eval_1st = st.number_input("Units Evaluated", 0, 20, 10, 
                                      help="Number of curricular units evaluated in 1st semester")
        
        # Semester 2 Academic Information
        st.markdown('<p class="section-header">📘 Semester 2 Academic Performance</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            grade_2nd = st.slider("Average Grade (0-20 scale)", 0.0, 20.0, 12.0, step=0.5, 
                                help="Average grade across all courses in 2nd semester")
            approved_2nd = st.number_input("Units Approved", 0, 20, 8, 
                                         help="Number of curricular units approved in 2nd semester")
        with col2:
            enrolled_2nd = st.number_input("Units Enrolled", 0, 20, 10, 
                                         help="Number of curricular units enrolled in 2nd semester")
            eval_2nd = st.number_input("Units Evaluated", 0, 20, 10, 
                                      help="Number of curricular units evaluated in 2nd semester")

        # Submit button with better styling
        submitted = st.form_submit_button("🔍 Predict Dropout Risk", 
                                        help="Click to analyze dropout risk", 
                                        type="primary",
                                        use_container_width=True)

        if submitted:
            # Prepare input data for prediction
            input_data = {
                'Curricular_units_2nd_sem_grade': grade_2nd,
                'Curricular_units_2nd_sem_approved': approved_2nd,
                'Curricular_units_1st_sem_grade': grade_1st,
                'Tuition_fees_up_to_date': tuition,
                'Curricular_units_1st_sem_approved': approved_1st,
                'Curricular_units_2nd_sem_evaluations': eval_2nd,
                'Curricular_units_1st_sem_evaluations': eval_1st,
                'Scholarship_holder': scholarship,
                'Application_mode': app_mode,
                'Gender': gender,
                'Debtor': debtor,
                'Age_at_enrollment': age,
                'course_category': course,
                'Curricular_units_1st_sem_enrolled': enrolled_1st,
                'Curricular_units_2nd_sem_enrolled': enrolled_2nd
            }

            # Convert input to a DataFrame and align with selected features
            input_df = pd.DataFrame([input_data])[selected_features]

            try:
                # Predict dropout risk using the model directly
                prediction_proba = best_model.predict_proba(input_df)[:, 1]
                dropout_risk = prediction_proba[0] * 100
                prediction = best_model.predict(input_df)

                # Risk level logic
                if dropout_risk > 60:
                    risk_level = 'High Risk 🔴'
                    risk_class = 'risk-high'
                elif dropout_risk > 30:
                    risk_level = 'Medium Risk 🟡'
                    risk_class = 'risk-medium'
                else:
                    risk_level = 'Low Risk 🟢'
                    risk_class = 'risk-low'

                # Display the results
                st.markdown(f"### Dropout Risk: **{risk_level}**")
                st.markdown(f"Risk Score: **{dropout_risk:.2f}%**")
                st.markdown(f"<div class='{risk_class}'>{risk_level}</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error in prediction: {e}")

if __name__ == "__main__":
    main()