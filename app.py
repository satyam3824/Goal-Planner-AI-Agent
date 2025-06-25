import streamlit as st
from agent import ask_agent
from memory import get_recent_memories

st.set_page_config(page_title="🌟 Goal Planner AI Agent", layout="centered")
st.title("🌟 Goal Planner AI Agent")
st.markdown("Plan your goals, set milestones, and get AI-generated guidance!")

user_input = st.text_area("Enter your goal or ask something related to goal setting:", height=150)

if st.button("Ask AI"):
    if user_input.strip() != "":
        with st.spinner("Thinking..."):
            try:
                response = ask_agent(user_input)
                st.success("Here's your plan:")
                st.write(response)

                # Show memory
                recent_memory = get_recent_memories()
                if recent_memory:
                    st.subheader("🧠 Recent Memory")
                    for i, mem in enumerate(recent_memory[::-1], 1):
                        st.markdown(f"**You:** {mem['user']}")
                        st.markdown(f"**AI:** {mem['ai']}")
                        st.markdown("---")
                else:
                    st.info("No previous memory yet.")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a question or goal.")

if st.button("🗑️ Clear Memory"):
    try:
        with open("memory.json", "w", encoding="utf-8") as f:
            f.write("[]")
        st.success("Memory cleared successfully!")
    except Exception as e:
        st.error(f"Could not clear memory: {e}")
