🚀 UDBOSS Food Intelligence System (MVP)
🧠 Overview

A backend system designed to reduce food waste in Nigeria by helping farmers decide when to harvest and sell based on market price trends.

⚙️ System Architecture
Farmer → Crop → Market Prices → Recommendation Engine → Feedback Loop
🧩 Modules Implemented
Farmer Module (data capture)
Crop Module (production tracking)
Market Module (price signals)
Recommendation Engine (decision system)
Feedback Loop (learning system)
🧠 Decision Logic
Detects price trends (increasing, decreasing, stable)
Recommends:
DELAY
HARVEST_NOW
MONITOR
🔁 Feedback System

Stores actual outcomes to:

compare predictions vs reality
improve system intelligence over time
🛠️ Tech Stack
Python
FastAPI
SQLite
📡 API Endpoints
Endpoint	Description
POST /farmers	Create farmer
POST /crops	Register crop
POST /market-prices	Add market data
GET /recommend/{crop_id}	Get recommendation
POST /feedback	Submit real-world result
🎯 MVP Goal

Build a working feedback loop that improves farmer decision-making and reduces food waste.
