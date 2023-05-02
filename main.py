import streamlit as st
import pandas as pd

#st.set_page_config(layout = "wide")
p1_score = 0
p2_score = 0
p3_score = 0
p4_score = 0

with st. container():
    st.header("Input players' names in starting sequence")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        player1 = st.text_input("Player 1", value = "player 1")
    with col2:
        player2 = st.text_input("Player 2", value = "player 2")
    with col3:
        player3 = st.text_input("Player 3", value = "player 3")
    with col4:
        player4 = st.text_input("Player 4", value = "player 4")

players = [player1, player2, player3, player4]
p1_score = 0
p2_score = 0
p3_score = 0
p4_score = 0


with st.container():
    st.header("Round 1")
    st.text("Deal 13 cards starting from " + player1)
    st.text("Hearts trump against all other suits")
    st.text("players' estimate wins in below sequence, sum cannot be 13")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        p1r01e = st.number_input(player1, step = 1)
    with col2:
        p2r01e = st.number_input(player2, step = 1)
    with col3:
        p3r01e = st.number_input(player3, step = 1)
    with col4:
        p4r01e = st.number_input(player4, step = 1)
    invalid = 13-p1r01e-p2r01e-p3r01e
    if p1r01e + p2r01e + p3r01e + p4r01e == 13:
        st.error(player4 + " cannot estimate " + str(invalid)),
    else:
        st.success("OK!")

    st.text("players' actual wins")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        p1r01a = st.number_input(player1, step = 1, key = 1)
    with col2:
        p2r01a = st.number_input(player2, step = 1, key = 2)
    with col3:
        p3r01a = st.number_input(player3, step = 1, key = 3)
    with col4:
        p4r01a = st.number_input(player4, step = 1, key = 4)
        
    if p1r01a == p1r01e:
        p1_score = p1_score + p1r01a
    else:
        p1_score = p1_score - abs(p1r01a - p1r01e)
        
    if p2r01a == p2r01e:
        p2_score = p2_score + p2r01a
    else:
        p2_score = p2_score - abs(p2r01a - p2r01e)
        
    if p3r01a == p3r01e:
        p3_score = p3_score + p3r01a
    else:
        p3_score = p3_score - abs(p3r01a - p3r01e)

    if p3r01a == p3r01e:
        p3_score = p3_score + p3r01a
    else:
        p3_score = p3_score - abs(p3r01a - p3r01e)

    if p4r01a == p4r01e:
        p4_score = p4_score + p4r01a
    else:
        p4_score = p4_score - abs(p4r01a - p4r01e)
    df = pd.DataFrame()
    df[player1] = p1_score
    df[player2] = p2_score
    df[player3] = p3_score
    df[player4] = p4_score
    st.bar_chart(df)
