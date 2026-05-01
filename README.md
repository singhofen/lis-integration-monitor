https://lis-integration-monitor-h4jt9uq5v6cxzdtzglnmkh.streamlit.app/

# LIS & Medical Equipment Integration Monitor
A Streamlit-based CE‑IT operational dashboard that simulates real-world
Clinical Engineering and LIS integration workflows. This project demonstrates
device connectivity monitoring, HL7 message parsing, LIS turnaround-time
analytics, device event logging, and Nuvolo-style PM tracking.

---

## 🔧 Features

### 1. Device Connectivity Monitoring
Simulates online/offline status for networked medical devices and displays
heartbeat timestamps. Demonstrates how CE‑IT teams monitor device uptime,
network stability, and integration readiness.

### 2. HL7 ORU^R01 Message Parser
Parses a sample HL7 v2.x lab result message and extracts:
- Patient name  
- Test code  
- Result value  
- Units  
- Reference range  
- Result flag  

This models LIS → EMR result transmission workflows.

### 3. LIS Turnaround Time (TAT) Analytics
Generates mock specimen timestamps and calculates:
- TAT in minutes  
- Average TAT  
- Bar chart visualization  

Useful for demonstrating LIS performance monitoring.

### 4. Device Log Viewer
Simulates CE‑IT style device event logs including:
- Power cycles  
- Network disconnects  
- Self-test failures  
- Firmware checks  
- Alarm events  

Includes severity levels (INFO, WARNING, ERROR).

### 5. LIS Device-Style PM Tracker
Simulates PM schedules with:
- Risk levels  
- PM intervals  
- Last PM date  
- Next PM due date  
- Days until due  
- Color-coded status badges (OK, Due Soon, OVERDUE)  
- Filters (risk level, PM status)  
- CSV export  
- Mock CMMS work order numbers  
- Device detail pop-up panels  

---

## 🧰 Technologies Used
- Python 3.x  
- Streamlit  
- Pandas  
- Numpy  
- HL7-style string parsing  
- Randomized simulation for demo purposes  

---

## ▶️ How to Run Locally

### 1. Clone the repository

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>


### 2. Install dependencies

pip install -r requirements.txt


### 3. Run the dashboard

streamlit run app.py


### 4. Access it in your browser
Streamlit will open automatically, or you can visit:

http://localhost:8501


---

## 🚀 Deploying to Streamlit Cloud

You can deploy this dashboard publicly with no server setup.

### 1. Push this project to a public GitHub repository  
Ensure your repo includes:
- `app.py`  
- `requirements.txt`  
- Any additional modules  

### 2. Go to Streamlit Cloud  
https://streamlit.io/cloud

### 3. Click **“New app”**  
Select:
- Your GitHub repo  
- The branch to deploy  
- `app.py` as the entry point  

### 4. Click **Deploy**  
Streamlit Cloud will automatically:
- Create the environment  
- Install dependencies  
- Launch the dashboard  

You’ll receive a public URL you can share on your resume or portfolio.

---

## 📌 Purpose of This Project
This dashboard is designed to demonstrate:
- CE‑IT integration concepts  
- HL7 message structure and parsing  
- Medical device connectivity monitoring  
- PM scheduling logic similar to Nuvolo/AIMS  
- Operational analytics for Clinical Engineering  
- Ability to build internal tools for CE‑IT workflows  

No real patient data or proprietary systems are used.

---

## 📸 Screenshots

### Dashboard Overview  
<img width="1912" height="840" alt="DEVICE LOG" src="https://github.com/user-attachments/assets/ab7d78aa-cf59-4817-80d2-3846e0c4bddd" />
### HL7 Parser  
<img width="1903" height="855" alt="parser-1" src="https://github.com/user-attachments/assets/d9223c4b-e38d-4233-80c0-b3f5ffd08b72" />

<img width="1918" height="858" alt="parser-2" src="https://github.com/user-attachments/assets/f1912e0e-cb2c-49a1-87e5-44a79f0acee3" />

<img width="1908" height="858" alt="LIS TAT" src="https://github.com/user-attachments/assets/76cb258b-aa5c-4a31-b509-4f0143c4489d" />

### Device Connectivity Monitor  
<img width="1905" height="832" alt="device tracker pm tracker" src="https://github.com/user-attachments/assets/79610b5d-89e4-410b-9947-9be5fe1c7506" />

### PM Tracker with CSV FILE UPLOAD DATA View  
<img width="1918" height="625" alt="uploaded csv file option" src="https://github.com/user-attachments/assets/ab48456c-72d9-4344-80e1-e88cbe6e4421" />

---

## 🧑‍🔧 Author
Chase — Clinical Engineering & CE‑IT Integration

