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

### 5. Nuvolo-Style PM Tracker
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

## 📸 Screenshots (Suggested Layout)

### Dashboard Overview  
*(Insert screenshot here)*

### HL7 Parser  
*(Insert screenshot here)*

### Device Connectivity Monitor  
*(Insert screenshot here)*

### PM Tracker with Status Badges  
*(Insert screenshot here)*

---

## 🧑‍🔧 Author
Chase — Clinical Engineering & CE‑IT Integration

