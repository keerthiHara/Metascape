# import streamlit as st
# from transformers import pipeline
# import json
# import requests

# # Load emotion model
# @st.cache_resource
# def load_model():
#     return pipeline("text-classification", model="nateraw/bert-base-uncased-emotion")
# # Traceback:
# # File "C:\Users\Mithun\OneDrive\Desktop\VR CODE\finalwork.py", line 11, in <module>
# #     model = load_model()
# # File "c:\users\mithun\appdata\local\programs\python\python39\lib\site-packages\streamlit\runtime\caching\cache_utils.py", line 218, in __call__
# #     return self._get_or_create_cached_value(args, kwargs, spinner_message)
# # File "c:\users\mithun\appdata\local\programs\python\python39\lib\site-packages\streamlit\runtime\caching\cache_utils.py", line 260, in _get_or_create_cached_value
# #     return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)
# # File "c:\users\mithun\appdata\local\programs\python\python39\lib\site-packages\streamlit\runtime\caching\cache_utils.py", line 318, in _handle_cache_miss
# #     computed_value = self._info.func(*func_args, **func_kwargs)
# # File "C:\Users\Mithun\OneDrive\Desktop\VR CODE\finalwork.py", line 9, in load_model
# #     return pipeline("text-classification", model="nateraw/bert-base-uncased-emotion")
# # File "c:\users\mithun\appdata\local\programs\python\python39\lib\site-packages\transformers\pipelines\__init__.py", line 754, in pipeline
# #     framework, model = infer_framework_load_model(
# # File "c:\users\mithun\appdata\local\programs\python\python39\lib\site-packages\transformers\pipelines\base.py", line 266, in infer_framework_load_model
# #     raise ValueError(f"Could not load model {model} with any of the followin

# model = load_model()

# # Emotion mapping
# emotion_map = {
#     "anger": "Angry",
#     "sadness": "Sad",
#     "joy": "Happy",
#     "fear": "Fear",
#     "love": "Love",
#     "surprise": "Surprised"
# }

# # Streamlit UI
# st.title("🧠 Detect Emotion & Send to Google Sheet")
# name = st.text_input("Enter your name")
# text = st.text_area("Describe your feeling")

# if st.button("Detect Emotion and Send"):
#     if not name.strip() or not text.strip():
#         st.warning("Please provide both name and text.")
#     else:
#         # Run model
#         result = model(text)[0]
#         label = result["label"].lower()
#         readable_emotion = emotion_map.get(label, label.capitalize())

#         # Prepare JSON
#         data = {
#             "UserName": name,
#             "Emotion": readable_emotion
#         }

#         st.subheader("📦 Emotion JSON:")
#         st.code(json.dumps(data, indent=2), language="json")

#         # Google Apps Script Web App URL
#         webhook_url = "https://script.google.com/macros/s/AKfycbx-35LOrAXI_CJMu1aZy63Kqcf9fL7r0Ts-QkO4KZSW4HH187UTSJjR6UrTDsLMhJyA/exec"

#         # Send data to Google Sheet
#         try:
#             response = requests.post(webhook_url, json=data)
#             if response.status_code == 200:
#                 st.success("✅ Data sent to Google Sheet successfully!")
#             else:
#                 st.error(f"⚠️ Failed with status code: {response.status_code}")
#         except Exception as e:
#             st.error(f"❌ Error sending data: {e}")

import streamlit as st
from transformers import pipeline
import json
import requests

# Load emotion model
@st.cache_resource
def load_model():
    return pipeline("text-classification", model="nateraw/bert-base-uncased-emotion")

model = load_model()

# Emotion mapping
emotion_map = {
    "anger": "Angry",
    "sadness": "Sad",
    "joy": "Happy",
    "fear": "Fear",
    "love": "Love",
    "surprise": "Surprised"
}

# Subcategory mapping for sadness
def get_sadness_subcategory(text):
    text_lower = text.lower()
    if any(word in text_lower for word in ["overwhelmed", "burnout", "stressed", "pressure"]):
        return "Stressed"
    elif any(word in text_lower for word in ["empty", "worthless", "hopeless", "depressed", "numb"]):
        return "Depression"
    elif any(word in text_lower for word in ["alone", "isolated", "lonely", "abandoned"]):
        return "Loneliness"
    else:
        return "Sad"

# Streamlit UI
st.title("🧠 let me analysis your Emotion")
name = st.text_input("Enter your name")
text = st.text_area("Describe your feeling")

if st.button("Detect Emotion and Send"):
    if not name.strip() or not text.strip():
        st.warning("Please provide both name and text.")
    else:
        # Run model
        result = model(text)[0]
        label = result["label"].lower()

        if label == "sadness":
            readable_emotion = get_sadness_subcategory(text)
        else:
            readable_emotion = emotion_map.get(label, label.capitalize())

        # Prepare JSON
        data = {
            "UserName": name,
            "Emotion": readable_emotion
        }

        st.subheader("📦 Emotion JSON:")
        st.code(json.dumps(data, indent=2), language="json")

        # Google Apps Script Web App URL
        webhook_url = "https://script.google.com/macros/s/AKfycbx-35LOrAXI_CJMu1aZy63Kqcf9fL7r0Ts-QkO4KZSW4HH187UTSJjR6UrTDsLMhJyA/exec"

        # Send data to Google Sheet
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 200:
                st.success("✅ Data sent to Google Sheet successfully!")
            else:
                st.error(f"⚠️ Failed with status code: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Error sending data: {e}")
