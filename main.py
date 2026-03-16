import streamlit as st

st.set_page_config(page_title="MBTI 스포츠 팀 추천", page_icon="🏆")

st.title("🏆 MBTI 스포츠 팀 추천")
st.write("MBTI를 선택하면 어울리는 스포츠 팀을 추천해드립니다! ⚽🏀⚾")

mbti = st.selectbox(
    "🧠 MBTI를 선택하세요",
    [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
)

teams = {

"INTJ":{
"name":"LA 레이커스 🏀",
"desc":"전략적이고 계산적인 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/commons/3/3c/Los_Angeles_Lakers_logo.png"
},

"INTP":{
"name":"맨체스터 시티 ⚽",
"desc":"분석적인 전술 축구!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/Manchester_City_FC_badge.svg/300px-Manchester_City_FC_badge.svg.png"
},

"ENTJ":{
"name":"뉴잉글랜드 패트리어츠 🏈",
"desc":"강한 리더십과 승부욕!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/New_England_Patriots_logo.svg/300px-New_England_Patriots_logo.svg.png"
},

"ENTP":{
"name":"FC 바르셀로나 ⚽",
"desc":"창의적인 공격 축구!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/4/47/FC_Barcelona_%28crest%29.svg/300px-FC_Barcelona_%28crest%29.svg.png"
},

"INFJ":{
"name":"리버풀 ⚽",
"desc":"열정과 팀워크!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Liverpool_FC.svg/300px-Liverpool_FC.svg.png"
},

"INFP":{
"name":"아스널 ⚽",
"desc":"아름다운 패스 축구!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Arsenal_FC.svg/300px-Arsenal_FC.svg.png"
},

"ENFJ":{
"name":"골든스테이트 워리어스 🏀",
"desc":"완벽한 팀 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/0/01/Golden_State_Warriors_logo.svg/300px-Golden_State_Warriors_logo.svg.png"
},

"ENFP":{
"name":"토트넘 홋스퍼 ⚽",
"desc":"에너지 넘치는 공격!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/Tottenham_Hotspur.svg/300px-Tottenham_Hotspur.svg.png"
},

"ISTJ":{
"name":"뉴욕 양키스 ⚾",
"desc":"전통과 안정적인 강팀!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/2/25/NewYorkYankees_PrimaryLogo.svg/300px-NewYorkYankees_PrimaryLogo.svg.png"
},

"ISFJ":{
"name":"LA 다저스 ⚾",
"desc":"꾸준하고 믿음직한 팀!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Los_Angeles_Dodgers_logo.svg/300px-Los_Angeles_Dodgers_logo.svg.png"
},

"ESTJ":{
"name":"캔자스시티 치프스 🏈",
"desc":"강력한 리더십!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Kansas_City_Chiefs_logo.svg/300px-Kansas_City_Chiefs_logo.svg.png"
},

"ESFJ":{
"name":"레알 마드리드 ⚽",
"desc":"팀워크 중심 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/300px-Real_Madrid_CF.svg.png"
},

"ISTP":{
"name":"레드불 레이싱 🏎️",
"desc":"침착하고 기술적인 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Red_Bull_Racing_logo.svg/512px-Red_Bull_Racing_logo.svg.png"
},

"ISFP":{
"name":"AC 밀란 ⚽",
"desc":"감각적인 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Logo_of_AC_Milan.svg/300px-Logo_of_AC_Milan.svg.png"
},

"ESTP":{
"name":"시카고 불스 🏀",
"desc":"폭발적인 경기 스타일!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Chicago_Bulls_logo.svg/300px-Chicago_Bulls_logo.svg.png"
},

"ESFP":{
"name":"PSG ⚽",
"desc":"화려한 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/en/thumb/a/a7/Paris_Saint-Germain_F.C..svg/300px-Paris_Saint-Germain_F.C..svg.png"
}

}

if st.button("🔥 팀 추천 받기"):

    team = teams[mbti]

    st.balloons()

    st.subheader(f"🎉 추천 팀: {team['name']}")
    st.write(team["desc"])
    st.image(team["logo"], width=220)

st.divider()
st.caption("💡 MBTI 성향을 기반으로 재미있게 매칭한 스포츠 팀 추천 앱입니다!")
