"""
Clinical Engineering Dashboard – Streamlit Application
------------------------------------------------------

This application simulates several CE-IT workflows including:
• Connectivity checks
• HL7 message generation and parsing
• Laboratory TAT monitoring
• Device log review
• Preventive maintenance tracking

The goal is to provide a realistic, interactive dashboard that mirrors
common clinical engineering and interoperability tools used in hospitals.

------------------------------------------------------
HOW TO RUN LOCALLY
------------------------------------------------------
1. Install Python 3.10+  
2. Install required packages:
       pip install streamlit pandas numpy

3. Save this file as app.py  
4. Run the application:
       streamlit run app.py

5. The dashboard will open in your browser automatically.

------------------------------------------------------
PAGE DESCRIPTIONS
------------------------------------------------------

Connectivity:
    Simulates device connectivity checks, pings, and status indicators.

HL7 Parser:
    Generates a random ORU^R01 HL7 message and parses it into structured
    patient demographics, vitals, and lab results.

LIS TAT:
    Displays simulated laboratory turnaround times and workflow metrics.

Device Logs:
    Shows mock device logs for troubleshooting and CE-IT review.

PM Tracker:
    Tracks preventive maintenance schedules, due dates, and completion status.

------------------------------------------------------
NOTES
------------------------------------------------------
• This dashboard is for simulation, education, and portfolio use.
• All data is randomly generated and does not represent real patients.
• Modify or expand any section to match real CE workflows.
"""


import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import random



# ---------------------------------------------------------
# COLOR BADGES FOR PM STATUS
# ---------------------------------------------------------
def pm_status_badge(status):
    colors = {"OK": "green", "Due Soon": "orange", "OVERDUE": "red"}
    return f"<span style='color:white; background-color:{colors.get(status,'gray')}; padding:4px 8px; border-radius:4px;'>{status}</span>"

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(page_title="LIS & Medical Equipment Integration Monitor", layout="wide")

# ---------------------------------------------------------
# DEVICE LIST
# ---------------------------------------------------------
devices = [
    {"name": "Philips MX800 Monitor – ICU 1", "ip": "10.10.1.11"},
    {"name": "Philips MX700 Monitor – ICU 2", "ip": "10.10.1.12"},
    {"name": "Hamilton C6 Ventilator – ICU 3", "ip": "10.10.1.13"},
    {"name": "Puritan Bennett 980 Ventilator – ICU 4", "ip": "10.10.1.14"},
    {"name": "Medfusion 4000 Pump – OR 1", "ip": "10.10.2.21"},
    {"name": "Medfusion 3500 Pump – OR 2", "ip": "10.10.2.22"},
    {"name": "Stryker Neptune Waste System – OR 3", "ip": "10.10.2.23"},
    {"name": "Drager Apollo Anesthesia Machine – OR 4", "ip": "10.10.2.24"},
    {"name": "Zoll X Series Defibrillator – ED 1", "ip": "10.10.3.31"},
    {"name": "Zoll R Series Defibrillator – ED 2", "ip": "10.10.3.32"},
    {"name": "Philips Intellivue MX550 – ED 3", "ip": "10.10.3.33"},
    {"name": "Stryker Bed – MedSurg 12", "ip": "10.10.4.41"},
    {"name": "Hillrom Advanta 2 Bed – MedSurg 8", "ip": "10.10.4.42"},
    {"name": "Welch Allyn Spot Monitor – MedSurg 5", "ip": "10.10.4.43"},
    {"name": "Sysmex XN Analyzer – Lab", "ip": "10.10.5.51"},
    {"name": "Roche Cobas 6000 – Lab", "ip": "10.10.5.52"},
    {"name": "Abbott Architect i2000 – Lab", "ip": "10.10.5.53"},
    {"name": "Beckman Coulter AU480 – Lab", "ip": "10.10.5.54"},
    {"name": "GE Corometrics Fetal Monitor – L&D 2", "ip": "10.10.6.61"},
    {"name": "Hillrom Bed – L&D 4", "ip": "10.10.6.62"}
]

