import streamlit as st
from pathlib import Path
from PIL import Image
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie



### PATH Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "omkar-kadam-resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



def load_lottie(url):
     r = requests.get(url)
     if r.status_code != 200:
          return None
     return r.json()

### Lottie animations
lottie_contact = load_lottie("https://lottie.host/b02b1461-7038-41ba-824e-2ce7cfd28a29/vgA8Snk1d9.json")
lot_contact = load_lottie("https://lottie.host/9aa59944-e81b-48c5-a126-ca70f0651cdd/eRnyFXR1Ko.json")




        

## -- General Settings

PAGE_TITLE = "Digital CV | Omkar Kadam "
PAGE_ICON = ":wave:"
NAME = "OMKAR KADAM"
DESCRIPTION = """
🕵️‍♂️ Hello Everyone,
In the realm of data, consider me your Sherlock Holmes. I am a seasoned Data Analyst/Scientist, specializing in a wide range of projects that span the entire data spectrum.
""" 
EMAIL= "kadam.omkar05@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/omkar-kadam05/",
    "GitHub":"https://github.com/omkarkd",
    "Publication":"https://www.ijert.org/a-modern-approach-towards-stock-prediction-over-traditional-methods",
    "Badges":"https://www.credly.com/users/omkar-kadam.272a91c1"

}
PROJECTS = {
    "🏆 ChatPDF: - LLM based chat application developed for the purpose of chatting with your pdf files, irrespective of the size of the document.",
    "🏆 Smart Shop Manager - This application was developed for a retail store for employees without any tech background",
    "🏆 Trending Video Insights - Built an end-to-end automated data pipeline solution to perform video analytics and trend analytics."
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
exp_col, skills_col = st.columns(2)

with exp_col:
    st.write('\n')
    st.subheader("🚀 Scope of My Work:")
    st.write(
        """
        - ✔️ Data Visualization: Transforming raw data into compelling visuals.
        - ✔️ Data Cleaning: Tidying up messy data for meaningful analysis.
        - ✔️ Model Fitting: Crafting data models for precise insights.
        - ✔️ Data Scraping/Extraction: Retrieving valuable information from the web.
        - ✔️ Data Mining: Digging deep to unearth hidden patterns.
        - ✔️ Machine Learning: Harnessing the power of algorithms for predictive analysis.
        - ✔️ Data Modeling: Creating structured data sets for informed decisions.
        """
    )

with skills_col:
    st.write('\n')
    st.subheader("💼 Tools of the Trade:")
    st.write(
        """
        - 👩‍💻 Programming: Python(Flask, TensorFlow, Streamlit, CNN), SQL.
        - 📊 Data Visualization: Tableau, PowerBi, MS Excel, Chart.js, Plotly, D3.js.
        - 📚 Modeling: Clustering techniques, Classification techniques, Linear Regression, Forecasting models, XGBoost, Logistic regression, Decision trees,Machine Learning.
        - 🗄️ Databases: MongoDB, SQL, NoSQL.
        - 🧠📚 NLP: Word2vec, Gensim, Semantic Analysis, Spacy, NER (Named Entity Recognition), .
        - ☁️ Cloud: Docker, Azure, Google Cloud Platform (GCP).
        - LLM: Gemini ai, Prompt Engineering, OpenAI, Langchain
        - 🧰🛠️ Others: Git, Microsoft Excel, Text ranking algorithm, Semantic Analysis, Elastic-search, , .
        """
    )

# --- Projects & Accomplishments ---
# st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project in PROJECTS:
    st.write(f"[{project}]")

st.write('\n')

# --- WORK HISTORY ---
st.subheader("Work History")
st.write("---")
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Employment Journey","Teaching Journey","Contact"],
        icons=['person','bi-person-check-fill','chat-left-text-fill'],
        orientation = "horizontal"
    )
if selected == "Employment Journey":
        
        st.write("🚧", "**Data Science Consultant | Naviya Technologies**")
        st.write("02/2020 - Present")
        st.write(
            """
        - ► Responsible for Designing and Developing Data models in-line with Business Requirement.
        - ► Led a team of 5 analysts to brainstorm KPI's and other performance stratergies, and implemented A/B tests.
        - ► Developed and Automated end-to-end Data analytics pipeline.
        """
        )

        st.write('\n')
        st.write("🚧", "**Consulting Data Analyst (Finance: Systems Team) | Zs-Associates**")
        st.write("02/2020 - Present")
        st.write(
            """
        - ► Identify areas for improvement in company finance processes.
        - ► Responsible for Gathering new requirements for introducing a new module in the existing system.
        - ► Performing the feasibility checks within modules ensuring high availability and performance.
        - ► Communicating the client requirements effectively to the developers.
        """
        )


        st.write('\n')
        st.write("🚧", "**Data Scientist | Ilink Digital**")
        st.write("02/2020 - Present")
        st.write(
            """
        - ► Worked Closely with offshore End-Users, 
            Data management team and onshored team of Data scientist to develop and deploy machine learning model which revoled around price-elasticity and other economic factors for PepsiCo.
        - ► Demostrated a working POC using Azure Data Lakes and Azure Machine Learning Studio. 
        - ► :award: Awarded for "Most Assisting" across multiple, functional Projects/Teams.
        """
        )

        st.write('\n')
        st.write("🚧", "**Data Analyst(Product Development) | ZingHr**")
        st.write("02/2020 - Present")
        st.write(
            """
        - ► Led the implementation of a Resume and JD Similarity algorithm.
        - ► Spearheaded the ideation, development, integration, and deployment of a Resume Parser system
        which serves over 750+ clients globally and involved ideation for V2 enhancements.
        """
        )



if selected == "Contact":
        st.header("Get in touch!")
        st.write("##")  
        st.write("##")   

        contact_form = """   
        <form action="https://formsubmit.co/kadam.omkar05@gmail.com" method="POST">
            <input type = "hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Name" required>
            <input type="email" name="email" placeholder="Mail"required>
            <textarea name = "message", placeholder="your message" required>
            <button type="submit">Send</button>
        </form>


        """
        left_col,right_col = st.columns((2,1))
        with left_col:
             st.markdown(
                  contact_form,unsafe_allow_html=True
             )
        with right_col:
             st_lottie(lot_contact)
