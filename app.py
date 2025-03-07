import streamlit as st
import time
from datetime import datetime
import pytz

local_tz = pytz.timezone('Asia/Kolkata')  # Replace with your local timezone
target_date = local_tz.localize(datetime(2025, 3, 8, 0, 0, 0))


# Get current time in local timezone
now = datetime.now(pytz.utc).astimezone(local_tz)
# st.write(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Function to calculate remaining time
def get_time_left():
    now = datetime.now(pytz.utc).astimezone(local_tz)
    remaining_time = target_date - now
    return remaining_time.total_seconds()

# Create a placeholder for the countdown
placeholder = st.empty()

# Countdown Loop
while get_time_left() > 0:
    remaining_time = get_time_left()
    days = int(remaining_time // 86400)
    hours = int((remaining_time % 86400) // 3600)
    minutes = int((remaining_time % 3600) // 60)
    seconds = int(remaining_time % 60)
    
    placeholder.subheader(f"⏳ {days} days, {hours} hours, {minutes} minutes, {seconds} seconds left!")
    time.sleep(1)

# Remove the countdown and display the birthday message
placeholder.empty()
st.balloons()
st.title("🎊 Happy Birthday Hema Sri! 🎂🥳")
st.image("image.png", caption="🎊 My Sweet Heart🎂🥳")
st.subheader("Wishing you lots of love, happiness, and success! ❤️")

# Initialize session state for the personal note button
if 'show_personal_note' not in st.session_state:
    st.session_state.show_personal_note = False

# Add a button for the personal note
if st.button("📜 Personal Note"):
    st.session_state.show_personal_note = not st.session_state.show_personal_note

# Display the personal note if the button was clicked
if st.session_state.show_personal_note:
    st.markdown("""
    <div style="border: 2px solid #f39c12; padding: 10px; border-radius: 10px; background-color: #f9e79f;">
        <h2 style="color: #d35400;">A Special Note for You</h2>
        <p style="color: #6c3483;">Dear Hema Sri,</p>
        <p style="color: #6c3483;">On this special day, I want to remind you how much you mean to me. Your presence brings joy and warmth to my life. May your birthday be filled with love, laughter, and unforgettable moments. Here's to many more wonderful years together!</p>
        <p style="color: #6c3483;">With all my love,</p>
        <p style="color: #6c3483;">Raayan</p>
    </div>
    """, unsafe_allow_html=True)

# Add confetti animation
st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/confetti-js@0.0.18/dist/index.min.js"></script>
    <script>
        var confettiSettings = { target: 'my-canvas' };
        var confetti = new ConfettiGenerator(confettiSettings);
        confetti.render();
    </script>
    <canvas id="my-canvas"></canvas>
""", unsafe_allow_html=True)