# ---------------------------------------------------------
# CONNECTIVITY SIMULATION
# ---------------------------------------------------------
def simulate_connectivity(offline_bias=0.25):
    rows = []
    for d in devices:
        rows.append({
            "Device": d["name"],
            "IP Address": d["ip"],
            "Status": "Offline" if random.random() < offline_bias else "Online",
            "Last Heartbeat": (dt.datetime.now() - dt.timedelta(seconds=random.randint(5,120))).strftime("%H:%M:%S")
        })
    return pd.DataFrame(rows)

# ---------------------------------------------------------
# RANDOM PATIENT
# ---------------------------------------------------------
def random_patient():
    first = random.choice(["JOHN","SARAH","MICHAEL","EMILY","DAVID","LAURA"])
    last = random.choice(["DOE","SMITH","JONES","BROWN","LEE","WILSON"])
    return f"{last}^{first}"

# ---------------------------------------------------------
# RANDOM CMP + VITALS HL7 GENERATOR
# ---------------------------------------------------------
def random_hl7():
    patient = random_patient()

    cmp_values = {
        "GLU^Glucose": (random.randint(70,140),"mg/dL","70-110"),
        "NA^Sodium": (random.randint(130,150),"mmol/L","135-145"),
        "K^Potassium": (round(random.uniform(3.0,5.8),1),"mmol/L","3.5-5.1"),
        "CL^Chloride": (random.randint(95,112),"mmol/L","98-107"),
        "CO2^CO2": (random.randint(18,32),"mmol/L","22-29"),
        "BUN^BUN": (random.randint(5,40),"mg/dL","7-20"),
        "CREAT^Creatinine": (round(random.uniform(0.5,2.5),1),"mg/dL","0.6-1.3"),
        "CA^Calcium": (round(random.uniform(7.5,10.8),1),"mg/dL","8.5-10.5"),
        "TP^Total Protein": (round(random.uniform(5.5,8.5),1),"g/dL","6.0-8.3"),
        "ALB^Albumin": (round(random.uniform(2.5,5.5),1),"g/dL","3.5-5.0"),
        "TBIL^Total Bilirubin": (round(random.uniform(0.1,3.0),1),"mg/dL","0.2-1.2"),
        "ALP^Alkaline Phosphatase": (random.randint(40,180),"U/L","44-147"),
        "AST^AST": (random.randint(10,120),"U/L","10-40"),
        "ALT^ALT": (random.randint(10,120),"U/L","7-56")
    }

    vitals = {
        "HR^Heart Rate": (random.randint(50,140),"bpm","60-100"),
        "BP^Blood Pressure": (f"{random.randint(90,160)}/{random.randint(50,100)}","mmHg","90/60-140/90"),
        "RR^Respiratory Rate": (random.randint(8,30),"breaths/min","12-20"),
        "TEMP^Temperature": (round(random.uniform(35.5,40.5),1),"C","36.0-37.5"),
        "SPO2^Oxygen Saturation": (random.randint(85,100),"%","95-100")
    }

    def flag(val,ref):
        if "/" in ref:
            return ""
        low,high = ref.split("-")
        low=float(low)
        high=float(high)
        val=float(str(val).replace("/",".")) if "/" in str(val) else float(val)
        return "H" if val>high else "L" if val<low else "N"

    cmp_obx=[]
    i=1
    for test,(value,units,ref) in cmp_values.items():
        cmp_obx.append(f"OBX|{i}|NM|{test}||{value}|{units}|{ref}|{flag(value,ref)}")
        i+=1

    vitals_obx=[]
    j=1
    for test,(value,units,ref) in vitals.items():
        vitals_obx.append(f"OBX|{j}|NM|{test}||{value}|{units}|{ref}|{flag(value,ref)}")
        j+=1

    return (
        f"MSH|^~\\&|DEVICE|HOSP|LIS|HOSP|{dt.datetime.now().strftime('%Y%m%d%H%M%S')}||ORU^R01|12345|P|2.3\n"
        f"PID|1||123456||{patient}\n"
        f"OBR|1||CMP|CMP^COMPREHENSIVE METABOLIC PANEL\n"
        + "\n".join(cmp_obx) + "\n"
        f"OBR|2||VITALS|VITALS^VITAL SIGNS\n"
        + "\n".join(vitals_obx)
    )

