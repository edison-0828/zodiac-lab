import streamlit as st
import hashlib
import time

# 1. 页面配置与移动端适配 CSS
st.set_page_config(page_title="性格城市匹配测试", page_icon="📍", layout="centered")

st.markdown("""
    <style>
    /* 基础背景与 App 端适配 */
    .stApp { background-color: #FFFFFF !important; color: #31333F !important; }
    
    .hero-title {
        font-size: clamp(2.2rem, 8vw, 3.5rem); 
        font-weight: 900;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #00C1D4, #4AA9FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 20px;
        line-height: 1.2; 
        letter-spacing: -1px; 
    }
    .icon-container { display: flex; justify-content: center; margin: 25px 0; }
    .location-card {
        width: clamp(100px, 25vw, 130px); height: clamp(100px, 25vw, 130px);
        background: linear-gradient(135deg, #7DE2FC 0%, #B9EDF8 100%);
        border-radius: 25px; display: flex; align-items: center; justify-content: center;
        box-shadow: 0 15px 30px rgba(0, 193, 212, 0.15);
    }
    .intro-section { text-align: center; padding: 0 15px; color: #555555; line-height: 1.8; font-size: clamp(0.95rem, 4vw, 1.1rem); }
    .intro-highlight { color: #1E1E1E; font-weight: 700; border-bottom: 2px solid #00C1D4; }
    
    /* 控件样式 */
    .stSelectbox label, .stMultiSelect label { font-size: 1.05rem !important; font-weight: 800 !important; color: #1E1E1E !important; padding-top: 15px; }
    div.stButton > button { height: 3rem; border-radius: 12px !important; font-weight: 700 !important; }
    
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .block-container { padding-top: 2rem !important; padding-bottom: 2rem !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. 状态管理
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'form_version' not in st.session_state:
    st.session_state.form_version = 0

def hard_reset_test():
    st.session_state.form_version += 1

def main():
    if st.session_state.page == 'home':
        st.markdown('<p class="hero-title">你的性格与哪个城市<br>是天选CP</p>', unsafe_allow_html=True)
        st.markdown('<div class="icon-container"><div class="location-card"><span style="font-size: clamp(50px, 15vw, 70px);">📍</span></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="intro-section">城市是钢筋水泥的森林，也是安放内心的容器。<br>有人生来属于上海的霓虹，有人注定流浪在 <span class="intro-highlight">大理的云边</span>。<br><br>解锁你的「地理人格」，找到那个与你灵魂同鸣的 <span class="intro-highlight">天选之地</span>。</div>', unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)
        if st.button("✨ 开启我的地理人格测算", use_container_width=True):
            st.session_state.page = 'test'
            st.rerun()

    elif st.session_state.page == 'test':
        v = st.session_state.form_version
        st.markdown("<h2 style='text-align: center; color: #1E1E1E; font-weight:900;'>📍 录入您的灵魂坐标</h2>", unsafe_allow_html=True)
        st.write("---")

        # --- 1-2 题：保留原始通俗选项 ---
        gender = st.selectbox("1. 您的性别", ["请选择...", "男生", "女生", "保密"], key=f"gender_{v}")
        status = st.selectbox("2. 目前的生活阶段", ["请选择...", "学生党", "职场新锐", "自由职业", "资深搬砖人"], key=f"status_{v}")

        # --- 3-10 题：保持算法中立性选项 ---
        q3 = st.multiselect("3. 当你独处时，哪种能量让你最舒适？", 
                           ["绝对的寂静", "远处的市声", "自然的呼吸感", "秩序井然的节律", "充满可能的未知感", "温暖的人间烟火"],
                           placeholder="请选择（可多选）...", key=f"q3_{v}")
        
        q4 = st.multiselect("4. 你的核心性格底色是？", 
                           ["求知驱动", "审美驱动", "效率驱动", "情感驱动", "自由驱动", "感官驱动"],
                           placeholder="请选择（可多选）...", key=f"q4_{v}")
        
        q5 = st.multiselect("5. 你理想中的生命状态是？", 
                           ["在繁华中保持清醒", "在广阔中寻找边界", "在细节中雕刻生活", "在变化中创造价值", "在稳定中体验细碎"],
                           placeholder="请选择（可多选）...", key=f"q5_{v}")
        
        q6 = st.selectbox("6. 面对未知的规则，你倾向于？", ["请选择...", "快速适应并利用", "保持审慎并解构", "寻找共鸣并融入", "建立属于自己的体系"], key=f"q6_{v}")
        q7 = st.selectbox("7. 什么样的成就感最令你着迷？", ["请选择...", "掌握复杂事物的快感", "创造美学价值的愉悦", "获得群体认同的温度", "突破自我边界的释放"], key=f"q7_{v}")
        q8 = st.selectbox("8. 若有一扇通往理想生活的门，门后是？", ["请选择...", "无尽的时间自由", "极致的物质文明", "深厚的精神传承", "原始的生命律动"], key=f"q8_{v}")
        q9 = st.selectbox("9. 在一段深刻的关系中，你寻求？", ["请选择...", "彼此独立的灵魂共振", "并肩作战的现实支持", "无条件的包容与接纳", "共同成长的智力博弈"], key=f"q9_{v}")
        q10 = st.selectbox("10. 哪句座右铭更贴合你的潜意识？", ["请选择...", "世界是我的表象", "我思故我在", "生活即艺术", "唯有奋斗不被辜负"], key=f"q10_{v}")

        if st.button("🚀 生成演算报告", use_container_width=True):
            inputs = [gender, status, q3, q4, q5, q6, q7, q8, q9, q10]
            if "请选择..." in inputs or any(not i for i in [q3, q4, q5]):
                st.error("⚠️ 磁场感应尚未完整，请完成所有选项。")
            else:
                raw_input = "".join([str(i) for i in inputs])
                hash_int = int(hashlib.md5(raw_input.encode()).hexdigest(), 16)
                
                with st.status("🔮 正在解析灵魂坐标...", expanded=False) as s:
                    time.sleep(1)
                    s.update(label="灵魂匹配成功！", state="complete")

                # 城市数据库
                city_db = [
                    {"name": "杭州", "score": "93%", "tags": ["精致", "江南", "平衡感"], "desc": "你追求在繁华与自然间游走。杭州的诗意与现代脉搏能完美契合你对‘审美平衡’的渴求。"},
                    {"name": "上海", "score": "97%", "tags": ["时尚", "独立", "国际化"], "desc": "你天生具备‘效率驱动’的底色。魔都的边界感与高效率，是你这种独立灵魂的最佳主场。"},
                    {"name": "大理", "score": "89%", "tags": ["清新", "自由", "慢生活"], "desc": "你渴望原始的生命律动。在苍山洱海间，你能彻底放下‘社交面具’，回归真实的自我。"},
                    {"name": "成都", "score": "95%", "tags": ["安逸", "火辣", "包容性"], "desc": "你极度看重情感温度。成都那份不急不躁的市井烟火，最能安放你那颗热烈又温柔的心。"},
                    {"name": "北京", "score": "96%", "tags": ["宏大", "底蕴", "厚重感"], "desc": "你心中有宏大叙事。北京的厚重感与充满机会的磁场，最能匹配你‘求知并向上’的野心。"},
                    {"name": "深圳", "score": "98%", "tags": ["效率", "拼搏", "极速"], "desc": "你拒绝精神内耗。深圳这座崇尚‘拼搏与突破’的城市，是你灵魂的天然加速器。"},
                    {"name": "西安", "score": "91%", "tags": ["厚重", "文化", "坚定性"], "desc": "你寻求跨越时间的笃定感。西安的古朴与沉静，能为你那颗内敛的心提供最深沉的支撑。"},
                    {"name": "长沙", "score": "94%", "tags": ["活力", "娱乐", "烟火气"], "desc": "你是天生的能量体。长沙那份不知疲倦的鲜活与热爱，最能精准点亮你每一个生命细胞。"}
                ]
                
                res = city_db[hash_int % len(city_db)]
                st.balloons()

                st.markdown(f"<h1 style='text-align: center; color: #00C1D4; font-size: 3.5rem; margin-bottom: 0;'>{res['score']}</h1>", unsafe_allow_html=True)
                st.markdown(f"<h2 style='text-align: center; margin-top: 0;'>📍 天选之城：{res['name']}</h2>", unsafe_allow_html=True)
                
                t_col1, t_col2, t_col3 = st.columns(3)
                t_col1.info(f"**{res['tags'][0]}**")
                t_col2.info(f"**{res['tags'][1]}**")
                t_col3.info(f"**{res['tags'][2]}**")
                
                with st.container(border=True):
                    st.markdown("### ✨ 灵魂契合理由")
                    st.write(res['desc'])
                
                # 原地重置按钮
                st.button("🔄 重新测试", use_container_width=True, on_click=hard_reset_test)

if __name__ == "__main__":
    main()