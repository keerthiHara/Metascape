# import streamlit as st

# # Predefined questions and answers
# social_media_questions = [
#     "what is social media?", "how does social media work?", "what are the benefits of social media?",
#     "why is social media important?", "what are the popular social media platforms?", "can social media affect mental health?"
# ]
# social_media_answers = {
#     "what is social media?": "Social media refers to online platforms where people can create, share, and interact with content. Popular examples include Facebook, Instagram, Twitter, etc.",
#     "how does social media work?": "Social media works by allowing users to create content, interact with others through likes, comments, shares, and follow or be followed by other users.",
#     "what are the benefits of social media?": "Social media offers several benefits like staying connected with family and friends, networking opportunities, and access to news and information.",
#     "why is social media important?": "Social media is important for communication, entertainment, business marketing, and education. It helps build communities and connect people globally.",
#     "what are the popular social media platforms?": "Some of the popular social media platforms include Facebook, Instagram, Twitter, LinkedIn, TikTok, and YouTube.",
#     "can social media affect mental health?": "Yes, excessive use of social media can sometimes lead to mental health issues such as anxiety, depression, and loneliness. It's important to manage screen time and engage positively."
# }

# general_answers = {
#     "hi": "Hello! How can I help you today?",
#     "hello": "Hi there! How can I assist you?",
#     "how are you": "I'm doing well, thank you for asking! How about you?",
#     "how was your day": "My day has been great, thanks for asking! How about yours?",
#     "what's up": "Not much, just here to assist you. How can I help?",
#     "good morning": "Good morning! How can I assist you today?",
#     "good evening": "Good evening! What can I do for you?"
# }

# # Emotion-based video recommendations
# emotion_videos = {
#     "It’s all too much, I can’t focus, my heart’s racing.": {
#         "emotion": "high stress",
#         "video": "https://www.youtube.com/watch?v=c5ktpqERTrQ"
#     },
#     "I feel a little off, like there’s a weight on my shoulders.": {
#         "emotion": "mild stress",
#         "video": "https://www.youtube.com/watch?v=Urh57dgnEVA"
#     },
#     "My thoughts won’t stop racing and I feel on edge.": {
#         "emotion": "anxious",
#         "video": "https://www.youtube.com/watch?v=GqV8LZJR0Qk"
#     },
#     "Everything is annoying me right now, I’m so irritable.": {
#         "emotion": "irritated",
#         "video": "https://www.youtube.com/watch?v=KgloGxiTtZA"
#     },
#     "I feel overwhelmed and like I can’t handle anything else.": {
#         "emotion": "overwhelmed",
#         "video": "https://www.youtube.com/watch?v=fryDy9YcbI4"
#     },
#     "Am feeling worried because I lost my mark… I just feel sad.": {
#         "emotion": "sad",
#         "video": "https://www.youtube.com/watch?v=eKumVFvGHFA"
#     },
#     "I’m so tired mentally, like I’ve been drained.": {
#         "emotion": "mentally exhausted",
#         "video": "https://www.youtube.com/watch?v=m7v_YQyv95s"
#     },
#     "Everything is going wrong and I feel so frustrated.": {
#         "emotion": "frustrated",
#         "video": "https://www.youtube.com/watch?v=2MAhf196a6U"
#     },
#     "I can’t sit still, I feel super restless.": {
#         "emotion": "restless",
#         "video": "https://www.youtube.com/watch?v=74F6lAOLtyA"
#     },
#     "I’m completely burned out and can’t keep going like this.": {
#         "emotion": "burnout",
#         "video": "https://www.youtube.com/watch?v=8Du1hrPrV38"
#     },
#     "I just have no energy left for anything today.": {
#         "emotion": "low energy",
#         "video": "https://www.youtube.com/watch?v=7ohzYII08eQ"
#     },
#     "I’m angry and I just want to scream!": {
#         "emotion": "angry",
#         "video": "https://www.youtube.com/watch?v=GqV8LZJR0Qk"
#     },
#     "I can’t sleep, my mind won’t shut off at night.": {
#         "emotion": "trouble sleeping",
#         "video": "https://www.youtube.com/watch?v=7AkbUfZjS5k"
#     },
#     "I’m calm but I really want to just relax and unwind.": {
#         "emotion": "calm but wants relaxation",
#         "video": "https://www.youtube.com/watch?v=Gf0Wlo6hJMg"
#     },
#     "It’s hard to breathe, my chest is tight… I feel like everything is falling apart.": {
#         "emotion": "panic attack",
#         "video": "https://www.youtube.com/watch?v=KgloGxiTtZA"
#     },
#     "I feel so alone even when I’m with people.": {
#         "emotion": "lonely",
#         "video": "https://www.youtube.com/watch?v=Mc83fY0v3g8"
#     },
#     "I’m smiling, but deep down I’m tense and uneasy.": {
#         "emotion": "happy but tense",
#         "video": "https://www.youtube.com/watch?v=hEdzv7D4CbQ"
#     },
#     "This reminds me of old times… I feel so nostalgic.": {
#         "emotion": "nostalgic",
#         "video": "https://www.youtube.com/watch?v=jqq_ZdD5Zwg"
#     },
#     "I feel peaceful right now and just want to enjoy the moment.": {
#         "emotion": "peaceful",
#         "video": "https://www.youtube.com/watch?v=3offgJ5kSM0"
#     },
#     "I feel hopeless, like nothing will ever get better.": {
#         "emotion": "hopeless",
#         "video": "https://www.youtube.com/watch?v=Ra_4N3n0yQs"
#     }
# }

