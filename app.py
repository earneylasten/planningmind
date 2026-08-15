import streamlit as st

st.set_page_config(
    page_title="PlanningMind · ViaMoon",
    page_icon="🌙",
    layout="wide",
)

st.title("🌙 PlanningMind")
st.subheader("Destination Health Index · Planning Blueprint Mapper")
st.markdown("**By Dr. Earney F. Lasten, Ph.D. · [viamoon.com](https://viamoon.com)**")
st.markdown("""
*The Lasten Destination Intelligence Framework (LDIF) —
an 11-dimension diagnostic system for destination health,
lifecycle positioning, and planning intervention.
Combined with the 26-step Planning Blueprint Process.*

*© 2026 Dr. Earney F. Lasten, Ph.D. — Original framework.*
""")
st.divider()

col1, col2 = st.columns(2)
with col1:
    destination = st.text_input("🏝️ Destination Name", placeholder="e.g. Aruba...")
with col2:
    country = st.text_input("🌍 Country", placeholder="e.g. Aruba...")

st.markdown("### Score each dimension 0–100")

s1  = st.slider("🏝️ 1. Destination Characteristics", 0, 100, 50)
s2  = st.slider("📣 2. Marketing Response", 0, 100, 50)
s3  = st.slider("💰 3. Economic Impacts", 0, 100, 50)
s4  = st.slider("👥 4. Social Impacts", 0, 100, 50)
s5  = st.slider("🌿 5. Environmental Impacts", 0, 100, 50)
s6  = st.slider("🏠 6. Housing & Labor Affordability", 0, 100, 50)
s7  = st.slider("🌡️ 7. Climate & Resource Resilience", 0, 100, 50)
s8  = st.slider("🎭 8. Cultural Authenticity & Language", 0, 100, 50)
s9  = st.slider("♿ 9. Accessibility & Inclusive Tourism", 0, 100, 50)
s10 = st.slider("📱 10. Digital & Reputation Dynamics", 0, 100, 50)
s11 = st.slider("🏛️ 11. Governance & Institutional Capacity", 0, 100, 50)

if st.button("🔍 Analyze My Destination", type="primary"):
    if not destination or not country:
        st.error("Please enter a destination name and country.")
    else:
        dhi = round(
            s1*0.10 + s2*0.08 + s3*0.12 + s4*0.10 +
            s5*0.10 + s6*0.09 + s7*0.09 + s8*0.09 +
            s9*0.08 + s10*0.07 + s11*0.08, 1
        )

        if dhi >= 65:
            label = "🟢 Healthy"
        elif dhi >= 40:
            label = "🟡 Needs Attention"
        else:
            label = "🔴 Critical"

        if dhi >= 80:
            stage, stage_desc = 3, "Development — Rapid growth. External investment arriving."
        elif dhi >= 65:
            stage, stage_desc = 4, "Consolidation — Growth slowing. Market maturing."
        elif dhi >= 50:
            stage, stage_desc = 2, "Involvement — Local initiatives emerging."
        elif dhi >= 35:
            stage, stage_desc = 5, "Stagnation — Peak capacity reached. Urgent attention needed."
        elif dhi >= 20:
            stage, stage_desc = 1, "Exploration — Few visitors, no formal infrastructure."
        else:
            stage, stage_desc = 6, "Decline — Visitor numbers falling. Bold action needed."

        st.success(f"### {destination}, {country}")
        st.metric("Destination Health Index (DHI)", f"{dhi}/100", label)
        st.progress(dhi / 100)

        st.markdown(f"### Butler Stage {stage}: {stage_desc}")

        st.markdown("### Your dimension scores:")
        dims = [
            ("🏝️ Destination Characteristics", s1),
            ("📣 Marketing Response", s2),
            ("💰 Economic Impacts", s3),
            ("👥 Social Impacts", s4),
            ("🌿 Environmental Impacts", s5),
            ("🏠 Housing & Labor", s6),
            ("🌡️ Climate Resilience", s7),
            ("🎭 Cultural Authenticity", s8),
            ("♿ Accessibility", s9),
            ("📱 Digital & Reputation", s10),
            ("🏛️ Governance", s11),
        ]
        for name, score in dims:
            icon = "🟢" if score >= 65 else "🟡" if score >= 40 else "🔴"
            st.write(f"{icon} {name}: **{score}/100**")

        st.divider()
        st.markdown(
            "Execute your plan at [viamoon.com](https://viamoon.com) · "
            "Get matched with experts at [viamoon.com/network](https://viamoon.com/network)"
        )
        st.caption(
            "PlanningMind by ViaMoon · Dr. Earney F. Lasten, Ph.D. · "
            "Planning Blueprint Process (Lasten & Pizam, 2013) · "
            "© 2026 VIAMOON Consultancy"
        )
