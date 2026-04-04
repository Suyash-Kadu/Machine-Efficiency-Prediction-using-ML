import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title = "Machine Efficiency", layout="wide")

cola, colb, colc = st.columns([3,1.5,2])

with colb:
        st.write("A Project on")

cold, cole, colf = st.columns([1,4.7,0.5])

with cole:
        st.title("Production Machine Efficiency Prediction using ML")

tab1, tab2 = st.tabs(["Home", "Form"])

with tab1:      

        col1, col2, col3 = st.columns([3,2.4,2])

        with col2:
                st.header("INTRODUCTION")

        col4, col5 = st.columns([1.2,0.8])

        with col4:
                st.write("In the modern manufacturing landscape, often referred to as Industry 4.0, the continuous and efficient operation" \
                " of production machinery is critical to maintaining profitability and competitiveness. Industrial machines operate under" \
                " immense physical stress, constantly fluctuating in temperature, pressure, and vibration. Traditionally, machine maintenance"
                " and efficiency tracking have been reactive addressed only after a failure occurs or a significant drop in production" \
                " quality is noticed. This reactive approach leads to costly unplanned downtimes, higher error rates, and increased operational" \
                " expenses.")
                st.write("With the advent of the Industrial Internet of Things (IIoT), modern shop floors are equipped with sensors that" \
                " continuously capture minute-level telemetry data. However, this raw data is typically massive, noisy, and characterized" \
                " by inconsistent scales and non-linear distributions, making it nearly impossible for human operators to manually extract" \
                " actionable insights in real time.")
        with col5:
               st.image("Gemini_Generated_Image_7ps1ad7ps1ad7ps1.png")

        st.divider()

        col9, col10, col11 = st.columns([2,2,1.5])

        with col10:
                st.header("PROBLEM STATEMENT")
        
        st.write("##### 1. Inconsistent Sensor Data")
        st.write("Industrial environments generate massive volumes of raw telemetry—such as vibration, temperature, and pressure" \
        " that often contain missing values and non-linear distributions, making it difficult to extract clear performance insights.")

        st.write("##### 2. Reactive Maintenance Gaps")
        st.write("Traditional production monitoring is frequently reactive, where issues are only addressed after a machine fails or a "
        "'maintenance flag' is triggered, leading to costly unplanned downtime.")

        st.write("##### 3. Operational Inefficiency Identification")
        st.write("There is a lack of automated systems that can quantify exactly how physical stressors (like power spikes or material" \
        " flow irregularities) correlate to a decrease in efficiency scores and an increase in production error rates.")

        st.divider()

        col6, col7, col8 = st.columns([3,1.5,2])

        with col7:
               st.header("OBJECTIVE")

        st.write("##### 1. Data Processing and Standardization")
        st.write("To clean and preprocess raw manufacturing dataset streams by handling missing values and anomalies inherent in" \
        " industrial sensor telemetry.")
        st.write("To normalize and scale mechanical variables with inconsistent units (e.g., Temperature in °C, Pressure in Pa, Power" \
        " Consumption in kW) to ensure feature parity for machine learning algorithms.")

        st.write("##### 2. Exploratory Data Analysis (EDA) & Pattern Recognition")
        st.write("To conduct cross-sectional analysis of machine states, removing temporal dependencies to evaluate the immediate" \
        " impact of physical stressors.")
        st.write("To quantify the relationships and correlations between mechanical variables"
        " (vibration, temperature, material flow rate) and target production metrics (error rates, cycle times, downtime).")

        st.write("##### 3. Predictive Modeling and Algorithm Evaluation")
        st.write("To train and evaluate a diverse suite of machine learning algorithms (including Linear Regression, Random Forest," \
        " Gradient Boosting, XGBoost, and SVR) to capture non-linear distributions in the data.")
        st.write("To predict a continuous Efficiency Score (0–100) indicating real-time machine health.")
        st.write("To build a classification system that accurately categorizes the Production Status as either"
        " 'Efficient' or 'Inefficient'")

        st.write("##### 4. Proactive Maintenance & Operational Optimization")
        st.write("To identify the specific thresholds of mechanical stress that trigger a transition from an efficient to an" \
        " inefficient production state.")
        st.write("To provide actionable, data-driven insights that allow facility managers to intervene proactively, rather than" \
        " reacting to machine failures or maintenance flags after they occur.")

with tab2:
       

        col1, col2 = st.columns(2)

        with col1:
                machine_type = st.selectbox("Machine Type", ["Welder", "Conveyor", "Drill", "CNC"])
                temp = st.number_input("Temperature", value = 50.00, step=2.00)
                vibration = st.number_input("Vibration Level", value = 2.00, step=0.10)
                power_con = st.number_input("Power Consumption", value = 15.00, step=2.00)
                pressure = st.number_input("Pressure", value = 5.00, step=0.50)

        with col2:
                material_flow_rate = st.number_input("Material Flow Rate", value = 20.00, step=1.00)
                cycle_time = st.number_input("Cycle Time", value = 100.00, step=5.00)
                error_rate = st.number_input("Error Rate", value = 0.50, step=0.01)
                downtime = st.number_input("Downtime", value = 0.00, step=5.00)
                main_flag = st.radio("Maintenance Flag", ["Yes", "No"], horizontal=True)

        mf = 0
        if main_flag == "Yes":
                mf = 1
        elif main_flag == "No":
                mf = 0

        mapping = {"Welder": 3, "Conveyor": 1, "Drill": 2, "CNC": 0}
        mt_val = mapping.get(machine_type, 0)


        if st.button("submit"):
                input_data = pd.DataFrame({
                        "temperature": [temp],
                        "vibration_level": [vibration],
                        "power_consumption": [power_con],
                        "pressure": [pressure],
                        "material_flow_rate": [material_flow_rate],
                        "cycle_time": [cycle_time],
                        "error_rate": [error_rate],
                        "downtime": [downtime],
                        "maintenance_flag": [mf]
                })

                with open("Production_System_ML_Model(R).pkl", "rb") as f:
                        FinalModel = pickle.load(f)

                efficiency = FinalModel.predict(input_data)
                efficiency_str = f"{efficiency[0]: .2f}"

        st.divider()

        try:
         st.metric("Machine Efficiency", value=efficiency_str)
        except:
         pass
