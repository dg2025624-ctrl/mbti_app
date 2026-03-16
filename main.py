import streamlit as st

st.set_page_config(page_title="MBTI 스포츠 팀 추천", page_icon="🏆")

st.title("🏆 MBTI 스포츠 팀 추천 앱")
st.write("당신의 MBTI를 선택하면 어울리는 스포츠 팀을 추천해드립니다! ⚽🏀⚾")

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
"INTJ": "🏀 LA 레이커스 – 전략적인 플레이를 좋아하는 당신!",
"INTP": "⚽ 맨체스터 시티 – 분석적인 축구 스타일!",
"ENTJ": "🏈 뉴잉글랜드 패트리어츠 – 리더십과 승부욕!",
"ENTP": "⚽ 바르셀로나 – 창의적인 공격 축구!",

"INFJ": "⚽ 리버풀 – 열정과 팀워크!",
"INFP": "⚽ 아스널 – 감성적이면서 아름다운 축구!",
"ENFJ": "🏀 골든스테이트 워리어스 – 팀 플레이의 정석!",
"ENFP": "⚽ 토트넘 – 에너지 넘치는 공격!",

"ISTJ": "⚾ 뉴욕 양키스 – 전통과 안정적인 강팀!",
"ISFJ": "⚾ LA 다저스 – 꾸준함과 팀워크!",
"ESTJ": "🏈 캔자스시티 치프스 – 강력한 리더십!",
"ESFJ": "⚽ 레알 마드리드 – 팀 중심의 플레이!",

"ISTP": "🏎️ 레드불 레이싱 – 침착한 기술형!",
"ISFP": "⚽ AC 밀란 – 감각적인 플레이!",
"ESTP": "🏀 시카고 불스 – 강렬하고 빠른 플레이!",
"ESFP": "⚽ PSG – 화려하고 재미있는 경기!"
}

if st.button("🔥 추천 받기"):
    st.balloons()
    st.success(f"당신에게 추천하는 팀은!\n\n{teams[mbti]} 🎉")

st.divider()

st.caption("💡 MBTI 성향과 스포츠 팀 스타일을 재미로 매칭한 앱입니다!")
