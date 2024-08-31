import streamlit as st
import os

st.set_page_config(page_title="My Portfolio with Media", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    body {
        background-color: #fff;
        color: #ff69b4;
    }
    
    .css-18e3th9 {
        background-color: #ffe4e1 !important;
    }
    
    .css-10trblm {
        color: #ff69b4;
    }

    .css-qbe2hs {
        color: #ff69b4 !important;
        font-size: 24px !important;
    }

    input[type="text"], input[type="email"], textarea {
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        border: 2px solid #ff69b4;
        width: 100%;
        box-sizing: border-box;
        color: #ff69b4;
    }

    button {
        background-color: #ff69b4;
        color: white;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        border-radius: 5px;
    }
    
    button:hover {
        background-color: #ff85b8;
    }

    form {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    input, textarea {
        margin-bottom: 0;
    }

    textarea {
        height: 100px;
        resize: none;
    }

    button {
        margin-top: 20px;
    }

    a {
        color: #ff69b4;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    </style>
""", unsafe_allow_html=True)

st.sidebar.title("About Me")
pages = ["Home", "Autobiography", "Portfolio", "Media Gallery", "Contact"]
page = st.sidebar.radio("Go to", pages)

# Define relative paths for images
def get_image_path(filename):
    return os.path.join("images", filename)

if page == "Home":
    st.title("Hello, Welcome!")
    st.write("""
        Hello! I'm Julianne Kristine D. Aban, a 4th Year BSIT Student in Cebu Institute of Technology - University.
        Explore my journey, skills, and projects through this interactive portfolio.
        Use the sidebar to navigate.
    """)
    st.image(get_image_path("home.jpg"), caption="My Portfolio Header", use_column_width=True) 

elif page == "Autobiography":
    st.title("Autobiography")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("About Me")
        st.write("""
            Hello! I'm Julianne Kristine D. Aban, and my journey in the world of technology has been nothing short of exciting. 
            From a young age, I was fascinated by how things work, which naturally led me to explore the realm of computing and technology. 
            My formal adventure began with studying Information Technology, where I delved into the intricacies of programming and system design.

            Throughout my academic career, I've been involved in a variety of projects that have allowed me to apply my skills in real-world scenarios. 
            Noteworthy among these are my projects like the Car Classifier AI, where I used computer vision to distinguish between car models, 
            and DeliverYey, a user-centric ordering system for food delivery that aimed to streamline the customer experience.

            I am passionate about leveraging technology to solve everyday problems and am always eager to learn and adapt to new challenges. 
            Looking ahead, I aspire to work in a role where I can combine my technical expertise with strategic thinking to drive impactful solutions. 
            Whether it's through developing cutting-edge applications or working on transformative projects, I am excited about the endless possibilities 
            in the tech industry.
        """)
    
    with col2:
        st.image(get_image_path("me.jpg"), caption="That's me!", use_column_width=True)

elif page == "Portfolio":
    st.title("My Portfolio")
    st.write("Here are some of the projects I've worked on.")

    projects = {
        "Car Classifier AI": "An AI model trained to classify different car models using computer vision techniques.",
        "DeliverYey: Ordering System Website": "A fully functional ordering system website designed for seamless food delivery.",
        "GreenSwap: Buy and Sell Application": "A platform for buying and selling second-hand items, promoting sustainability."
    }

    for project, description in projects.items():
        with st.expander(project):
            st.write(description)
            st.image(get_image_path(f"{project.lower().replace(' ', '_').replace(':', '').replace('-', '')}.jpg"), caption=project, use_column_width=True)

    st.write("You can find more of my work and contributions on my GitHub profile: [Julianne Aban on GitHub](https://github.com/julianneaban)")

elif page == "Media Gallery":
    st.title("Media Gallery")
    
    st.subheader("Video Presentation")
    st.video("https://youtu.be/bJzb-RuUcMU?si=XXLq2u-t4sYHDq3Q")

    st.subheader("Github Profile")
    st.write("[Julianne Aban on GitHub](https://github.com/julianneaban)")

    st.subheader("Project Images")
    st.image([
        get_image_path("car_classifier_ai.jpg"), 
        get_image_path("deliveryey_ordering_system_website.jpg"), 
        get_image_path("greenswap_buy_and_sell_application.jpg")
    ], caption=["Car Classifier AI", "DeliverYey: Ordering System Website", "GreenSwap: Buy and Sell Application"], use_column_width=True)

elif page == "Contact":
    st.title("Contact Me")
    st.write("I’d love to hear from you! Fill out the form below to get in touch.")

    st.markdown("""
        <style>
            .contact-form input, .contact-form textarea {
                width: 100%;
                padding: 10px;
                margin: 5px 0 15px 0;
                display: inline-block;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
            }

            .contact-form button {
                width: 100%;
                background-color: #ff69b4;
                color: white;
                padding: 14px 20px;
                margin: 8px 0;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }

            .contact-form button:hover {
                background-color: #ff85b8;
            }

            .contact-form {
                display: flex;
                flex-direction: column;
                max-width: 500px;
                margin: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    contact_form = """
    <form action="https://formsubmit.co/juliannekristineaban@gmail.com" method="POST" class="contact-form">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your Email" required>
         <textarea name="message" placeholder="Your Message" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
    
    st.write("Or connect with me on [LinkedIn](https://www.linkedin.com)")

st.sidebar.markdown("---")
st.sidebar.write("Developed by Julianne Kristine D. Aban")