# ---------------------------------------------------------
# HL7 PARSER
# ---------------------------------------------------------
def parse_hl7(msg):
    lines=msg.strip().split("\n")
    parsed={"Patient":None,"Tests":[]}
    current_obr=None

    for line in lines:
        fields=line.split("|")

        if line.startswith("PID"):
            parsed["Patient"]=fields[5]

        elif line.startswith("OBR"):
            current_obr={"Test Code":fields[4],"Results":[]}
            parsed["Tests"].append(current_obr)

        elif line.startswith("OBX") and current_obr is not None:
            current_obr["Results"].append({
                "Result":fields[5],
                "Units":fields[6],
                "Reference Range":fields[7],
                "Flag":fields[8] if len(fields)>8 else ""
            })

    return parsed

# ---------------------------------------------------------
# LIS TAT SIMULATION
# ---------------------------------------------------------
def simulate_tat(n=10):
    df=pd.DataFrame({
        "Specimen":[f"S{i}" for i in range(1,n+1)],
        "Received":[dt.datetime.now()-dt.timedelta(minutes=random.randint(20,120)) for _ in range(n)],
        "Completed":[dt.datetime.now()-dt.timedelta(minutes=random.randint(1,20)) for _ in range(n)]
    })
    df["TAT (min)"]=(df["Completed"]-df["Received"]).dt.total_seconds()/60
    return df

# ---------------------------------------------------------
# DEVICE LOGS
# ---------------------------------------------------------
def generate_device_logs(n=20):
    events=["Power cycle detected","Network disconnect","Network restored","Alarm triggered","Self-test passed","Self-test failed","Configuration updated","Firmware check","Battery low","Battery restored"]
    severity=["INFO","WARNING","ERROR"]
    logs=[]
    for _ in range(n):
        d=random.choice(devices)
        logs.append({
            "Timestamp":(dt.datetime.now()-dt.timedelta(minutes=random.randint(1,500))).strftime("%Y-%m-%d %H:%M:%S"),
            "Device":d["name"],
            "IP Address":d["ip"],
            "Event":random.choice(events),
            "Severity":random.choice(severity)
        })
    return pd.DataFrame(logs).sort_values("Timestamp",ascending=False)

# ---------------------------------------------------------
# PM TRACKER
# ---------------------------------------------------------
def generate_pm_tracker():
    n=len(devices)
    risk=np.random.choice(["Low","Medium","High"],size=n,p=[0.3,0.4,0.3])
    intervals=[12 if r=="Low" else 6 if r=="Medium" else 3 for r in risk]

    pm=pd.DataFrame({
        "Asset":[d["name"] for d in devices],
        "IP Address":[d["ip"] for d in devices],
        "Risk Level":risk,
        "PM Interval (Months)":intervals,
        "Work Order #":[f"WO-{random.randint(10000,99999)}" for _ in range(n)],
        "Last PM":[dt.date.today()-dt.timedelta(days=random.randint(30,365)) for _ in range(n)]
    })

    pm["Last PM"]=pd.to_datetime(pm["Last PM"])
    pm["Next PM Due"]=pm["Last PM"]+pm["PM Interval (Months)"].apply(lambda m:pd.Timedelta(days=m*30))
    today=pd.to_datetime(dt.date.today())
    pm["Days Until Due"]=(pm["Next PM Due"]-today).dt.days
    pm["Status"]=pm["Days Until Due"].apply(lambda d:"OVERDUE" if d<0 else "Due Soon" if d<30 else "OK")
    return pm



# ---------------------------------------------------------
# SIDEBAR CONTROLS
# ---------------------------------------------------------
st.sidebar.title("Integration Controls")

