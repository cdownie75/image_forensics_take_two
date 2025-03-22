
# Image Forensics Dashboard

This repository contains a Streamlit-based image forensics dashboard that detects signs of image manipulation.

## 📁 Contents

- `streamlit_dashboard.py`: Streamlit Cloud frontend
- `image_analysis_pipeline.py`: Python-based image analysis tool
- `forensic_reports.json`: Sample output for dashboard testing
- `images/`: Example images used for analysis
- `requirements.txt`: Python dependencies

## 🚀 Streamlit Cloud Setup

1. Push this folder to a new GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Choose this repo and set `streamlit_dashboard.py` as the main file.
4. Done!

## 🧪 Local Testing

```bash
pip install -r requirements.txt
python image_analysis_pipeline.py
streamlit run streamlit_dashboard.py
```
