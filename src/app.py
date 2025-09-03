import requests
import streamlit as st
import time
import src.api.crew.utils as utils

st.title("Netflex Customer Support Chatbot")

# Sidebar
st.sidebar.header("Customer Info")

if "customer" not in st.session_state:
    st.session_state.customer = {}

with st.sidebar.form("customer_form", clear_on_submit=False):
    first_last_name = st.text_input("First Last Name", placeholder="Khalid Ali")
    username = st.text_input("Username", placeholder="unique pre customer, e.g. khalid.ali")
    subscription_plan = st.selectbox("Subscription Plan", ["No Plan", "Basic", "Standard", "Premium"])

    submitted = st.form_submit_button("Save Customer")
    if submitted:
        st.session_state.customer = {
            "name": first_last_name,
            "username": username,
            "subscription_plan": subscription_plan,
        }
        utils.add_or_update_subscription(
            customer_id=username,
            subscription_plan=subscription_plan
        )
        st.sidebar.success("Data saved!")

if st.sidebar.button("🔄 Refresh"):
    st.rerun()

if st.session_state.customer:
    st.sidebar.warning(f"Your current subscription plan is: {utils.get_subscription(st.session_state.customer.get('username'))}")

# Main Chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show past messages
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

customer_ready = bool(st.session_state.customer.get("username")) and bool(st.session_state.customer.get("name"))

def convert_chat_history(history_tuples):
    return [{"role": role, "content": msg} for role, msg in history_tuples]

if not customer_ready:
    st.error("Please save your customer info in the sidebar before chatting.")
    st.chat_input("Type your message...", disabled=True)

else:

    # Chat input
    if user_input := st.chat_input("Type your message..."):
        # Store user message
        st.session_state.chat_history.append(("user", user_input))
        with st.chat_message("user"):
            st.markdown(user_input)

        chat_request = {
            "customer_id": st.session_state.customer.get('username'),
            "customer_name": st.session_state.customer.get('name'),
            "customer_question": user_input
        }
        
        try:
            response = requests.post("http://localhost:5000/api/v1/crew/chat", json=chat_request)
            response.raise_for_status()
            support_reply = response.json().get("response", "Sorry, I didn't get that. may be its a problem in the backend, please try again.")

        except Exception as e:
            support_reply = "Sorry, there was an error in the backend. Please try again."
            st.error(f"Error: {e}")
            
        def stream_reply():
            for chunk in support_reply.split(" "):
                yield chunk + " "
                time.sleep(0.05)

        st.session_state.chat_history.append(("assistant", support_reply))
        with st.chat_message("assistant"):
            st.write_stream(stream_reply)
