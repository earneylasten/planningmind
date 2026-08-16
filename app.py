import streamlit as st
import requests

st.set_page_config(
    page_title="PlanningMind · ViaMoon",
    page_icon="https://exhibz.viamoon.com/wp-content/uploads/2026/08/cropped-Favicon114.png",
    layout="wide",
)

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

def save_assessment(data: dict) -> bool:
    try:
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/planningmind_assessments",
            json=data,
            headers={
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
                "Prefer": "return=minimal",
            },
            timeout=5,
        )
        return response.status_code == 201
    except Exception:
        return False

BLUEPRINT_STEPS = {
    1:  "Define the Mission — Why does this project exist?",
    2:  "Define the Vision — What will it look like at its best?",
    3:  "Identify Decision Makers — Who has authority?",
    4:  "Identify Key Stakeholders — Who is affected?",
    5:  "Build Stakeholder Consensus — Align interests",
    6:  "Understand the Market — Who are your visitors/users?",
    7:  "Supply Analysis — What already exists?",
    8:  "Demand Analysis — Who wants this and how many?",
    9:  "Competitive Analysis — What are similar destinations doing?",
    10: "External Factors — What forces shape the context?",
    11: "Risk Analysis — What could go wrong?",
    12: "Environmental Scan — What is the ecological situation?",
    13: "Climate & Resource Assessment — What are the limits?",
    14: "Cultural Context — What are the heritage values?",
    15: "Story Development — What is the narrative?",
    16: "Location Analysis — Where exactly?",
    17: "Site Size & Capacity — How big? How many?",
    18: "Accessibility Planning — Who can reach it and how?",
    19: "Concept Design — What will it physically look like?",
    20: "Prototype Development — Test the concept",
    21: "Charrette Process — Stakeholder design review",
    22: "Feasibility Assessment — Is it viable?",
    23: "Financial Planning — What will it cost and earn?",
    24: "Marketing Strategy — How will people know?",
    25: "Implementation Plan — How will it be built?",
    26: "Launch & Operations — How will it run?",
}

STAGES = {
    1: ("Exploration", "Few visitors, no formal infrastructure. Destination largely unknown."),
    2: ("Involvement", "Local initiatives emerging. Basic facilities developing. Visitor numbers growing slowly."),
    3: ("Development", "Rapid growth. Investment arriving. Infrastructure expanding fast."),
    4: ("Consolidation", "Growth slowing. Market maturing. Destination well established."),
    5: ("Stagnation", "Peak capacity reached. Visitor numbers plateau. Environmental and social stress appearing."),
    6: ("Decline", "Visitor numbers falling. Losing competitiveness. Urgent intervention needed."),
    7: ("Rejuvenation", "Active reinvention underway. New products, new markets, new infrastructure."),
}

INTERVENTIONS = {
    1: "Foundational planning needed. Focus on Steps 1-6 — establish mission, vision, and stakeholder alignment before any development begins.",
    2: "Structure the growth. Steps 3-8 are critical — formalize stakeholder engagement and conduct supply and demand analysis.",
    3: "Manage rapid development. Steps 9-18 are urgent — assess carrying capacity and protect what makes your destination unique.",
    4: "Diversify and refresh. Steps 6-8 and 24-26 apply — strengthen your market understanding and marketing strategy.",
    5: "Urgent intervention required. Steps 1-2 and 19-23 are critical — redefine your vision and redesign your product offering.",
    6: "Bold action needed. Full 26-step replanning recommended. Start from Step 1 and rebuild systematically.",
    7: "Sustain the momentum. Steps 19-26 apply — lock in design innovations and execute your relaunch strategy.",
}

DIMENSION_TO_STEPS = {
    "destination":   {"urgent": [1,2,3],   "important": [15,16,17]},
    "marketing":     {"urgent": [6,7,8],   "important": [24,25,26]},
    "economic":      {"urgent": [9,10,11], "important": [22,23,24]},
    "social":        {"urgent": [3,4,5],   "important": [6,7,21]},
    "environmental": {"urgent": [12,13],   "important": [17,18,22]},
    "housing_labor": {"urgent": [9,10],    "important": [12,13,24]},
    "climate":       {"urgent": [13,14],   "important": [12,22,23]},
    "cultural":      {"urgent": [1,2,14],  "important": [3,4,19,21]},
    "accessibility": {"urgent": [5,6,18],  "important": [16,17,19]},
    "digital":       {"urgent": [7,8],     "important": [24,25,26]},
    "governance":    {"urgent": [3,4],     "important": [5,6,22]},
}

WEIGHTS = {
    "destination": 0.10, "marketing": 0.08,
    "economic": 0.12, "social": 0.10,
    "environmental": 0.10, "housing_labor": 0.09,
    "climate": 0.09, "cultural": 0.09,
    "accessibility": 0.08, "digital": 0.07,
    "governance": 0.08,
}

