import streamlit as st
import hashlib
import time

# 1. 页面配置
st.set_page_config(page_title="性格城市匹配测试", page_icon="📍", layout="centered")

# 2. CSS 重构：调大标题字号并优化排版
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; color: #31333F !important; }
    
    /* 核心优化：超大渐变标题 */
    .hero-title {
        font-size: 3.5rem; /* 从 2.8 调大到 3.5 */
        font-weight: 900;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #00C1D4, #4AA9FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 40px;
        margin-bottom: 5px;
        line-height: 1.1; /* 收紧行高，更有视觉张力 */
        letter-spacing: -2px; /* 紧凑排版 */
    }

    .icon-container {
        display: flex;
        justify-content: center;
        margin: 30px 0;
    }
    .location-card {
        width: 130px;
        height: 130px;
        background: linear-gradient(135deg, #7DE2FC 0%, #B9EDF8 100%);
        border-radius: 35px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 20px 40px rgba(0, 193, 212, 0.2);
    }

    .intro-section {
        text-align: center;
        padding: 0 10px;
        color: #555555;
        line-height: 1.8;
        font-size: 1.1rem;
    }
    .intro-highlight {
        color: #1E1E1E;
        font-weight: 700;
        border-bottom: 3px solid #00C1D4;
    }

    .stSelectbox label, .stMultiSelect label {
        font-size: 1.2rem !important;
        font-weight: 800 !important;
        color: #1E1E1E !important;
        padding-top: 20px;
    }
    
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 状态管理
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'form_version' not in st.session_state:
    st.session_state.form_version = 0

def hard_reset_test():
    st.session_state.form_version += 1

def main():
    if st.session_state.page == 'home':
        # 应用超大渐变标题
        st.markdown('<p class="hero-title">你的性格与哪个城市<br>是天选CP</p>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="icon-container">
            <div class="location-card">
                <span style="font-size: 70px;">📍</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="intro-section">
            城市是钢筋水泥的森林，也是安放内心的容器。<br>
            有人生来属于上海的霓虹，有人注定流浪在 <span class="intro-highlight">大理的云边</span>。<br><br>
            解锁你的「地理人格」，通过深度潜意识演算，<br>
            找到那个懂你悲欢、与你灵魂同鸣的 <span class="intro-highlight">天选之地</span>。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            if st.button("✨ 开启我的地理人格测算", use_container_width=True):
                st.session_state.page = 'test'
                st.rerun()

    elif st.session_state.page == 'test':
        v = st.session_state.form_version
        st.markdown("<h2 style='text-align: center; color: #1E1E1E; font-weight:900;'>📍 录入您的灵魂坐标</h2>", unsafe_allow_html=True)
        st.write("---")

        # --- 题目部分 (保持原有逻辑) ---
        col1, col2 = st.columns(2)
        with col1:
            gender = st.selectbox("1. 您的性别", ["请选择...", "男生", "女生", "保密"], key=f"gender_{v}")
        with col2:
            status = st.selectbox("2. 目前的生活阶段", ["请选择...", "学生党", "职场新锐", "自由职业", "资深搬砖人"], key=f"status_{v}")

        q3 = st.multiselect("3. 您最向往的周末状态？", 
                           ["梧桐树下漫步", "弄堂里的精品咖啡", "洱海边发呆看云", "CBD不夜城的灯火", "山间徒步呼吸", "沉浸式看展", "宅家拼乐高", "烟火气摊位扫街"],
                           placeholder="请选择（可多选）...", key=f"q3_{v}")
        
        q4 = st.multiselect("4. 您的核心性格标签？", 
                           ["文艺浪漫", "精致独立", "随性自由", "硬核搞钱", "内敛静谧", "热情如火", "极简主义", "斜杠青年"],
                           placeholder="请选择（可多选）...", key=f"q4_{v}")
        
        q5 = st.multiselect("5. 理想的居住环境？", 
                           ["江南韵味", "科技创新前沿", "被大自然包围", "千年文化底蕴", "魔幻都市感"],
                           placeholder="请选择（可多选）...", key=f"q5_{v}")
        
        # 6-10 题 (此处略，保持之前的代码内容)
        q6 = st.selectbox("6. 面对社交压力？", ["请选择...", "社交悍匪", "礼貌疏离", "隐身术", "观察者"], key=f"q6_{v}")
        q7 = st.selectbox("7. 你的消费观？", ["请选择...", "体验派", "实用派", "随性派", "极简派"], key=f"q7_{v}")
        q8 = st.selectbox("8. 如果有长假？", ["请选择...", "大理/拉萨", "纽约/东京", "回老家", "闭关精进"], key=f"q8_{v}")
        q9 = st.selectbox("9. 关系中最看重？", ["请选择...", "情感共鸣", "未来规划", "独立自由", "安全感"], key=f"q9_{v}")
        q10 = st.selectbox("10. 你的座右铭？", ["请选择...", "诗与远方", "出众出局", "顺其自然", "知行合一"], key=f"q10_{v}")

        if st.button("🚀 生成演算报告", use_container_width=True):
            inputs = [gender, status, q3, q4, q5, q6, q7, q8, q9, q10]
            if "请选择..." in inputs or any(not i for i in [q3, q4, q5]):
                st.error("⚠️ 还有题目未完成哦！")
            else:
                raw_input = "".join([str(i) for i in inputs])
                hash_int = int(hashlib.md5(raw_input.encode()).hexdigest(), 16)
                
                with st.status("🔮 正在锁定磁场...", expanded=False) as s:
                    time.sleep(1.2)
                    s.update(label="演算完成！", state="complete")

                city_db = [
                    {"name": "杭州", "score": "93%", "tags": ["精致", "江南", "平衡感"], "desc": "西湖的烟火气与数字时代的脉搏完美交织。"},
                    {"name": "上海", "score": "97%", "tags": ["时尚", "独立", "国际化"], "desc": "你属于流光溢彩的黄浦江畔，你的精致只有在魔都能被彻底理解。"},
                    {"name": "大理", "score": "89%", "tags": ["清新", "自由", "风花雪月"], "desc": "风花雪月是大理的注脚，更是你灵魂的出口。"},
                    {"name": "成都", "score": "95%", "tags": ["安逸", "火辣", "包容性"], "desc": "那种热辣火爆的性格与极致安逸的生活态度在你身上完美共生。"},
                    {"name": "北京", "score": "96%", "tags": ["宏大", "底蕴", "厚重感"], "desc": "你胸怀大志，北京的深厚底蕴最能接住你的野心。"},
                    {"name": "深圳", "score": "98%", "tags": ["效率", "拼搏", "极速"], "desc": "你拒绝止步不前，深圳这座不谈出身的城市是你的助推器。"},
                    {"name": "西安", "score": "91%", "tags": ["厚重", "文化", "坚定性"], "desc": "你内心深沉如古城墙，渴望在历史呼吸中感受生命底蕴。"},
                    {"name": "长沙", "score": "94%", "tags": ["活力", "娱乐", "烟火气"], "desc": "你是天生的活力派。长沙深夜的欢腾最能点燃你的热情。"}
                ]
                
                res = city_db[hash_int % len(city_db)]
                st.balloons()

                st.markdown(f"<h1 style='text-align: center; color: #00C1D4; font-size: 3.5rem;'>{res['score']}</h1>", unsafe_allow_html=True)
                st.markdown(f"<h2 style='text-align: center;'>📍 天选之城：{res['name']}</h2>", unsafe_allow_html=True)
                
                t_col1, t_col2, t_col3 = st.columns(3)
                t_col1.info(f"**{res['tags'][0]}**")
                t_col2.info(f"**{res['tags'][1]}**")
                t_col3.info(f"**{res['tags'][2]}**")
                
                with st.container(border=True):
                    st.markdown("### ✨ 灵魂契合理由")
                    st.write(res['desc'])
                
                st.button("🔄 重新测试", use_container_width=True, on_click=hard_reset_test)

if __name__ == "__main__":
    main()