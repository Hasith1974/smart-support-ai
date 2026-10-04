import streamlit as st
from chatbot import get_response_stream
from langchain_core.messages import HumanMessage, AIMessage
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartSupport AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE
# ============================================================

if "conversations" not in st.session_state:
    st.session_state.conversations = {}


if "active_chat" not in st.session_state:
    chat_id = datetime.now().strftime("%Y%m%d%H%M%S%f")

    st.session_state.active_chat = chat_id

    st.session_state.conversations[chat_id] = {
        "title": "New Conversation",
        "messages": []
    }


if "quick_question" not in st.session_state:
    st.session_state.quick_question = None


# ============================================================
# CHAT FUNCTIONS
# ============================================================

def create_new_chat():
    """Create a new conversation."""

    chat_id = datetime.now().strftime("%Y%m%d%H%M%S%f")

    st.session_state.conversations[chat_id] = {
        "title": "New Conversation",
        "messages": []
    }

    st.session_state.active_chat = chat_id


def get_current_chat():
    """Return the currently active conversation."""

    return st.session_state.conversations[
        st.session_state.active_chat
    ]


def create_chat_title(question):
    """Create a short title from the first question."""

    title = question.strip()

    if len(title) > 32:
        title = title[:32] + "..."

    return title


# ============================================================
# CURRENT CHAT
# ============================================================

current_chat = get_current_chat()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🤖 SmartSupport AI")

    st.caption("AI-Powered Customer Support")

    st.divider()


    # --------------------------------------------------------
    # NEW CONVERSATION
    # --------------------------------------------------------

    if st.button(
        "➕ New Conversation",
        use_container_width=True
    ):

        create_new_chat()

        st.session_state.quick_question = None

        st.rerun()


    # --------------------------------------------------------
    # QUICK SUPPORT
    # --------------------------------------------------------

    st.subheader("💬 Quick Support")


    if st.button(
        "🛒 Order Support",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "I need help with my order."
        )


    if st.button(
        "📦 Shipping",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "I need help with shipping and delivery."
        )


    if st.button(
        "💳 Payment",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "I need help with a payment."
        )


    if st.button(
        "↩️ Refund",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "I want to know about the refund process."
        )


    if st.button(
        "👨‍💻 General Support",
        use_container_width=True
    ):

        st.session_state.quick_question = (
            "I need general customer support."
        )


    st.divider()


    # --------------------------------------------------------
    # CONVERSATIONS
    # --------------------------------------------------------

    st.subheader("💬 Your Conversations")


    chat_items = list(
        st.session_state.conversations.items()
    )[::-1]


    for chat_id, chat in chat_items:

        title = chat["title"]


        if chat_id == st.session_state.active_chat:

            button_text = f"🟣 {title}"

        else:

            button_text = f"💬 {title}"


        if st.button(
            button_text,
            key=f"chat_{chat_id}",
            use_container_width=True
        ):

            st.session_state.active_chat = chat_id

            st.session_state.quick_question = None

            st.rerun()


    st.divider()


    # --------------------------------------------------------
    # CLEAR CONVERSATIONS
    # --------------------------------------------------------

    if st.button(
        "🗑️ Clear All Conversations",
        use_container_width=True
    ):

        st.session_state.conversations = {}

        create_new_chat()

        st.session_state.quick_question = None

        st.rerun()


    st.divider()


    st.caption("POWERED BY")

    st.write("⚡ Gemini")

    st.write("🔗 LangChain")

    st.write("🎈 Streamlit")


# ============================================================
# MAIN HEADER
# ============================================================

col1, col2, col3 = st.columns([1, 8, 2])


with col1:

    st.markdown("# 🤖")


with col2:

    st.title("SmartSupport AI")

    st.caption(
        "Your intelligent customer support assistant"
    )


with col3:

    st.success("● Online")


st.divider()


# ============================================================
# WELCOME SCREEN
# ============================================================

if not current_chat["messages"]:

    st.markdown("# Hello! 👋")

    st.markdown(
        """
        ### Welcome to SmartSupport AI

        I'm your AI-powered customer support assistant.

        You can ask me about:

        - 🛒 **Orders**
        - 📦 **Shipping**
        - 💳 **Payments**
        - ↩️ **Refunds**
        - 👨‍💻 **General Support**
        """
    )

    st.divider()

    st.subheader("How can I help you?")


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        with st.container(border=True):

            st.markdown("## 🛒")

            st.markdown("### Orders")

            st.caption(
                "Get help with your orders"
            )


    with col2:

        with st.container(border=True):

            st.markdown("## 📦")

            st.markdown("### Shipping")

            st.caption(
                "Track shipping and delivery"
            )


    with col3:

        with st.container(border=True):

            st.markdown("## 💳")

            st.markdown("### Payments")

            st.caption(
                "Get help with payments"
            )


    with col4:

        with st.container(border=True):

            st.markdown("## ↩️")

            st.markdown("### Refunds")

            st.caption(
                "Learn about refund requests"
            )


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in current_chat["messages"]:

    if isinstance(message, HumanMessage):

        with st.chat_message(
            "user",
            avatar="👤"
        ):

            st.markdown(message.content)


    elif isinstance(message, AIMessage):

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            st.markdown(message.content)


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "💬 Ask SmartSupport AI anything..."
)


# ============================================================
# QUICK QUESTION HANDLER
# ============================================================

if question is None and st.session_state.quick_question:

    question = st.session_state.quick_question

    st.session_state.quick_question = None


# ============================================================
# PROCESS USER QUESTION
# ============================================================

if question:

    # --------------------------------------------------------
    # ADD USER MESSAGE
    # --------------------------------------------------------

    current_chat["messages"].append(
        HumanMessage(content=question)
    )


    # --------------------------------------------------------
    # CREATE TITLE FOR NEW CHAT
    # --------------------------------------------------------

    if current_chat["title"] == "New Conversation":

        current_chat["title"] = create_chat_title(
            question
        )


    # --------------------------------------------------------
    # SHOW USER MESSAGE
    # --------------------------------------------------------

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.markdown(question)


    # --------------------------------------------------------
    # AI RESPONSE
    # --------------------------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        response_placeholder = st.empty()

        full_response = ""


        try:

            # Stream the response token-by-token
            for chunk in get_response_stream(
                question,
                current_chat["messages"][:-1]
            ):

                full_response += chunk

                response_placeholder.markdown(
                    full_response + "▌"
                )


            # Remove cursor after generation
            response_placeholder.markdown(
                full_response
            )


            response = full_response


        except Exception as error:

            response = (
                "Sorry, I couldn't process your "
                "request right now. Please try again."
            )

            st.error(response)

            # Uncomment while debugging if needed:
            # st.exception(error)


    # --------------------------------------------------------
    # SAVE AI RESPONSE
    # --------------------------------------------------------

    current_chat["messages"].append(
        AIMessage(content=response)
    )


    # --------------------------------------------------------
    # REFRESH UI
    # --------------------------------------------------------

    st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "SmartSupport AI • Powered by Gemini + LangChain"
)