DIM_LABELS = {
    "destination":   "🏝️ Destination Characteristics",
    "marketing":     "📣 Marketing Response",
    "economic":      "💰 Economic Impacts",
    "social":        "👥 Social Impacts",
    "environmental": "🌿 Environmental Impacts",
    "housing_labor": "🏠 Housing & Labor Affordability",
    "climate":       "🌡️ Climate & Resource Resilience",
    "cultural":      "🎭 Cultural Authenticity & Language",
    "accessibility": "♿ Accessibility & Inclusive Tourism",
    "digital":       "📱 Digital & Reputation Dynamics",
    "governance":    "🏛️ Governance & Institutional Capacity",
}

def get_stage(dhi):
    if dhi >= 80: return 3
    if dhi >= 65: return 4
    if dhi >= 50: return 2
    if dhi >= 35: return 5
    if dhi >= 20: return 1
    return 6

def get_blueprint(scores):
    urgent = set()
    important = set()
    for dim, score in scores.items():
        if dim not in DIMENSION_TO_STEPS:
            continue
        m = DIMENSION_TO_STEPS[dim]
        if score < 40:
            urgent.update(m["urgent"])
            important.update(m["important"])
        elif score < 65:
            important.update(m["urgent"])
    return sorted(urgent), sorted(important - urgent)

# ── Header ────────────────────────────────

col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image(
        "https://viamoon.com/viamoon-logo.png",
        width=180,
    )
with col_title:
    st.title("🌙 PlanningMind")
    st.subheader("Destination Health Index · Planning Blueprint Mapper")
    st.markdown(
        "**By Dr. Earney F. Lasten, Ph.D. · "
        "[viamoon.com](https://viamoon.com)**"
    )

st.markdown("""
*The Lasten Destination Intelligence Framework (LDIF) —
an 11-dimension diagnostic system for destination health,
lifecycle positioning, and planning intervention,
combined with the 26-step Planning Blueprint Process.*

*© 2026 Dr. Earney F. Lasten, Ph.D. — Original framework.*
""")
st.divider()

# ── Inputs ────────────────────────────────

col1, col2 = st.columns(2)
with col1:
    destination = st.text_input(
        "🏝️ Destination / City / Region",
        placeholder="e.g. Aruba, New York, San Nicolas, Medellín..."
    )
with col2:
    country = st.text_input(
        "🌍 Country / Territory",
        placeholder="e.g. Aruba, USA, Colombia, Netherlands..."
    )

st.markdown("### Score each dimension 0–100")
st.caption("0 = Critical problem · 50 = Needs attention · 100 = Excellent")

# ── Sliders ───────────────────────────────

scores = {}
col_a, col_b = st.columns(2)

with col_a:
    scores["destination"]   = st.slider("🏝️ 1. Destination Characteristics", 0, 100, 50, 5)
    scores["marketing"]     = st.slider("📣 2. Marketing Response", 0, 100, 50, 5)
    scores["economic"]      = st.slider("💰 3. Economic Impacts", 0, 100, 50, 5)
    scores["social"]        = st.slider("👥 4. Social Impacts", 0, 100, 50, 5)
    scores["environmental"] = st.slider("🌿 5. Environmental Impacts", 0, 100, 50, 5)
    scores["housing_labor"] = st.slider("🏠 6. Housing & Labor Affordability", 0, 100, 50, 5)

with col_b:
    scores["climate"]       = st.slider("🌡️ 7. Climate & Resource Resilience", 0, 100, 50, 5)
    scores["cultural"]      = st.slider("🎭 8. Cultural Authenticity & Language", 0, 100, 50, 5)
    scores["accessibility"] = st.slider("♿ 9. Accessibility & Inclusive Tourism", 0, 100, 50, 5)
    scores["digital"]       = st.slider("📱 10. Digital & Reputation Dynamics", 0, 100, 50, 5)
    scores["governance"]    = st.slider("🏛️ 11. Governance & Institutional Capacity", 0, 100, 50, 5)

st.divider()

# ── Analyze ───────────────────────────────

