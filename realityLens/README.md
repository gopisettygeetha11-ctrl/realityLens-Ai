# RealityLens AI - Fact Check & Verification Suite

A dual-application intelligence suite designed for review verification, heuristic friction detection, and actionable insight extraction.

---

## 📁 Repository Structure

```
RealityLens_AI/
│
├── ai_places_app/                 # Project 1: Places & Hotels Fact Checker
│   ├── .streamlit/config.toml     # Streamlit theme & server configuration
│   ├── app.py                     # Main Streamlit application
│   ├── requirements.txt           # App dependencies
│   └── README.md                  # Detailed app documentation
│
├── delivery_apps/                 # Project 2: Delivery & E-Commerce Fact Checker
│   ├── .streamlit/config.toml     # Streamlit theme & server configuration
│   ├── app.py                     # Main Streamlit application
│   ├── requirements.txt           # App dependencies
│   └── README.md                  # Detailed app documentation
│
├── archive/                       # Archived prototypes and historical backups
├── index.html                     # Web portal & landing page
├── vercel.json                    # Vercel deployment configuration
├── .gitignore                     # Git ignore rules for venv, caches, and secrets
└── README.md                      # Repository overview and deployment guide
```

---

## 🚀 Running the Apps Locally

Make sure you have Python 3.10+ installed and install dependencies:

### 1. AI Places & Hotels App
```bash
cd ai_places_app
pip install -r requirements.txt
streamlit run app.py
```
> Access at: `http://localhost:8501`

### 2. Delivery & E-Commerce Apps
```bash
cd delivery_apps
pip install -r requirements.txt
streamlit run app.py
```
> Access at: `http://localhost:8501` (or next available port, e.g. 8502)

---

## 🌐 Deployment Instructions

### Option A: Streamlit Community Cloud (Recommended & Free)
Streamlit apps require persistent WebSocket connections which are natively supported for free on Streamlit Community Cloud:

1. Push your repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/) with your GitHub account.
3. Click **New app** and select your repository.
4. **Deploy AI Places**:
   - Set **Main file path**: `ai_places_app/app.py`
   - Click **Deploy**
5. **Deploy Delivery Apps**:
   - Create another app in Streamlit Cloud.
   - Set **Main file path**: `delivery_apps/app.py`
   - Click **Deploy**

### Option B: Deploying Portal to Vercel
The root directory includes `index.html` and `vercel.json` configured as a static web portal:
1. Connect this GitHub repository to [Vercel](https://vercel.com/).
2. Vercel will immediately deploy the static portal dashboard without any build errors.
3. You can paste your live Streamlit Cloud URLs directly into the portal cards.

---

## 🔒 Security & Git Hygiene
The `.gitignore` file automatically excludes:
- Python virtual environments (`.venv/`, `venv/`)
- Compiled Python caches (`__pycache__/`, `*.pyc`)
- Streamlit secrets (`secrets.toml`) and environment variables (`.env`)
- Local archive zips and OS metadata files
