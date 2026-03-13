import streamlit as st
import time

# 设置网页标题和布局
st.set_page_config(page_title="AI Email System Demo", layout="centered")

st.title("📧 AI Email Reply System - Live Demo")
st.markdown("### Automated Intent Recognition & Reply Generation")

# 输入区：对应 PPT 中的 Customer Email [cite: 46, 47]
email_text = st.text_area("📥 Paste Customer Email Here:", height=150, placeholder="Type your customer email here...")

# 点击按钮触发处理
if st.button("🚀 Process Email (Run AI Model)"):
    if email_text:
        # 制造一个很炫酷的“AI思考中”的加载动画
        with st.spinner("🧠 AI is analyzing intent and generating response..."):
            time.sleep(1.5)  # 故意停顿1.5秒，显得系统真的在调用大模型

            # 核心演示逻辑（通过关键词模拟 AI 分类）
            if "refund" in email_text.lower() or "money" in email_text.lower():
                intent = "Billing & Refund (退款与账单)"
                confidence = 92
                action = "✅ High Confidence: Auto-Send Reply"
                reply = "Dear Customer, we apologize for the inconvenience. We have processed your refund. It will appear on your statement in 3-5 business days."

            elif "broken" in email_text.lower() or "angry" in email_text.lower():
                intent = "Complex Issue / Complaint (复杂客诉)"
                confidence = 45
                action = "⚠️ Low Confidence: Route to Human Agent"
                reply = "[DRAFT ONLY - NEED HUMAN REVIEW] Dear Customer, I am so sorry to hear about your experience. I have escalated this to our senior support team..."

            else:
                intent = "General Inquiry (常规咨询)"
                confidence = 88
                action = "✅ High Confidence: Auto-Send Reply"
                reply = "Thank you for reaching out! We have received your inquiry and our team is looking into it."

        # 界面输出区：对应 PPT 中的系统决策 [cite: 54]
        st.success("✅ Processing Complete!")
        st.subheader("📊 AI Analysis Results")

        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**Identified Intent[cite: 50]:** {intent}")
        with col2:
            if confidence > 80:
                st.success(f"**Confidence Score:** {confidence}%")
            else:
                st.error(f"**Confidence Score:** {confidence}%")

        # 决策结果：自动发送还是转交人工 [cite: 55, 56, 57, 58]
        st.warning(f"**System Decision:** {action}")

        # 生成的回复 [cite: 52, 53]
        st.subheader("📝 Generated Reply (LLM Output)")
        st.text_area("Response", value=reply, height=100, label_visibility="collapsed")

    else:
        st.error("Please paste an email first!")