offline_bias=st.sidebar.slider("Offline probability",0.0,0.6,0.25,0.05)
tat_samples=st.sidebar.slider("Number of LIS samples",5,30,10,1)
log_count=st.sidebar.slider("Number of log entries",10,100,20)

# ---------------------------------------------------------
# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

# ---------------------------------------------------------
# MAIN PAGE AREA
# ---------------------------------------------------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, on_bad_lines='skip')
    st.write("### Uploaded CSV Data")
    st.dataframe(df)


    

page=st.sidebar.radio("Navigation",["Connectivity","HL7 Parser","LIS TAT","Device Logs","PM Tracker"])

# ---------------------------------------------------------
# EXPORTS
# ---------------------------------------------------------
if page=="PM Tracker":
    st.sidebar.subheader("Export Options")
    pm_export=generate_pm_tracker()
    st.sidebar.download_button("Download PM CSV",pm_export.to_csv(index=False).encode("utf-8"),"pm_tracker_export.csv","text/csv")

st.sidebar.subheader("Export All Data")
export_all="\n".join([
    "=== DEVICE CONNECTIVITY ===",
    simulate_connectivity(offline_bias).to_csv(index=False),
    "\n=== LIS TURNAROUND TIME ===",
    simulate_tat(tat_samples).to_csv(index=False),
    "\n=== DEVICE LOGS ===",
    generate_device_logs(log_count).to_csv(index=False),
    "\n=== PM TRACKER ===",
    generate_pm_tracker().to_csv(index=False)
]).encode("utf-8")

st.sidebar.download_button("Download ALL Data (CSV)",export_all,"integration_dashboard_export.csv","text/csv")

# ---------------------------------------------------------
# PAGE ROUTER
# ---------------------------------------------------------
if page=="Connectivity":
    st.title("Device Connectivity Status")
    conn_df=simulate_connectivity(offline_bias)
    st.dataframe(conn_df,use_container_width=True)
    pct=(conn_df["Status"]=="Online").mean()*100
    st.metric("Devices Online",f"{pct:.0f}%")

elif page=="HL7 Parser":
    st.title("HL7 ORU^R01 Message Parser")

    # Generate a fresh random HL7 every time page loads
    current_hl7=random_hl7()

    # READ-ONLY HL7 display
    st.text_area("HL7 Message (Read-Only)", current_hl7, height=300, key=f"hl7_{random.randint(1,999999)}", disabled=True)

    if st.button("Parse HL7"):
        parsed=parse_hl7(current_hl7)
        parsed["parsed_at"]=dt.datetime.now().strftime("%H:%M:%S.%f")
        st.json(parsed)

elif page=="LIS TAT":
    st.title("LIS Turnaround Time Analytics")
    tat=simulate_tat(tat_samples)
    st.dataframe(tat,use_container_width=True)
    st.metric("Average TAT (min)",f"{tat['TAT (min)'].mean():.1f}")
    st.bar_chart(tat.set_index("Specimen")["TAT (min)"])

elif page=="Device Logs":
    st.title("Device Log Viewer")
    logs=generate_device_logs(log_count)
    st.dataframe(logs,use_container_width=True)

elif page=="PM Tracker":
    st.title("LIS Device PM Tracker")
    pm=generate_pm_tracker()

    risk_filter=st.selectbox("Filter by Risk Level",["All","Low","Medium","High"])
    status_filter=st.selectbox("Filter by PM Status",["All","OK","Due Soon","OVERDUE"])

    filtered=pm.copy()
    if risk_filter!="All":
        filtered=filtered[filtered["Risk Level"]==risk_filter]
    if status_filter!="All":
        filtered=filtered[filtered["Status"]==status_filter]

    display=filtered.copy()
    display["Status"]=display["Status"].apply(pm_status_badge)

    st.write(display.to_html(escape=False),unsafe_allow_html=True)

    csv=filtered.to_csv(index=False).encode("utf-8")
    st.download_button("Download PM Report as CSV",csv,"pm_tracker_export.csv","text/csv")
