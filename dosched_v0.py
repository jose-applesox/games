import streamlit as st
import pandas as pd
import base64

LOGO_IMAGE = "WCL_official.png"

def get_game_list():
    excel_data_df = pd.read_excel('2022 games.xlsx')

    teams = [
        'BEL','BEN','COR','COW',
        'EDM','KAM','KEL','NAN',
        'PAL','POR','RID','SPR',
        'VIC','WEN','WWS','YAK'
    ]

    gl = []
    for _, row in excel_data_df.iterrows():
        date = row['Date'].date()
        for home in teams:
            road = row[home]
            if road in teams:
                # Check road team schedule
                if row[road] != '@'+home:
                    print("Data error", date, home, road)
                gl.append( (date,home,road) )
        
    return gl

def css_style():
    st.markdown(
        """
        <style>
        .container {
            display: flex;
            justify-content: start;
        }
        .logo-text {
            font-weight:700 !important;
            font-size:50px !important;
            color: #f9a01b !important;
            padding-top: 75px !important;
        }
        .logo-img {
            float:right;
            height: auto; 
            width: auto; 
            max-width: 100px; 
            max-height: 100px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def header() :
    st.markdown(
        f"""
        <div class="container">
            <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
            <p class="logo-text">&nbsp;&nbsp;2022 Schedule</p>
        </div>
        """,
    unsafe_allow_html=True
    )

def banner():
    return """
<div class="jumbotron">
  <h1 class="display-4">Hello, world!</h1>
  <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
  <hr class="my-4">
  <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
  <p class="lead">
    <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
  </p>
</div>    
    """

def card() :
    return """
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="card-link">Card link</a>
    <a href="#" class="card-link">Another link</a>
  </div>
</div>
    """

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 1rem;}
</style>

"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
css_style()

st.sidebar.write("")
st.sidebar.write("")
date = st.sidebar.date_input(
    "Showing games for"
)

c1, c2, _ = st.columns(3)
with c1:
    st.image(LOGO_IMAGE, width=200)
#_, c2, _ = st.columns(3)
with c2:
    s=date.strftime("%b %d")
    st.title(s)
st.markdown(card(), unsafe_allow_html =True)
