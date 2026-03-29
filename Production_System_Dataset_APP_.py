import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title = "Machine Efficiency", layout="wide")

st.header("Project - Find Machine Efficiency")

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
                "machine_type": [mt_val],
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
    st.text_input("Machine Efficiency", value=efficiency_str)
except:
    st.text_input("Machine Efficiency")