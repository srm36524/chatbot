import streamlit as st

# Greet the user
st.title("Welcome to the Degree Program Selector!")
st.write("Please provide your details below.")

# Collect the user's name
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Nice to meet you.")

    # Ask the user to select a degree program
    program = st.selectbox("Select your degree program:", ["BA", "BCom", "BSc"])

    if program == "BA":
        st.write("You have selected **BA**.")
        subjects = st.multiselect("Select your subjects:", ["Economics", "History", "Political Science"])
        if subjects:
            st.write(f"You have selected the following subjects: {', '.join(subjects)}")
        st.write("**Eligibility:** Intermediate (any group)")

    elif program == "BCom":
        st.write("You have selected **BCom**.")
        specialization = st.selectbox("Select your specialization:", ["General", "Computer Applications"])
        st.write(f"You have selected **{specialization}** specialization.")
        st.write("**Eligibility:** Intermediate (any group)")

    elif program == "BSc":
        st.write("You have selected **BSc**.")
        subjects = st.multiselect("Select your subjects:", ["Chemistry", "Zoology", "Computer Science"])
        if subjects:
            st.write(f"You have selected the following subjects: {', '.join(subjects)}")
        st.write("**Eligibility:** Intermediate (Science group)")

    # Fee details
    if program:
        st.write("---")
        if st.button("Show Fee Details"):
            if program == "BA":
                st.write("**Fee for BA:** Rs 10,000")
            elif program == "BCom":
                st.write("**Fee for BCom:** Rs 15,000")
            elif program == "BSc":
                st.write("**Fee for BSc:** Rs 20,000")

    # Contact details
    st.write("---")
    st.write("**Contact Details:**")
    st.write("B Appa Rao")
    st.write("Phone: 99999999")
