import streamlit as st
import random
import time
from ai_service import analyze_sentiment

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="เซียมซี: ฮีลใจสายมู", page_icon="🔮", layout="centered")

# ตกแต่ง CSS ธีมดวงดาว สายมู ดาร์กโมดลึกลับ
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #1a102f 50%, #0f172a 100%);
        color: #f3f4f6;
    }
    h1 {
        color: #e2e8f0;
        font-family: 'Prompt', sans-serif;
        text-shadow: 0 0 10px rgba(168, 85, 247, 0.5);
    }
    .stButton>button {
        background: linear-gradient(90deg, #9333ea 0%, #4f46e5 100%);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        width: 100%;
        border: none;
        padding: 0.75rem;
        box-shadow: 0 4px 15px rgba(147, 51, 234, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #a855f7 0%, #6366f1 100%);
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.6);
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# หัวข้อหลัก
st.title("🔮 เซียมซี: ฮีลใจสายมู")
st.markdown("##### *✨ ตั้งจิตอธิษฐาน พิมพ์ระบายความในใจ แล้วเขย่ากระบอกเซียมซีรับคำทำนายแห่งดวงดาว*")

st.markdown("---")

# ช่องกรอกข้อความ
user_input = st.text_input("💬 พิมพ์เรื่องที่คุณกำลังเครียดหรือกังวลตอนนี้:", placeholder="เช่น ปั่นโปรเจกต์กลุ่มไม่ไหวแล้ว, คิดถึงแมว, ชีวิตช่วงนี้เหนื่อยจัง...")

st.markdown("<br>", unsafe_allow_html=True)

# รายการใบเซียมซีสำรอง (กรณีสุ่ม)
fortune_list = [
    "“ช่วงนี้ดวงงานรุมเร้า ทำโปรเจกต์กลุ่มจนตาแตก แนะนำให้สูดหายใจเข้าลึกๆ มองดูดวงดาวแล้วบอกตัวเองว่า 'เดี๋ยวทุกอย่างก็ผ่านพ้นไปได้ด้วยดี' ลุยต่ออีกนิด ชัยชนะรออยู่!”",
    "“สิ่งที่คุณกังวลอยู่ ภายใต้แสงดาวแห่งจักรวาลบอกว่ามันจะคลี่คลายในไม่ช้า หาชานมไข่มุกกินแล้วนอนหลับให้เต็มอิ่ม พรุ่งนี้ค่อยลุยใหม่!”",
    "“ดวงชะตาบอกว่าช่วงนี้เหนื่อยหน่อยนะ แต่ความพยายามจะไม่สูญเปล่า ระวังเรื่องสุขภาพ พักผ่อนบ้าง แล้วทุกอย่างจะราบรื่นเกินคาด!”",
    "“โอ๋ๆ นะคะคนเก่ง ช่วงนี้ดาวมฤตยูโคจรเข้าใกล้ความเครียด แนะนำให้ป้ายยาตัวเองด้วยการดูแมวหรือหาของอร่อยกิน แล้วพลังใจจะกลับมาเต็มเปี่ยม!”"
]

# ปุ่มกดเขย่าเซียมซี
if st.button("🪩 เริ่มเขย่ากระบอกเซียมซี..."):
    if user_input:
        # เอฟเฟกต์จำลองการเขย่ากระบอกเซียมซี
        shake_placeholder = st.empty()
        
        shake_animations = [
            "🔮 *(กำลังตั้งสมาธิ...)* 🥢",
            "📿 *กริ๊งๆ... เขย่าแรงๆ เรียกพลังจักรวาล!* 🌌",
            "✨ *ใกล้แล้วๆ ไม้เซียมซีใกล้จะร่วงลงมาแล้ว!* 🎋",
            "🔮 *อุ๊ย! ไม้เซียมซีหล่นออกมา 1 ไม้แล้ว!* 👇"
        ]
        
        for anim in shake_animations:
            shake_placeholder.markdown(f"<h3 style='text-align: center; color: #c084fc;'>{anim}</h3>", unsafe_allow_html=True)
            time.sleep(0.5)
            
        with st.spinner("ดาวเคราะห์กำลังโคจรเชื่อมโยงกับ AIForThai..."):
            # เรียกใช้ฟังก์ชันยิง API จริง
            api_result = analyze_sentiment(user_input)
            
        shake_placeholder.empty()
        st.success("🌟 ติ๊ง! เปิดใบเซียมซีแห่งโชคชะตาสำเร็จแล้ว!")
        
        # แสดงผลลัพธ์แบบแบ่ง 2 คอลัมน์
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📜 คำทำนายจากเซียมซีดวงดาว")
            # สุ่มใบเซียมซีไม่ให้ซ้ำซากจำเจ
            selected_fortune = random.choice(fortune_list)
            st.info(selected_fortune)
            
            with st.expander("🔍 ดูผลวิเคราะห์พลังงาน AI"):
                st.json(api_result)
            
        with col2:
            st.markdown("### 🖼️ มีมพลังจักรวาลฮีลใจ")
            memes = [
                "https://media.giphy.com/media/3o7TKSjRrfIPjeiOkM/giphy.gif",
                "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",
                "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"
            ]
            st.image(random.choice(memes), use_container_width=True)
            
    else:
        st.warning("⚠️ โปรดพิมพ์เรื่องในใจลงในช่องว่างก่อนเขย่ากระบอกเซียมซีนะจ๊ะ!")