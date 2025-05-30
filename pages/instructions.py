import streamlit as st

st.set_page_config(page_title="Instructions", page_icon="📖")

st.title("📖 How to Play Tamagotchi")

st.markdown(
    """
Welcome to **Tamagotchi for Streamlit**!

This is a virtual pet you must take care of. You can:

- 🍽️ Feed your pet (lowers hunger)
- 🎮 Play (lowers boredom)
- 🛁 Bathe it (cleans dirtiness)
- 😴 Put it to sleep (rest to reduce tiredness)
- 🍖 Search for food (find meals)

Be careful! If any parameter (hunger, boredom, dirtiness, tiredness) reaches **10**, your pet will **die**.

---

### 🎮 Game Mechanics

- You can interact by clicking buttons below the message screen.
- If your pet is asleep, only the **Wake Up** button will be available. It may take more than one click to wake your pet up!
- When you play, you'll face your pet in a game of **rock-paper-scissors**.

---

### 👨‍💻 About the Project

This game was created as a fun way to practice **Object-Oriented Programming (OOP)** in Python and web development with **Streamlit**.

Author: [Álvaro Mejía](https://alvarodsci.wixsite.com/alvaro-mejia)

GitHub: [mgalvaro/tamagotchi](https://github.com/mgalvaro/tamagotchi)

---
"""
)
