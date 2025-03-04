import streamlit as st  

# Set the title and description  
st.title("🎉 Python Mad Lib Game By Muhammad Ashhad Khan 🎉")  
st.markdown(  
    """  
    Welcome to the Python Mad Lib Game! Fill in the details below to create your own story.   
    This is a fun way to learn programming and improve your language skills!  
    """  
)  

# Sidebar for user inputs  
st.sidebar.header("Input Details")  
name = st.sidebar.text_input("Enter your name:")  
programming_language = st.sidebar.text_input("Enter your programming language:")  
mentor = st.sidebar.text_input("Enter your mentor:")  
house = st.sidebar.text_input("Enter your House (e.g., Governor House or PIAIC House):")  

# Button to generate the story  
if st.sidebar.button("Generate Story"):  
    if name and programming_language and mentor and house:  
        # Display the generated story  
        st.header("📖 Here's Your Story: ")  
        st.markdown(  
            f"""  
            **Once upon a time**, {name} found out that IT initiatives were being tested at the **{house}**.  
            So, **{name}** enrolled himself and successfully passed the test. 
           {name} has also passed the tests of Quarter 1 and Quarter 2 with good marks. 
            Now **{name}** is also learning a **{programming_language}**, and **{mentor}** is teaching him.  
            The faculty there is also very good!  
            """  
        )  
    else:  
        st.warning("Please fill in all the fields!")  

# Footer  
st.markdown("---")  
st.markdown("©️ by Muhammad Ashhad Khan ")  