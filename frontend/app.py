import streamlit as st
import requests
import time
import os
from dotenv import load_dotenv
import base64
import re

load_dotenv()

API_URL = "http://127.0.0.1:8000/assistant"

# --- Custom CSS ---
def add_bg_from_url():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #eef2f3, #8e9eab);
            color: #1e1e1e;
        }
        </style>
    """, unsafe_allow_html=True)

def local_css():
    st.markdown("""
        <style>
        /* Normal Submit button */
.stForm button {
    background-color: #4a86e8 !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    padding: 10px 20px !important;
    border-radius: 8px !important;
    border: none !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    transition: background 0.3s ease-in-out;
    opacity: 1 !important;
}

/* Hover state */
.stForm button:hover:enabled {
    background-color: #3b6ac9 !important;
    color: #ffffff !important;
}

/* DISABLED state */
.stForm button:disabled {
    background-color: #d3d3d3 !important;
    color: #888 !important;
    cursor: not-allowed !important;
    opacity: 1 !important;
}
        .main-header {
            font-size: 2.5rem;
            font-weight: 700;
            color: #0f2027;
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }

        .subheader {
            font-size: 1.2rem;
            color: #243b55;
            margin-bottom: 2rem;
        }

        .feature-title, p, li {
            color: #222;
        }

        h1, h2, h3, h4 {
            color: #0f2027;
            margin-bottom: 1rem;
        }

        .feature-row {
            display: flex;
            justify-content: space-around;
            margin: 3rem 0;
        }

        .feature-item {
            text-align: center;
            padding: 20px;
        }

        .feature-icon {
            background-color: #fff;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 15px auto;
            box-shadow: 0 2px 5px rgba(0,0,0,0.15);
        }

        .feature-icon span {
            font-size: 2rem;
        }

        .upload-section {
            margin-top: 3rem;
            padding: 2rem;
            background: #ffffffaa;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .response-container {
            background-color: #f9f9f9;
            padding: 1.2rem;
            border-radius: 10px;
            border-left: 4px solid #4a86e8;
            color: #222;
            font-size: 1rem;
            line-height: 1.6;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
            margin-top: 1rem;
        }

        .stButton > button {
            background-color: #4a86e8 !important;
            color: #fff !important;
            font-weight: 600;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            transition: background 0.3s ease;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .stButton > button:hover {
            background-color: #3b6ac9 !important;
        }

        /* Chat input */
        input[type="text"] {
            background-color: #ffffff !important;
            color: #1e1e1e !important;
            border: 2px solid #4a86e8 !important;
            border-radius: 8px !important;
            padding: 12px;
            font-size: 16px;
            font-weight: 500;
            box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
        }

        input[type="text"]:focus {
            border-color: #3b6ac9 !important;
            outline: none !important;
        }

        /* Submit button inside st.form */
        form button {
            background-color: #4a86e8 !important;
            color: white !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            padding: 10px 20px !important;
            border-radius: 8px !important;
            border: none !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            transition: background 0.3s ease-in-out;
        }

        form button:hover {
            background-color: #3b6ac9 !important;
            color: #ffffff !important;
        }
        
        </style>
    """, unsafe_allow_html=True)



# Apply styles
add_bg_from_url()
local_css()

# --- Header ---
st.markdown("""
<div class="main-header">
    <span style="margin-right:10px;">🎓</span> AI Powered Study Assistant
</div>
<div class="subheader">
    Your Personalized Learning Assistant
</div>
""", unsafe_allow_html=True)

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["📚 Learn", "ℹ️ About", "❓ How to Use"])

with tab1:
    st.markdown("""
    Upload your study material and let our AI transform your learning experience:
    - 📝 **Instant Summaries**
    - 🧠 **Interactive AI Quizzes**
    - 💬 **AI Tutor**
    """)
    st.markdown("""
    <div class="feature-row">
        <div class="feature-item"><div class="feature-icon"><span>📚</span></div><div class="feature-title">Smart Summaries</div></div>
        <div class="feature-item"><div class="feature-icon"><span>🧠</span></div><div class="feature-title">AI Quizzes</div></div>
        <div class="feature-item"><div class="feature-icon"><span>💬</span></div><div class="feature-title">AI Tutor</div></div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("## About Study Buddy AI\nStudy Buddy AI combines NLP with educational intelligence to create personalized learning experiences.")

with tab3:
    st.markdown("## Getting Started\n1. Upload your PDF\n2. Click 'Create Quiz'\n3. Answer & Submit\n4. Enjoy instant feedback!")

# --- Upload Section ---
st.markdown("""
<div class="upload-section">
    <h2 style="margin: 0; display: flex; align-items: center;">
        <span style="margin-right:10px; font-size: 1.5rem;">📄</span>
        Upload Your Study Material
    </h2>
</div>
""", unsafe_allow_html=True)

if 'uploaded_file' not in st.session_state:
    st.session_state['uploaded_file'] = None

uploaded_file = st.file_uploader("Select a PDF file to get started", type=["pdf"], key="file_uploader")

if uploaded_file and st.session_state['uploaded_file'] is None:
    st.session_state['uploaded_file'] = uploaded_file
    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ File uploaded successfully!")
    with st.spinner("🧠 Processing document for chat..."):
        with open("temp_uploaded.pdf", "rb") as f:
            res_process = requests.post(f"{API_URL}/upload", files={"file": f})
        if res_process.status_code == 200:
            st.info("✅ Document processed for chat.")
        else:
            st.error("❌ Failed to process document.")

col1, col2 = st.columns(2)
with col1:
    summarize_btn = st.button("📝 Generate Summary", use_container_width=True, disabled=not uploaded_file)
with col2:
    quiz_btn = st.button("🧠 Create Quiz", use_container_width=True, disabled=not uploaded_file)

# --- Summary ---
if summarize_btn:
    with st.spinner("🤖 Creating summary..."):
        with open("temp_uploaded.pdf", "rb") as f:
            res = requests.post(f"{API_URL}/summarize", files={"file": f})
        if res.status_code == 200:
            summary = res.json().get("summary", "No summary found.")
            with st.expander("📝 Your Document Summary", expanded=True):
                st.markdown("### Key Points Summary")
                st.markdown(summary)
                b64 = base64.b64encode(summary.encode()).decode()
                st.markdown(f'<a href="data:text/plain;base64,{b64}" download="document_summary.txt">Download Summary</a>', unsafe_allow_html=True)
        else:
            st.error("❌ Failed to summarize.")

# --- Quiz ---
if quiz_btn:
    with st.spinner("🧩 Creating quiz..."):
        with open("temp_uploaded.pdf", "rb") as f:
            res = requests.post(f"{API_URL}/generate-quiz", files={"file": f}, data={"num_questions": 5})
        if res.status_code == 200:
            quiz_text = res.json().get("quiz")
            if quiz_text and isinstance(quiz_text, str):
                for key in ['llm_quiz_data', 'llm_user_answers', 'quiz_submitted']:
                    st.session_state.pop(key, None)
                questions = re.split(r"Question \d+[:：]?", quiz_text)[1:]
                st.session_state['llm_quiz_data'] = []
                for q_text in questions:
                    lines = q_text.strip().split('\n')
                    question = ""
                    options = {}
                    correct_answer = None
                    for line in lines:
                        line = line.strip()
                        if line.startswith(('A)', 'B)', 'C)', 'D)')):
                            options[line[0]] = line[2:].strip()
                        elif line.startswith("Correct Answer:"):
                            correct_answer = line.split(":")[-1].strip().split(')')[0].strip()
                        elif line and not line.startswith("Question") and not question:
                            question = line.strip()
                    st.session_state['llm_quiz_data'].append({
                        'question': question,
                        'options': options,
                        'correct_answer': correct_answer
                    })
                st.session_state['llm_user_answers'] = {}
                st.session_state['llm_quiz_expanded'] = True
                st.session_state['quiz_submitted'] = False
            else:
                st.warning("⚠️ No quiz content received.")
        else:
            st.error("❌ Failed to generate quiz.")

# --- Render Quiz ---
if 'llm_quiz_data' in st.session_state:
    with st.expander("🧠 Interactive Quiz", expanded=st.session_state.get('llm_quiz_expanded', False)):
        st.markdown("#### Answer the questions below:")
        with st.form("llm_quiz_form"):
            user_answers = {}
            for i, q_data in enumerate(st.session_state['llm_quiz_data']):
                question = q_data['question']
                options = q_data['options']
                st.markdown(f"**Question {i+1}: {question}**")
                selected_answer = st.radio(
                    f"Select your answer for Question {i+1}",
                    options=list(options.keys()),
                    format_func=lambda x: f"{x}) {options[x]}",
                    key=f"llm_q_{i}",
                    index=None
                )
                user_answers[i] = selected_answer
            submitted_llm = st.form_submit_button("Submit Quiz")
            if submitted_llm:
                st.session_state['llm_user_answers'] = user_answers
                st.session_state['quiz_submitted'] = True
                st.session_state['llm_quiz_expanded'] = True

# --- Show Results ---
if st.session_state.get('quiz_submitted', False):
    st.markdown("### 📝 Quiz Results:")
    score = 0
    for i, q_data in enumerate(st.session_state['llm_quiz_data']):
        question = q_data['question']
        options = q_data['options']
        correct_answer = q_data['correct_answer']
        user_answer = st.session_state['llm_user_answers'].get(i)
        st.markdown(f"**Question {i+1}:** {question}")
        st.markdown(f"Your Answer: **{user_answer}) {options.get(user_answer, 'Not Answered')}**")
        st.markdown(f"Correct Answer: **{correct_answer}) {options.get(correct_answer, 'N/A')}**")
        if user_answer == correct_answer:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error("❌ Incorrect.")
        st.divider()
    st.markdown(f"### 🏆 Your Score: {score} / {len(st.session_state['llm_quiz_data'])}")

# --- Reset Button (Always Shown if Quiz Exists) ---

if 'llm_quiz_data' in st.session_state:
    st.markdown("---")
    if st.button("🔁 Reset Quiz"):
        for key in list(st.session_state.keys()):
            if key.startswith("llm_q_"):
                del st.session_state[key]
        for key in ['llm_quiz_data', 'llm_user_answers', 'quiz_submitted', 'llm_quiz_expanded']:
            st.session_state.pop(key, None)
        st.success("✅ Quiz has been reset.")
        st.rerun()  # 🔥 force rerender so radio buttons clear!


# --- Chatbot ---
st.markdown("### 💬 Ask Questions About Your Material")
user_query = st.text_input("What would you like to know?")
if st.button("💡 Get Answer", disabled=st.session_state['uploaded_file'] is None):
    if user_query:
        with st.spinner("🧠 Searching for the best answer..."):
            res = requests.post(f"{API_URL}/chat", data={"query": user_query})
            if res.status_code == 200:
                response = res.json().get("response", "No response found.")
                st.markdown("#### 🤖 Answer:")
                st.markdown(f"<div class='response-container'>{response}</div>", unsafe_allow_html=True)
            else:
                st.error("❌ Failed to get an answer.")
    else:
        st.warning("⚠️ Please enter a question.")
