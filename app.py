#import statements
import streamlit as st
import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def main():
    lottie_hello = load_lottieurl("https://lottie.host/052653a2-761d-49c0-8447-fea767592952/NrhCF0XZyW.json")

    st.title("Phishing Domain and Malicious URL Detection")
    st_lottie(lottie_hello)


if __name__=="__main__":
    main()