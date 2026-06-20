# 🚌 Dahod Mini Bus - Smart City Transit Hub

A real-time transit telemetry infrastructure built to track public mini-buses across Dahod city. This prototype enables automated smartphone tracking for bus operators and live dynamic map visualization for commuters without relying on external GPS hardware trackers.

---

## 🗺️ Portal Navigation & System URLs

When running the application locally, use the following network endpoints to access the respective system frontends:

* **🌐 Passenger Tracking Portal:** [http://127.0.0.1:5002](http://127.0.0.1:5002)  
    *The public dashboard displaying live bus positions, color-coded transit routes, and fixed bus shelter locations.*
* **📱 Driver Telemetry Console:** [http://127.0.0.1:5002/driver](http://127.0.0.1:5002/driver)  
    *The secure authentication gateway and operational control panel used by operators to stream real-time GPS locations.*

---

## 🔑 Driver Authentication Matrix

To safeguard the transit stream from rogue telemetry, the Driver Portal is protected by a global validation guard. **Any number plate can be typed freely (it is not fixed in a database)**, allowing you to quickly spin up multiple drivers on the fly!

| Parameter | Required Input Protocol / Credentials |
| :--- | :--- |
| **Bus ID / Plate Number** | Enter **ANY** custom identifier (e.g., `GJ-20-B-1001`, `GJ-20-B-2002`, `BUS-A`) |
| **Route Assignment** | Select the corresponding route from the dropdown menu |
| **Secure Shift Password** | **`dahod2026`** |

> ⚠️ **Important Security Note:** Access to the tracking engine will be rejected instantly unless the exact security key (`dahod2026`) is provided.

---

## ⚙️ Operational Workflow

To properly simulate and present the project ecosystem during your evaluation, execute the steps in this specific chronological order:

1. **Initialize the Server:** Launch `app.py` in your terminal to boot up the central routing mesh.
2. **Open the Passenger Portal:** Open [http://127.0.0.1:5002](http://127.0.0.1:5002) in a browser tab. The map will load over Dahod showing 3 static, color-coded route lines. The "Live Fleet" counter will read `0`.
3. **Login as a Driver:** Open [http://127.0.0.1:5002/driver](http://127.0.0.1:5002/driver) (ideally on a mobile device or a split-screen browser window). Enter a unique Bus ID, a route name, and the password `dahod2026`. Click **"Start Route Shift"**.
4. **Grant Device Permissions:** Allow the browser to access your device location when prompted. 
5. **Observe Real-Time Stream:** The moment the driver console locks onto a GPS coordinate, a dynamic blue **"B"** marker will appear on the Passenger Map. The live fleet counter will scale automatically. To add more buses, simply open another driver window and log in with a **different number plate**.

---

## 📁 System Blueprint & Directory Layout

```text
dahod_bus_tracker/
│
├── app.py                 # Core Python Flask backend server
├── requirements.txt       # Environment dependency lockfile
├── README.md              # Project documentation guide
└── templates/             # Frontend Layout Assets
    ├── index.html         # Leaflet Map Passenger Dashboard
    └── driver.html        # Secure Driver Console & GPS Engine