# # Set background
# def set_background():
#     background_image_url = "https://media.gettyimages.com/id/1433585361/video/cyber-attack-in-the-article-and-text.jpg?s=640x640&k=20&c=rdOMYjDydDqkC8qtU1DWaPRVady17dhXN-n569ErezM="
#     st.markdown(f"""
#         <style>
#         .stApp {{
#             background-image: url("{background_image_url}");
#             background-size: cover;
#             background-position: center;
#             background-attachment: fixed;
#         }}
#         </style>
#     """, unsafe_allow_html=True)

# # Chatbot logic
# def chatbot():
#     set_background()
#     st.title("💬 Smart ChatBot")

#     if 'messages' not in st.session_state:
#         st.session_state.messages = []

#     def get_answer(user_input):
#         user_input = user_input.lower().strip()

#         # General answers
#         if user_input in general_answers:
#             return general_answers[user_input]

#         # Social media Q&A
#         if user_input in social_media_questions:
#             return social_media_answers.get(user_input)

#         # Emotion-based video
#         for emotion_desc, data in emotion_videos.items():
#             if emotion_desc.lower() in user_input:
#                 return f"You seem to be feeling **{data['emotion'].title()}**. Here's something that might help: [Watch Video]({data['video']})"

#         return "I'm sorry, I don't have an answer for that. Can you ask something else?"

#     # Input section
#     user_input = st.text_input("Type your message:", "")
#     if user_input:
#         response = get_answer(user_input)
#         st.session_state.messages.append(("You", user_input))
#         st.session_state.messages.append(("Bot", response))

#     # Display chat
#     for sender, message in reversed(st.session_state.messages):
#         align = "right" if sender == "You" else "left"
#         bg_color = "#e0e0e0" if sender == "You" else "#cfe2f3"
#         st.markdown(
#             f'<div style="background-color:{bg_color}; border-radius: 10px; padding: 10px; text-align:{align}; margin-bottom:10px;">'
#             f"<b>{sender}:</b> {message}</div>",
#             unsafe_allow_html=True
#         )

# # Run the chatbot
# chatbot()



# --------------------------------------------------------------------------------------------------------------------


import streamlit as st
import requests
# import textblob
# import Q-table 
import os

# Set your Groq API key here or through an environment variable
GROQ_API_KEY = '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'
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'
GROQ_MODEL_NAME = 'meta-llama/llama-4-scout-17b-16e-instruct'  # You can switch to llama3-8b-8192, etc.

# Predefined questions and answers
social_media_questions = [
    "what is social media?", "how does social media work?", "what are the benefits of social media?",
    "why is social media important?", "what are the popular social media platforms?", "can social media affect mental health?"
]
social_media_answers = {
    "what is social media?": "Social media refers to online platforms where people can create, share, and interact with content. Popular examples include Facebook, Instagram, Twitter, etc.",
    "how does social media work?": "Social media works by allowing users to create content, interact with others through likes, comments, shares, and follow or be followed by other users.",
    "what are the benefits of social media?": "Social media offers several benefits like staying connected with family and friends, networking opportunities, and access to news and information.",
    "why is social media important?": "Social media is important for communication, entertainment, business marketing, and education. It helps build communities and connect people globally.",
    "what are the popular social media platforms?": "Some of the popular social media platforms include Facebook, Instagram, Twitter, LinkedIn, TikTok, and YouTube.",
    "can social media affect mental health?": "Yes, excessive use of social media can sometimes lead to mental health issues such as anxiety, depression, and loneliness. It's important to manage screen time and engage positively."
}

general_answers = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How can I assist you?",
    "how are you": "I'm doing well, thank you for asking! How about you?",
    "how was your day": "My day has been great, thanks for asking! How about yours?",
    "what's up": "Not much, just here to assist you. How can I help?",
    "good morning": "Good morning! How can I assist you today?",
    "good evening": "Good evening! What can I do for you?"
}

