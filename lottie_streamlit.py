import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    lottie_hello = r.json()
    st_lottie(lottie_hello)