if st.button("🔍 Analyze My Destination →", type="primary", use_container_width=True):

    if not destination or not country:
        st.error("⚠️ Please enter a destination name and country.")
    else:
        dhi = round(sum(scores[k] * WEIGHTS[k] for k in WEIGHTS), 1)
        dhi_label = (
            "🟢 Healthy" if dhi >= 65
            else "🟡 Needs Attention" if dhi >= 40
            else "🔴 Critical"
        )
        stage_num = get_stage(dhi)
        stage_name, stage_desc = STAGES[stage_num]
        urgent_steps, important_steps = get_blueprint(scores)

        saved = save_assessment({
            "destination_name": destination,
            "country": country,
            "score_destination": scores["destination"],
            "score_marketing": scores["marketing"],
            "score_economic": scores["economic"],
            "score_social": scores["social"],
            "score_environmental": scores["environmental"],
            "score_housing_labor": scores["housing_labor"],
            "score_climate": scores["climate"],
            "score_cultural": scores["cultural"],
            "score_accessibility": scores["accessibility"],
            "score_digital": scores["digital"],
            "score_governance": scores["governance"],
            "dhi_score": dhi,
            "destination_stage": stage_num,
            "stage_name": stage_name,
        })
        if saved:
            st.toast("✅ Assessment saved", icon="🌙")
        else:
            st.toast("⚠️ Could not save — results still shown")

        st.markdown(f"## 📊 Results — {destination}, {country}")

        tab1, tab2, tab3, tab4 = st.tabs([
            "📈 Health Index",
            "🔄 Destination Stage",
            "🗺️ 26-Step Blueprint",
            "✅ Action Plan",
        ])

        with tab1:
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.metric("Destination Health Index (DHI)", f"{dhi}/100", dhi_label)
            with col_m2:
                st.metric("Destination Stage", f"Stage {stage_num}", stage_name)
            st.progress(dhi / 100)
            st.markdown("#### Dimension Scores")
            for dim, label in DIM_LABELS.items():
                score = scores[dim]
                icon = "🟢" if score >= 65 else "🟡" if score >= 40 else "🔴"
                c1, c2 = st.columns([5, 1])
                with c1:
                    st.progress(score / 100, text=label)
                with c2:
                    st.markdown(f"{icon} **{score}**")
            st.caption("Lasten Destination Intelligence Framework (LDIF) · © 2026 Dr. Earney F. Lasten, Ph.D.")

        with tab2:
            st.markdown(f"### Stage {stage_num}: **{stage_name}**")
            st.info(stage_desc)
            st.markdown("#### What this means for your destination:")
            st.write(INTERVENTIONS[stage_num])
            st.markdown("#### All Destination Stages")
            for num, (name, desc) in STAGES.items():
                if num == stage_num:
                    st.markdown(f"**▶ Stage {num}: {name}** ← *{destination}*")
                else:
                    st.markdown(f"Stage {num}: {name}")
            st.caption("Lasten Destination Intelligence Framework (LDIF) · © 2026 Dr. Earney F. Lasten, Ph.D.")

        with tab3:
            st.markdown(f"### 26-Step Planning Blueprint — {destination}")
            st.markdown("Based on your 11-dimension scores, these planning steps apply to your destination right now.")
            if urgent_steps:
                st.markdown("#### 🔴 Urgent — Address Immediately")
                for s in urgent_steps:
                    st.markdown(f"**Step {s}** — {BLUEPRINT_STEPS[s]}")
            else:
                st.success("No urgent steps — your destination is performing well.")
            if important_steps:
                st.markdown("#### 🟡 Important — Address This Quarter")
                for s in important_steps:
                    st.markdown(f"Step {s} — {BLUEPRINT_STEPS[s]}")
            st.markdown("#### The 7 Major Questions")
            questions = [
                ("Why?",     "Steps 1-2",   "Mission & Vision"),
                ("Who?",     "Steps 3-6",   "Stakeholders & Market"),
                ("What?",    "Steps 7-14",  "Analysis & Context"),
                ("When?",    "Step 15",     "Story & Timeline"),
                ("Where?",   "Steps 16-18", "Location & Access"),
                ("How?",     "Steps 19-23", "Design & Feasibility"),
                ("Execute!", "Steps 24-26", "Marketing & Launch"),
            ]
            for q, steps, desc in questions:
                st.markdown(f"**{q}** · {steps} · {desc}")
            st.markdown("Execute your full plan at **[viamoon.com/flowchart](https://viamoon.com/flowchart)**")
            st.caption("26-step Planning Blueprint Process · © 2026 Dr. Earney F. Lasten, Ph.D.")

        with tab4:
            st.markdown(f"### Action Plan — {destination}")
            critical = [(k, v) for k, v in scores.items() if v < 40]
            critical.sort(key=lambda x: x[1])
            if critical:
                st.markdown("#### Most Critical Dimensions:")
                for dim, score in critical[:3]:
                    st.error(f"🔴 **{DIM_LABELS[dim]}** — scored {score}/100 — requires immediate intervention.")
            else:
                st.success("🟢 No critical dimensions. Focus on maintaining strengths.")
            st.markdown("#### Recommended Next Steps:")
            st.markdown("1. Review the urgent Blueprint steps in the 26-Step tab above")
            st.markdown("2. Engage a certified planning expert → [viamoon.com/network](https://viamoon.com/network)")
            st.markdown("3. Post your planning project → [viamoon.com/marketplace](https://viamoon.com/marketplace)")
            st.markdown("4. Use the full 26-step platform → [viamoon.com/flowchart](https://viamoon.com/flowchart)")
            st.markdown("5. Read The Experience Masterplan → [viamoon.com/textbook](https://viamoon.com/textbook)")
            st.divider()
            st.caption(
                "PlanningMind · Lasten Destination Intelligence Framework (LDIF) · "
                "26-step Planning Blueprint Process · "
                "© 2026 Dr. Earney F. Lasten, Ph.D. · "
                "VIAMOON Consultancy (Aruba) · VIAMOON SAS (Colombia) · "
                "viamoon.com"
            )