# Emotion-based video recommendations
emotion_videos = {
    "I can’t focus": {
        "emotion": "high stress",
        "video": "https://www.youtube.com/watch?v=c5ktpqERTrQ"
    },
    "there’s a weight on my shoulders": {
        "emotion": "mild stress",
        "video": "https://www.youtube.com/watch?v=Urh57dgnEVA"
    },
    "My thoughts won’t stop": {
        "emotion": "anxious",
        "video": "https://www.youtube.com/watch?v=GqV8LZJR0Qk"
    },
    "Everything is annoying me right now": {
        "emotion": "irritated",
        "video": "https://www.youtube.com/watch?v=KgloGxiTtZA"
    },
    "I feel overwhelmed": {
        "emotion": "overwhelmed",
        "video": "https://www.youtube.com/watch?v=fryDy9YcbI4"
    },
    "I just feel sad": {
        "emotion": "sad",
        "video": "https://www.youtube.com/watch?v=eKumVFvGHFA"
    },
    "I’m so tired mentally": {
        "emotion": "mentally exhausted",
        "video": "https://www.youtube.com/watch?v=m7v_YQyv95s"
    },
    "I feel so frustrated": {
        "emotion": "frustrated",
        "video": "https://www.youtube.com/watch?v=2MAhf196a6U"
    },
    "I feel super restless": {
        "emotion": "restless",
        "video": "https://www.youtube.com/watch?v=74F6lAOLtyA"
    },
    "I’m completely burned out": {
        "emotion": "burnout",
        "video": "https://www.youtube.com/watch?v=8Du1hrPrV38"
    },
    "I just have no energy left for anything today": {
        "emotion": "low energy",
        "video": "https://www.youtube.com/watch?v=7ohzYII08eQ"
    },
    "im angry": {
        "emotion": "angry",
        "video": "https://www.youtube.com/watch?v=GqV8LZJR0Qk"
    },
    "i cant sleep": {
        "emotion": "trouble sleeping",
        "video": "https://www.youtube.com/watch?v=7AkbUfZjS5k"
    },
    "I’m calm but I want to just relax": {
        "emotion": "calm but wants relaxation",
        "video": "https://www.youtube.com/watch?v=Gf0Wlo6hJMg"
    },
    "It’s hard to breathe": {
        "emotion": "panic attack",
        "video": "https://www.youtube.com/watch?v=KgloGxiTtZA"
    },
    "i feel so alone": {
        "emotion": "lonely",
        "video": "https://www.youtube.com/watch?v=Mc83fY0v3g8"
    },
    "I’m smiling, but deep down I’m tense and uneasy.": {
        "emotion": "happy but tense",
        "video": "https://www.youtube.com/watch?v=hEdzv7D4CbQ"
    },
    "This reminds me of old times": {
        "emotion": "nostalgic",
        "video": "https://www.youtube.com/watch?v=jqq_ZdD5Zwg"
    },
    "I feel peaceful right now and just want to enjoy the moment.": {
        "emotion": "peaceful",
        "video": "https://www.youtube.com/watch?v=3offgJ5kSM0"
    },
    "I feel hopeless": {
        "emotion": "hopeless",
        "video": "https://www.youtube.com/watch?v=Ra_4N3n0yQs"
    }
}


def set_background():
    background_image_url = "https://www.claysys.com/app/uploads/2022/03/AI_Chatbots.png"
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

def llama_generate(prompt):
    """Call Groq LLaMA API and return response."""
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': GROQ_MODEL_NAME,
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}
        ],
        'max_tokens': 128,
        'temperature': 0.7
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    else:
        return f"Error: {response.status_code}, {response.text}"

def chatbot():
    set_background()
    st.title("METASCAPE'S BOT")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    def get_answer(user_input):
        user_input_lower = user_input.lower().strip()

        if user_input_lower in general_answers:
            return general_answers[user_input_lower]
        if user_input_lower in social_media_questions:
            return social_media_answers.get(user_input_lower)

        for emotion_desc, data in emotion_videos.items():
            if emotion_desc.lower() in user_input_lower:
                return f"You seem to be feeling **{data['emotion'].title()}**. Here's something that might help: [Watch Video]({data['video']})"

        # If no match, fallback to Groq LLaMA model
        llama_response = llama_generate(user_input)
        return llama_response if llama_response else "I'm sorry, I don't have an answer for that."

    user_input = st.text_input("Type your message:", "")
    if user_input:
        response = get_answer(user_input)
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Bot", response))

    for sender, message in reversed(st.session_state.messages):
        align = "right" if sender == "You" else "left"
        bg_color = "#e0e0e0" if sender == "You" else "#cfe2f3"
        st.markdown(
            f'<div style="background-color:{bg_color}; border-radius: 10px; padding: 10px; text-align:{align}; margin-bottom:10px;">'
            f"<b>{sender}:</b> {message}</div>",
            unsafe_allow_html=True
        )

chatbot()
