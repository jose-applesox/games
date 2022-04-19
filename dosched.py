import streamlit as st
import pandas as pd
import base64

LOGO_IMAGE = "WCL_official.png"

@st.cache
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


def games_from_gl(gl, d):
    games = []
    for g in gl:
        day, home, road = g
        if day == date:
            games.append((home,road))
    return games

def card(home,road) :
    return f"""
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">{road+' @ '+home}</h5>
    <a href="https://web.playsight.com/facility/wenatchee-applesox/home" class="card-link">Video Stream</a>
</div>
    """

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 1rem;}
</style>

"""

gl = get_game_list()

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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

games = games_from_gl(gl, date)
if games:
    cols = st.columns(4)
    idx = 0
    for g in games:
        home, road = g
        cols[idx].markdown(card(home,road), unsafe_allow_html =True)
        cols[idx].write("")
        cols[idx].write("")
        idx+=1
        if idx == 4:
            idx = 0
else:
    s=date.strftime("%b %d")
    st.subheader("No games Scheduled for " + s)
