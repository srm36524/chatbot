import streamlit as st

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Greet the user
st.title("Degree Program Selector Chatbot")
st.write("Welcome! I'm here to help you choose a degree program.")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Collect the user's name
if "name" not in st.session_state:
    user_input = st.chat_input("Enter your name:")
    if user_input:
        st.session_state.name = user_input
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("assistant"):
            st.write(f"Hello, {user_input}! Nice to meet you.")
            st.session_state.messages.append({"role": "assistant", "content": f"Hello, {user_input}! Nice to meet you."})
        st.rerun()

# If name is collected, proceed to degree selection
if "name" in st.session_state:
    if "program" not in st.session_state:
        user_input = st.chat_input("Select your degree program (BA, BCom, BSc):")
        if user_input and user_input.upper() in ["BA", "BCOM", "BSC"]:
            st.session_state.program = user_input.upper()
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("assistant"):
                st.write(f"You have selected **{st.session_state.program}**.")
                if st.session_state.program == "BA":
                    st.write("Please select your subjects: Economics, History, Political Science.")
                elif st.session_state.program == "BCom":
                    st.write("Please select your specialization: General, Computer Applications.")
                elif st.session_state.program == "BSc":
                    st.write("Please select your subjects: Chemistry, Zoology, Computer Science.")
                st.session_state.messages.append({"role": "assistant", "content": f"You have selected **{st.session_state.program}**."})
            st.rerun()

    # Handle subject/specialization selection
    if "program" in st.session_state and "subjects" not in st.session_state:
        if st.session_state.program == "BA":
            user_input = st.chat_input("Select your subjects (Economics, History, Political Science):")
            if user_input:
                st.session_state.subjects = [s.strip() for s in user_input.split(",")]
                st.session_state.messages.append({"role": "user", "content": user_input})
                with st.chat_message("assistant"):
                    st.write(f"You have selected: {', '.join(st.session_state.subjects)}")
                    st.write("**Eligibility:** Intermediate (any group)")
                    st.session_state.messages.append({"role": "assistant", "content": f"You have selected: {', '.join(st.session_state.subjects)}"})
                st.rerun()
        elif st.session_state.program == "BCom":
            user_input = st.chat_input("Select your specialization (General, Computer Applications):")
            if user_input:
                st.session_state.subjects = [user_input.strip()]
                st.session_state.messages.append({"role": "user", "content": user_input})
                with st.chat_message("assistant"):
                    st.write(f"You have selected: {st.session_state.subjects[0]}")
                    st.write("**Eligibility:** Intermediate (any group)")
                    st.session_state.messages.append({"role": "assistant", "content": f"You have selected: {st.session_state.subjects[0]}"})
                st.rerun()
        elif st.session_state.program == "BSc":
            user_input = st.chat_input("Select your subjects (Chemistry, Zoology, Computer Science):")
            if user_input:
                st.session_state.subjects = [s.strip() for s in user_input.split(",")]
                st.session_state.messages.append({"role": "user", "content": user_input})
                with st.chat_message("assistant"):
                    st.write(f"You have selected: {', '.join(st.session_state.subjects)}")
                    st.write("**Eligibility:** Intermediate (Science group)")
                    st.session_state.messages.append({"role": "assistant", "content": f"You have selected: {', '.join(st.session_state.subjects)}"})
                st.rerun()

    # Show fee details
    if "subjects" in st.session_state and "fee_shown" not in st.session_state:
        with st.chat_message("assistant"):
            if st.session_state.program == "BA":
                st.write("**Fee for BA:** Rs 10,000")
            elif st.session_state.program == "BCom":
                st.write("**Fee for BCom:** Rs 15,000")
            elif st.session_state.program == "BSc":
                st.write("**Fee for BSc:** Rs 20,000")
            st.write("**Contact Details:**")
            st.write("B Appa Rao")
            st.write("Phone: 99999999")
            st.session_state.messages.append({"role": "assistant", "content": "Fee and contact details displayed."})
            st.session_state.fee_shown = True
