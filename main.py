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
"INTJ": {
"name":"LA 레이커스 🏀",
"desc":"전략적이고 계산적인 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/commons/3/3c/Los_Angeles_Lakers_logo.svg"
},

"INTP": {
"name":"맨체스터 시티 ⚽",
"desc":"분석적이고 전술적인 팀!",
"logo":"https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg"
},

"ENTJ": {
"name":"뉴잉글랜드 패트리어츠 🏈",
"desc":"강한 리더십과 승리 집착!",
"logo":"https://upload.wikimedia.org/wikipedia/en/b/b9/New_England_Patriots_logo.svg"
},

"ENTP": {
"name":"FC 바르셀로나 ⚽",
"desc":"창의적인 공격 축구!",
"logo":"https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg"
},

"INFJ": {
"name":"리버풀 FC ⚽",
"desc":"열정과 팀워크의 상징!",
"logo":"https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg"
},

"INFP": {
"name":"아스널 FC ⚽",
"desc":"아름다운 패스 축구!",
"logo":"https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg"
},

"ENFJ": {
"name":"골든스테이트 워리어스 🏀",
"desc":"완벽한 팀 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/en/0/01/Golden_State_Warriors_logo.svg"
},

"ENFP": {
"name":"토트넘 홋스퍼 ⚽",
"desc":"에너지 넘치는 공격!",
"logo":"https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg"
},

"ISTJ": {
"name":"뉴욕 양키스 ⚾",
"desc":"전통과 안정감!",
"logo":"https://upload.wikimedia.org/wikipedia/en/2/25/NewYorkYankees_PrimaryLogo.svg"
},

"ISFJ": {
"name":"LA 다저스 ⚾",
"desc":"꾸준하고 믿음직한 팀!",
"logo":"https://upload.wikimedia.org/wikipedia/en/6/69/Los_Angeles_Dodgers_logo.svg"
},

"ESTJ": {
"name":"캔자스시티 치프스 🏈",
"desc":"강력한 리더십!",
"logo":"https://upload.wikimedia.org/wikipedia/en/e/e1/Kansas_City_Chiefs_logo.svg"
},

"ESFJ": {
"name":"레알 마드리드 ⚽",
"desc":"팀워크 중심 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg"
},

"ISTP": {
"name":"레드불 레이싱 🏎️",
"desc":"차분한 기술형 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/en/f/fc/Red_Bull_Racing_logo.svg"
},

"ISFP": {
"name":"AC 밀란 ⚽",
"desc":"감각적인 플레이!",
"logo":"https://upload.wikimedia.org/wikipedia/commons/d/d0/Logo_of_AC_Milan.svg"
},

"ESTP": {
"name":"시카고 불스 🏀",
"desc":"강렬하고 폭발적인 경기!",
"logo":"https://upload.wikimedia.org/wikipedia/en/6/67/Chicago_Bulls_logo.svg"
},

"ESFP": {
"name":"PSG ⚽",
"desc":"화려하고 즐거운 축구!",
"logo":"https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg"
}
}

if st.button("🔥 팀 추천 받기"):
    team = teams[mbti]

    st.balloons()

    st.subheader(f"🎉 추천 팀: {team['name']}")
    st.write(team["desc"])

    st.image(team["logo"], width=200)

st.divider()
st.caption("💡 MBTI 성향을 기반으로 재미있게 매칭한 스포츠 팀 추천 앱입니다!")
