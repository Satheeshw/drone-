import streamlit as st
import random
import time
import plotly.graph_objects as go

def simulate_drone_data():
    battery_voltage = round(random.uniform(10.5, 12.5), 2)
    roll = round(random.uniform(-180, 180), 2)
    pitch = round(random.uniform(-90, 90), 2)
    yaw = round(random.uniform(0, 360), 2)
    temperature = round(random.uniform(20, 40), 2)
    altitude = round(random.uniform(0, 1000), 2)
    latitude = round(random.uniform(-90, 90), 6)
    longitude = round(random.uniform(-180, 180), 6)
    connection_health = random.choice(["Excellent", "Poor", "No Signal"])
    return {
        "Battery Voltage": battery_voltage,
        "Roll": roll,
        "Pitch": pitch,
        "Yaw": yaw,
        "Temperature": temperature,
        "Altitude": altitude,
        "Latitude": latitude,
        "Longitude": longitude,
        "Connection Health": connection_health,
    }

st.sidebar.title("Drone Telemetry Dashboard")
page = st.sidebar.selectbox("Choose a page", ["Home", "Dashboard"])

if page == "Home":
    st.title("Welcome to the Drone Telemetry Dashboard")
    st.write("This dashboard provides real-time metrics and graphs for the drone's performance.")
    st.image("drone.jpeg",width=700)
elif page == "Dashboard":
    st.title("Drone Telemetry Dashboard")
    container = st.empty()

    while True:
        drone_data = simulate_drone_data()
        with container.container():
            col1, col2, col3 = st.columns(3)
            col1.metric("Battery Voltage", f"{drone_data['Battery Voltage']} V")
            col2.metric("Temperature", f"{drone_data['Temperature']}°C")
            col3.metric("Altitude", f"{drone_data['Altitude']} m")

            gauge = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = drone_data['Battery Voltage'],
                title = {'text': "Battery Voltage"},
                delta = {'reference': 12, 'increasing': {'color': "RebeccaPurple"}},
                gauge = {
                    'axis': {'range': [0, 12], 'visible': True},
                    'bar': {'color': "black"},
                    'bgcolor': "lightgray",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0,4], 'color': "red"},
                        {'range': [4,8], 'color': "yellow"},
                        {'range': [8,12], 'color': "green"},
                        ],
                    }
                ))
            st.plotly_chart(gauge, use_container_width=True, key=str(time.time()))

            col4, col5, col6 = st.columns(3)
            col4.metric("Roll", f"{drone_data['Roll']}°")
            col5.metric("Pitch", f"{drone_data['Pitch']}°")
            col6.metric("Yaw", f"{drone_data['Yaw']}°")

            col7, col8 = st.columns(2)
            col7.metric("Latitude", f"{drone_data['Latitude']}°")
            col8.metric("Longitude", f"{drone_data['Longitude']}°")

            st.write(f"Connection Health: {drone_data['Connection Health']}")
        time.sleep(1)
