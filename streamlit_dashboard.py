### Paste your full Streamlit dashboard code here from Canvas ###
# streamlit_dashboard.py
import streamlit as st
import json
import os
from PIL import Image

st.title("Image Forensics Dashboard")
with open("forensic_reports.json") as f:
    data = json.load(f)

for item in data["reports"]:
    st.subheader(item["filename"])
    st.image(f"images/{item['filename']}")
    st.write("Flagged:", "Yes" if item.get("flagged") else "No")
    if item.get("flagged"):
        st.write("Tokens used:", item["tokens_used"])
        st.write("Estimated cost:", f"${item['estimated_cost_usd']}")
        st.write("GPT-3.5 Report:")
        st.code(item["gpt35_report"])
