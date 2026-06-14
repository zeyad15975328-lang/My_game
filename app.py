import random
import streamlit as streamlit_app

# Modern clean ASCII art representations for the shapes
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

# Fixed and aligned Scissors art for a better appearance
scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

shape = [rock_art, paper_art, scissors_art]

# Streamlit UI Configuration
streamlit_app.set_page_config(page_title="Rock, Paper, Scissors", layout="centered")
streamlit_app.title("🪨 📄 ✂️ Rock, Paper, Scissors")

# Game Rules Section
with streamlit_app.expander("📚 Show Game Rules"):
    streamlit_app.markdown(
        """
    ********** RULES **********
    1. You choose and computer choose.
    2. Rock smash scissors -> Rock win.
    3. Scissor cut paper -> Scissors win.
    4. Paper cover Rock -> Paper win.
    """
    )

streamlit_app.subheader("Make Your Move")

# User Input
choice = streamlit_app.selectbox(
    "Choose Rock, Paper, or Scissors:", 
    ["Select...", "Rock", "Paper", "Scissors"], 
    index=0
)

if choice != "Select...":
    # Layout with side-by-side columns to display the choices clearly
    col1, col2 = streamlit_app.columns(2)

    with col1:
        streamlit_app.write("### Your Choice:")
        if choice == "Rock":
            streamlit_app.code(shape[0], language="text")
        elif choice == "Paper":
            streamlit_app.code(shape[1], language="text")
        elif choice == "Scissors":
            streamlit_app.code(shape[2], language="text")

    # Computer Choice Logic
    words_list = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(words_list).capitalize()

    with col2:
        streamlit_app.write("### Computer Choice:")
        if computer_choice == "Rock":
            streamlit_app.code(shape[0], language="text")
        elif computer_choice == "Paper":
            streamlit_app.code(shape[1], language="text")
        elif computer_choice == "Scissors":
            streamlit_app.code(shape[2], language="text")

    # Result Section
    streamlit_app.write("---")
    if computer_choice == choice:
        streamlit_app.info("🤝 It's a tie!")
    elif (
        (choice == "Scissors" and computer_choice == "Paper") or
        (choice == "Rock" and computer_choice == "Scissors") or
        (choice == "Paper" and computer_choice == "Rock")
    ):
        streamlit_app.success(f"🎉 Winner! {choice} beats {computer_choice}")
    else:
        streamlit_app.error(f"😢 Loser! {computer_choice} beats {choice}")
