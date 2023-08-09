# import statements
import streamlit as st
from lottie_streamlit import load_lottieurl
from prediction import predictor


def main():
    st.header("Phishing Domain and Malicious URL Detection")
    load_lottieurl(
        "https://lottie.host/052653a2-761d-49c0-8447-fea767592952/NrhCF0XZyW.json"
    )

    url = st.text_input("Enter URL Here", "https://www.example.com/")

    if st.button("Detect!"):
        result = predictor(url)
        if result == 0:
            st.subheader("This URL seems to be safe!😼")
            st.subheader("You are Good to go 👍🏻")
            load_lottieurl(
                "https://lottie.host/e4735726-9f74-4286-9ee9-c393e912cc77/47OtrlTYLi.json"
            )
        else:
            st.subheader("This URL seems to be malicious!👎")
            load_lottieurl(
                "https://lottie.host/8ae43c45-0511-4beb-84de-e3e075a7ef0d/Xu8r4ZE9no.json"
            )


if __name__ == "__main__":
    main()
