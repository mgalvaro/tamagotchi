import streamlit as st
from tamagotchi import Tamagotchi
from config import PAGE_CONFIG
from functions import *


def main():

    st.set_page_config(**PAGE_CONFIG)

    st.title("🐾 Tamagotchi Game")


if __name__ == "__main__":
    main()
