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

# ── Translations ──────────────────────────

TRANSLATIONS = {
    "English": {
        "lang_code": "en",
        "subtitle": "Destination Health Index · Planning Blueprint Mapper",
        "by": "By Dr. Earney F. Lasten, Ph.D.",
        "framework_desc": (
            "*The Lasten Destination Intelligence Framework (LDIF) — "
            "an 11-dimension diagnostic system for destination health, "
            "lifecycle positioning, and planning intervention, "
            "combined with the 26-step Planning Blueprint Process.*"
        ),
        "copyright": "© 2026 Dr. Earney F. Lasten, Ph.D. — Original framework.",
        "dest_label": "🏝️ Destination / City / Region",
        "dest_placeholder": "e.g. Aruba, New York, San Nicolas, Medellín...",
        "country_label": "🌍 Country / Territory",
        "country_placeholder": "e.g. Aruba, USA, Colombia, Netherlands...",
        "score_title": "### Score each dimension 0–100",
        "score_caption": "0 = Critical problem · 50 = Needs attention · 100 = Excellent",
        "analyze_btn": "🔍 Analyze My Destination →",
        "error_msg": "⚠️ Please enter a destination name and country.",
        "saved_ok": "✅ Assessment saved",
        "saved_fail": "⚠️ Could not save — results still shown",
        "results_title": "## 📊 Results —",
        "tab_health": "📈 Health Index",
        "tab_stage": "🔄 Destination Stage",
        "tab_blueprint": "🗺️ 26-Step Blueprint",
        "tab_action": "✅ Action Plan",
        "dhi_label": "Destination Health Index (DHI)",
        "stage_label": "Destination Stage",
        "dim_scores": "#### Dimension Scores",
        "stage_means": "#### What this means for your destination:",
        "all_stages": "#### All Destination Stages",
        "your_dest": "← Your destination",
        "blueprint_title": "### 26-Step Planning Blueprint —",
        "blueprint_desc": "Based on your 11-dimension scores, these planning steps apply to your destination right now.",
        "ready_cta": "🗺️ **Ready to execute?** Work through all 26 steps at [viamoon.com/flowchart](https://viamoon.com/flowchart) — with AI guidance at every step.",
        "urgent": "#### 🔴 Urgent — Address Immediately",
        "important": "#### 🟡 Important — Address This Quarter",
        "no_urgent": "No urgent steps — your destination is performing well.",
        "seven_q": "#### The 7 Major Questions",
        "action_title": "### Action Plan —",
        "critical_dims": "#### Most Critical Dimensions:",
        "no_critical": "🟢 No critical dimensions. Focus on maintaining strengths.",
        "next_steps": "#### Recommended Next Steps:",
        "step1": "1. Review urgent Blueprint steps in the 26-Step tab above",
        "step2": "2. Engage a certified planning expert → [viamoon.com/network](https://viamoon.com/network)",
        "step3": "3. Post your planning project → [viamoon.com/marketplace](https://viamoon.com/marketplace)",
        "step4": "4. Use the full 26-step platform → [viamoon.com/flowchart](https://viamoon.com/flowchart)",
        "step5": "5. Read The Experience Masterplan → [viamoon.com/textbook](https://viamoon.com/textbook)",
        "requires": "— requires immediate intervention.",
        "welcome": "🌙 Welcome from lifecycle.viamoon.com — continuing your deeper analysis for",
        "welcome2": ". Score all 11 dimensions below and click Analyze.",
        "open": "Open ↗",
        "healthy": "🟢 Healthy",
        "attention": "🟡 Needs Attention",
        "critical": "🔴 Critical",
        "dim_labels": {
            "destination":   "🏝️ 1. Destination Characteristics",
            "marketing":     "📣 2. Marketing Response",
            "economic":      "💰 3. Economic Impacts",
            "social":        "👥 4. Social Impacts",
            "environmental": "🌿 5. Environmental Impacts",
            "housing_labor": "🏠 6. Housing & Labor Affordability",
            "climate":       "🌡️ 7. Climate & Resource Resilience",
            "cultural":      "🎭 8. Cultural Authenticity & Language",
            "accessibility": "♿ 9. Accessibility & Inclusive Tourism",
            "digital":       "📱 10. Digital & Reputation Dynamics",
            "governance":    "🏛️ 11. Governance & Institutional Capacity",
        },
        "stages": {
            1: ("Exploration", "Few visitors, no formal infrastructure. Destination largely unknown."),
            2: ("Involvement", "Local initiatives emerging. Basic facilities developing. Visitor numbers growing slowly."),
            3: ("Development", "Rapid growth. Investment arriving. Infrastructure expanding fast."),
            4: ("Consolidation", "Growth slowing. Market maturing. Destination well established."),
            5: ("Stagnation", "Peak capacity reached. Visitor numbers plateau. Environmental and social stress appearing."),
            6: ("Decline", "Visitor numbers falling. Losing competitiveness. Urgent intervention needed."),
            7: ("Rejuvenation", "Active reinvention underway. New products, new markets, new infrastructure."),
        },
        "interventions": {
            1: "Foundational planning needed. Focus on Steps 1-6 — establish mission, vision, and stakeholder alignment before any development begins.",
            2: "Structure the growth. Steps 3-8 are critical — formalize stakeholder engagement and conduct supply and demand analysis.",
            3: "Manage rapid development. Steps 9-18 are urgent — assess carrying capacity and protect what makes your destination unique.",
            4: "Diversify and refresh. Steps 6-8 and 24-26 apply — strengthen your market understanding and marketing strategy.",
            5: "Urgent intervention required. Steps 1-2 and 19-23 are critical — redefine your vision and redesign your product offering.",
            6: "Bold action needed. Full 26-step replanning recommended. Start from Step 1 and rebuild systematically.",
            7: "Sustain the momentum. Steps 19-26 apply — lock in design innovations and execute your relaunch strategy.",
        },
        "questions": [
            ("Why?",     "Steps 1-2",   "Mission & Vision"),
            ("Who?",     "Steps 3-6",   "Stakeholders & Market"),
            ("What?",    "Steps 7-14",  "Analysis & Context"),
            ("When?",    "Step 15",     "Story & Timeline"),
            ("Where?",   "Steps 16-18", "Location & Access"),
            ("How?",     "Steps 19-23", "Design & Feasibility"),
            ("Execute!", "Steps 24-26", "Marketing & Launch"),
        ],
    },

    "Español": {
        "lang_code": "es",
        "subtitle": "Índice de Salud del Destino · Mapeador del Plan de Desarrollo",
        "by": "Por el Dr. Earney F. Lasten, Ph.D.",
        "framework_desc": (
            "*El Marco de Inteligencia de Destinos Lasten (LDIF) — "
            "un sistema diagnóstico de 11 dimensiones para la salud del destino, "
            "posicionamiento en el ciclo de vida e intervención de planificación, "
            "combinado con el Proceso de 26 Pasos del Plan de Desarrollo.*"
        ),
        "copyright": "© 2026 Dr. Earney F. Lasten, Ph.D. — Marco original.",
        "dest_label": "🏝️ Destino / Ciudad / Región",
        "dest_placeholder": "ej. Aruba, Medellín, Cartagena, Bogotá...",
        "country_label": "🌍 País / Territorio",
        "country_placeholder": "ej. Colombia, Aruba, España, México...",
        "score_title": "### Puntúe cada dimensión de 0 a 100",
        "score_caption": "0 = Problema crítico · 50 = Necesita atención · 100 = Excelente",
        "analyze_btn": "🔍 Analizar Mi Destino →",
        "error_msg": "⚠️ Por favor ingrese el nombre del destino y el país.",
        "saved_ok": "✅ Evaluación guardada",
        "saved_fail": "⚠️ No se pudo guardar — resultados mostrados",
        "results_title": "## 📊 Resultados —",
        "tab_health": "📈 Índice de Salud",
        "tab_stage": "🔄 Etapa del Destino",
        "tab_blueprint": "🗺️ Plan de 26 Pasos",
        "tab_action": "✅ Plan de Acción",
        "dhi_label": "Índice de Salud del Destino (DHI)",
        "stage_label": "Etapa del Destino",
        "dim_scores": "#### Puntajes por Dimensión",
        "stage_means": "#### ¿Qué significa esto para su destino?",
        "all_stages": "#### Todas las Etapas del Destino",
        "your_dest": "← Su destino",
        "blueprint_title": "### Plan de Desarrollo de 26 Pasos —",
        "blueprint_desc": "Basado en sus puntajes de 11 dimensiones, estos pasos de planificación aplican a su destino ahora mismo.",
        "ready_cta": "🗺️ **¿Listo para ejecutar?** Trabaje los 26 pasos en [viamoon.com/flowchart](https://viamoon.com/flowchart) — con guía de IA en cada paso.",
        "urgent": "#### 🔴 Urgente — Atender de Inmediato",
        "important": "#### 🟡 Importante — Atender Este Trimestre",
        "no_urgent": "No hay pasos urgentes — su destino está funcionando bien.",
        "seven_q": "#### Las 7 Preguntas Principales",
        "action_title": "### Plan de Acción —",
        "critical_dims": "#### Dimensiones Más Críticas:",
        "no_critical": "🟢 Sin dimensiones críticas. Enfóquese en mantener las fortalezas.",
        "next_steps": "#### Próximos Pasos Recomendados:",
        "step1": "1. Revise los pasos urgentes en la pestaña de 26 Pasos",
        "step2": "2. Contacte un experto certificado → [viamoon.com/network](https://viamoon.com/network)",
        "step3": "3. Publique su proyecto → [viamoon.com/marketplace](https://viamoon.com/marketplace)",
        "step4": "4. Use la plataforma completa → [viamoon.com/flowchart](https://viamoon.com/flowchart)",
        "step5": "5. Lea El Masterplan de la Experiencia → [viamoon.com/textbook](https://viamoon.com/textbook)",
        "requires": "— requiere intervención inmediata.",
        "welcome": "🌙 Bienvenido desde lifecycle.viamoon.com — continuando su análisis para",
        "welcome2": ". Puntúe las 11 dimensiones y haga clic en Analizar.",
        "open": "Abrir ↗",
        "healthy": "🟢 Saludable",
        "attention": "🟡 Necesita Atención",
        "critical": "🔴 Crítico",
        "dim_labels": {
            "destination":   "🏝️ 1. Características del Destino",
            "marketing":     "📣 2. Respuesta de Marketing",
            "economic":      "💰 3. Impactos Económicos",
            "social":        "👥 4. Impactos Sociales",
            "environmental": "🌿 5. Impactos Ambientales",
            "housing_labor": "🏠 6. Vivienda y Asequibilidad Laboral",
            "climate":       "🌡️ 7. Resiliencia Climática y de Recursos",
            "cultural":      "🎭 8. Autenticidad Cultural e Idioma",
            "accessibility": "♿ 9. Accesibilidad y Turismo Inclusivo",
            "digital":       "📱 10. Dinámica Digital y Reputación",
            "governance":    "🏛️ 11. Capacidad de Gobernanza",
        },
        "stages": {
            1: ("Exploración", "Pocos visitantes, sin infraestructura formal. Destino poco conocido."),
            2: ("Involucramiento", "Iniciativas locales emergentes. Instalaciones básicas en desarrollo."),
            3: ("Desarrollo", "Crecimiento rápido. Inversión llegando. Infraestructura en expansión."),
            4: ("Consolidación", "Crecimiento desacelerándose. Mercado madurando. Destino bien establecido."),
            5: ("Estancamiento", "Capacidad máxima alcanzada. Visitantes en meseta. Estrés ambiental y social."),
            6: ("Declive", "Visitantes disminuyendo. Perdiendo competitividad. Intervención urgente necesaria."),
            7: ("Rejuvenecimiento", "Reinvención activa. Nuevos productos, mercados e infraestructura."),
        },
        "interventions": {
            1: "Se necesita planificación fundamental. Enfóquese en los Pasos 1-6 — establezca misión, visión y alineación de partes interesadas.",
            2: "Estructure el crecimiento. Los Pasos 3-8 son críticos — formalice el compromiso de partes interesadas y realice análisis de oferta y demanda.",
            3: "Gestione el desarrollo rápido. Los Pasos 9-18 son urgentes — evalúe la capacidad de carga y proteja lo único de su destino.",
            4: "Diversifique y refresque. Los Pasos 6-8 y 24-26 aplican — fortalezca su comprensión del mercado y estrategia de marketing.",
            5: "Se requiere intervención urgente. Los Pasos 1-2 y 19-23 son críticos — redefina su visión y rediseñe su oferta.",
            6: "Se necesita acción audaz. Se recomienda replanificación completa de 26 pasos. Comience desde el Paso 1.",
            7: "Sostenga el impulso. Los Pasos 19-26 aplican — consolide innovaciones de diseño y ejecute su estrategia de relanzamiento.",
        },
        "questions": [
            ("¿Por qué?", "Pasos 1-2",   "Misión y Visión"),
            ("¿Quién?",   "Pasos 3-6",   "Partes Interesadas"),
            ("¿Qué?",     "Pasos 7-14",  "Análisis y Contexto"),
            ("¿Cuándo?",  "Paso 15",     "Historia y Cronograma"),
            ("¿Dónde?",   "Pasos 16-18", "Ubicación y Acceso"),
            ("¿Cómo?",    "Pasos 19-23", "Diseño y Factibilidad"),
            ("¡Ejecutar!", "Pasos 24-26", "Marketing y Lanzamiento"),
        ],
    },

    "Nederlands": {
        "lang_code": "nl",
        "subtitle": "Bestemmingsgezondheidsindex · Planning Blauwdruk Mapper",
        "by": "Door Dr. Earney F. Lasten, Ph.D.",
        "framework_desc": (
            "*Het Lasten Bestemmingsintelligentiekader (LDIF) — "
            "een 11-dimensionaal diagnostisch systeem voor bestemmingsgezondheid, "
            "levenscycluspositionering en planningsinterventie, "
            "gecombineerd met het 26-stappen Planningsblauwdrukproces.*"
        ),
        "copyright": "© 2026 Dr. Earney F. Lasten, Ph.D. — Origineel kader.",
        "dest_label": "🏝️ Bestemming / Stad / Regio",
        "dest_placeholder": "bijv. Aruba, Amsterdam, Curaçao, Rotterdam...",
        "country_label": "🌍 Land / Gebied",
        "country_placeholder": "bijv. Aruba, Nederland, Curaçao...",
        "score_title": "### Scoor elke dimensie van 0 tot 100",
        "score_caption": "0 = Kritiek probleem · 50 = Heeft aandacht nodig · 100 = Uitstekend",
        "analyze_btn": "🔍 Analyseer Mijn Bestemming →",
        "error_msg": "⚠️ Voer een bestemmingsnaam en land in.",
        "saved_ok": "✅ Beoordeling opgeslagen",
        "saved_fail": "⚠️ Kon niet opslaan — resultaten worden getoond",
        "results_title": "## 📊 Resultaten —",
        "tab_health": "📈 Gezondheidsindex",
        "tab_stage": "🔄 Bestemmingsfase",
        "tab_blueprint": "🗺️ 26-Stappen Blauwdruk",
        "tab_action": "✅ Actieplan",
        "dhi_label": "Bestemmingsgezondheidsindex (DHI)",
        "stage_label": "Bestemmingsfase",
        "dim_scores": "#### Dimensiescores",
        "stage_means": "#### Wat betekent dit voor uw bestemming?",
        "all_stages": "#### Alle Bestemmingsfasen",
        "your_dest": "← Uw bestemming",
        "blueprint_title": "### 26-Stappen Planningsblauwdruk —",
        "blueprint_desc": "Op basis van uw 11-dimensiescores zijn deze planningsstappen nu van toepassing op uw bestemming.",
        "ready_cta": "🗺️ **Klaar om uit te voeren?** Werk alle 26 stappen interactief op [viamoon.com/flowchart](https://viamoon.com/flowchart) — met AI-begeleiding bij elke stap.",
        "urgent": "#### 🔴 Urgent — Direct Aanpakken",
        "important": "#### 🟡 Belangrijk — Dit Kwartaal Aanpakken",
        "no_urgent": "Geen urgente stappen — uw bestemming presteert goed.",
        "seven_q": "#### De 7 Hoofdvragen",
        "action_title": "### Actieplan —",
        "critical_dims": "#### Meest Kritieke Dimensies:",
        "no_critical": "🟢 Geen kritieke dimensies. Focus op het handhaven van sterke punten.",
        "next_steps": "#### Aanbevolen Volgende Stappen:",
        "step1": "1. Bekijk urgente blauwdrukstappen in het tabblad 26 Stappen",
        "step2": "2. Raadpleeg een gecertificeerde expert → [viamoon.com/network](https://viamoon.com/network)",
        "step3": "3. Plaats uw planningsproject → [viamoon.com/marketplace](https://viamoon.com/marketplace)",
        "step4": "4. Gebruik het volledige platform → [viamoon.com/flowchart](https://viamoon.com/flowchart)",
        "step5": "5. Lees The Experience Masterplan → [viamoon.com/textbook](https://viamoon.com/textbook)",
        "requires": "— vereist onmiddellijke interventie.",
        "welcome": "🌙 Welkom van lifecycle.viamoon.com — diepere analyse voor",
        "welcome2": ". Scoor alle 11 dimensies en klik op Analyseren.",
        "open": "Openen ↗",
        "healthy": "🟢 Gezond",
        "attention": "🟡 Heeft Aandacht Nodig",
        "critical": "🔴 Kritiek",
        "dim_labels": {
            "destination":   "🏝️ 1. Bestemmingskenmerken",
            "marketing":     "📣 2. Marketingreactie",
            "economic":      "💰 3. Economische Impacts",
            "social":        "👥 4. Sociale Impacts",
            "environmental": "🌿 5. Milieu-impacts",
            "housing_labor": "🏠 6. Woning & Arbeidsmarkt",
            "climate":       "🌡️ 7. Klimaat- en Hulpbronveerkracht",
            "cultural":      "🎭 8. Culturele Authenticiteit & Taal",
            "accessibility": "♿ 9. Toegankelijkheid & Inclusief Toerisme",
            "digital":       "📱 10. Digitale & Reputatiedynamiek",
            "governance":    "🏛️ 11. Bestuurscapaciteit",
        },
        "stages": {
            1: ("Verkenning", "Weinig bezoekers, geen formele infrastructuur. Bestemming grotendeels onbekend."),
            2: ("Betrokkenheid", "Lokale initiatieven komen op. Basisvoorzieningen in ontwikkeling."),
            3: ("Ontwikkeling", "Snelle groei. Investeringen stromen binnen. Infrastructuur breidt uit."),
            4: ("Consolidatie", "Groei vertraagt. Markt rijpt. Bestemming goed gevestigd."),
            5: ("Stagnatie", "Maximale capaciteit bereikt. Bezoekers op plateau. Milieu- en sociale druk."),
            6: ("Neergang", "Bezoekersaantallen dalen. Verlies van concurrentievermogen. Urgente interventie nodig."),
            7: ("Verjonging", "Actieve heruitvinding. Nieuwe producten, markten en infrastructuur."),
        },
        "interventions": {
            1: "Fundamentele planning nodig. Focus op Stappen 1-6 — stel missie, visie en stakeholderafstemming vast.",
            2: "Structureer de groei. Stappen 3-8 zijn kritiek — formaliseer stakeholdersbetrokkenheid en voer supply- en vraaganalyse uit.",
            3: "Beheer snelle ontwikkeling. Stappen 9-18 zijn urgent — beoordeel draagkracht en bescherm wat uw bestemming uniek maakt.",
            4: "Diversifieer en ververs. Stappen 6-8 en 24-26 zijn van toepassing — versterk uw marktbegrip en marketingstrategie.",
            5: "Urgente interventie vereist. Stappen 1-2 en 19-23 zijn kritiek — herdefinieer uw visie en herontwerp uw aanbod.",
            6: "Gedurfde actie nodig. Volledige 26-stappen herplanning aanbevolen. Begin opnieuw bij Stap 1.",
            7: "Houd het momentum vast. Stappen 19-26 zijn van toepassing — bevestig ontwerpinnovaties en voer uw herlanseringsstrategie uit.",
        },
        "questions": [
            ("Waarom?",   "Stappen 1-2",   "Missie & Visie"),
            ("Wie?",      "Stappen 3-6",   "Stakeholders & Markt"),
            ("Wat?",      "Stappen 7-14",  "Analyse & Context"),
            ("Wanneer?",  "Stap 15",       "Verhaal & Tijdlijn"),
            ("Waar?",     "Stappen 16-18", "Locatie & Toegang"),
            ("Hoe?",      "Stappen 19-23", "Ontwerp & Haalbaarheid"),
            ("Uitvoeren!", "Stappen 24-26", "Marketing & Lancering"),
        ],
    },

    "Papiamento": {
        "lang_code": "pap",
        "subtitle": "Indice di Salud di Destino · Mapeador di Plan di Desaroyo",
        "by": "Pa Dr. Earney F. Lasten, Ph.D.",
        "framework_desc": (
            "*E Marco di Inteligencia di Destino Lasten (LDIF) — "
            "un sistema diagnostico di 11 dimension pa salud di destino, "
            "posicionamento den ciclo di bida i intervencion di planificacion, "
            "kombiná ku e Proceso di 26 Paso di Planning Blueprint.*"
        ),
        "copyright": "© 2026 Dr. Earney F. Lasten, Ph.D. — Marco original.",
        "dest_label": "🏝️ Destino / Ciudad / Region",
        "dest_placeholder": "p.e. Aruba, San Nicolas, Oranjestad...",
        "country_label": "🌍 Pais / Territorio",
        "country_placeholder": "p.e. Aruba, Kòrsou, Hulanda...",
        "score_title": "### Puntuá kada dimension di 0 te 100",
        "score_caption": "0 = Problema kritiko · 50 = Mester atencion · 100 = Excelente",
        "analyze_btn": "🔍 Analisa Mi Destino →",
        "error_msg": "⚠️ Por fabor pone nòmber di destino i pais.",
        "saved_ok": "✅ Evaluacion a wordo guarda",
        "saved_fail": "⚠️ No por a guarda — resultadonan ta mustra",
        "results_title": "## 📊 Resultadonan —",
        "tab_health": "📈 Indice di Salud",
        "tab_stage": "🔄 Fase di Destino",
        "tab_blueprint": "🗺️ Plan di 26 Paso",
        "tab_action": "✅ Plan di Akshon",
        "dhi_label": "Indice di Salud di Destino (DHI)",
        "stage_label": "Fase di Destino",
        "dim_scores": "#### Puntuacionnan pa Dimension",
        "stage_means": "#### Kiko e ta nifica pa bo destino?",
        "all_stages": "#### Tur Fasenan di Destino",
        "your_dest": "← Bo destino",
        "blueprint_title": "### Plan di Desaroyo di 26 Paso —",
        "blueprint_desc": "Basá riba bo puntuacionnan di 11 dimension, e pasonan aki di planificacion ta aplikabel na bo destino awor.",
        "ready_cta": "🗺️ **Listo pa ehekutá?** Traha tur 26 paso na [viamoon.com/flowchart](https://viamoon.com/flowchart) — ku guia di AI na kada paso.",
        "urgent": "#### 🔴 Urgente — Trata Inmediatamente",
        "important": "#### 🟡 Importante — Trata E Trimester Aki",
        "no_urgent": "No tin pasonan urgente — bo destino ta funshonando bon.",
        "seven_q": "#### E 7 Preguntanan Principal",
        "action_title": "### Plan di Akshon —",
        "critical_dims": "#### Dimensionnan Mas Kritiko:",
        "no_critical": "🟢 No tin dimensionnan kritiko. Enfokate riba mantene fortalezanan.",
        "next_steps": "#### Próximo Pasonan Rekomendá:",
        "step1": "1. Revisa pasonan urgente den e tab di 26 Paso",
        "step2": "2. Kontakta un experto sertifiká → [viamoon.com/network](https://viamoon.com/network)",
        "step3": "3. Pone bo proyekto → [viamoon.com/marketplace](https://viamoon.com/marketplace)",
        "step4": "4. Usa e plataforma kumpleto → [viamoon.com/flowchart](https://viamoon.com/flowchart)",
        "step5": "5. Lesa The Experience Masterplan → [viamoon.com/textbook](https://viamoon.com/textbook)",
        "requires": "— ta rekeri intervencion inmediato.",
        "welcome": "🌙 Bon bini di lifecycle.viamoon.com — kontinuando bo analisis pa",
        "welcome2": ". Puntuá tur 11 dimension i klik Analisa.",
        "open": "Habri ↗",
        "healthy": "🟢 Saludabel",
        "attention": "🟡 Mester Atencion",
        "critical": "🔴 Kritiko",
        "dim_labels": {
            "destination":   "🏝️ 1. Karakteristikanan di Destino",
            "marketing":     "📣 2. Respuesta di Marketing",
            "economic":      "💰 3. Impaktonan Ekonómiko",
            "social":        "👥 4. Impaktonan Sosial",
            "environmental": "🌿 5. Impaktonan Ambiental",
            "housing_labor": "🏠 6. Biba i Asequibilidad Laboral",
            "climate":       "🌡️ 7. Resiliencia Klimatiko i di Rekurso",
            "cultural":      "🎭 8. Autentisidad Kultural i Idioma",
            "accessibility": "♿ 9. Aksesibilidad i Turismo Inklusivo",
            "digital":       "📱 10. Dinamika Digital i Reputacion",
            "governance":    "🏛️ 11. Kapasidad di Gobernansa",
        },
        "stages": {
            1: ("Exploracion", "Poko bisitantenan, sin infraestruktira formal. Destino mayoria deskonosí."),
            2: ("Involukracion", "Inisiativanan lokal ta surgi. Fasilidadnan básiko ta desaroyando."),
            3: ("Desaroyo", "Kresimento rapido. Inversion ta yega. Infraestruktira ta expande."),
            4: ("Konsolidacion", "Kresimento ta desaselerá. Merkado ta madura. Destino bon establesí."),
            5: ("Estankamento", "Kapasidad maksimo a yega. Bisitantenan na plateau. Stres ambiental i sosial."),
            6: ("Desendencia", "Bisitantenan ta baha. Perdiendo kompetitividad. Intervencion urgente nesario."),
            7: ("Rihuvenisencion", "Reinvencion aktivo. Produktonan nobo, merkado nobo, infraestruktira nobo."),
        },
        "interventions": {
            1: "Planificacion fundamental ta nesario. Enfokate riba Pasonan 1-6 — establesé mision, vision i alineacion di stakeholder.",
            2: "Estruturá e kresimento. Pasonan 3-8 ta kritiko — formalisá involukracion di stakeholder i hasi analisis di oferta i demanda.",
            3: "Maneha desaroyo rapido. Pasonan 9-18 ta urgente — evaluá kapasidad di karga i protehá loke ta hasi bo destino unico.",
            4: "Diversifiká i refreskká. Pasonan 6-8 i 24-26 ta aplikabel — fortalesé bo komprencion di merkado i estrategia di marketing.",
            5: "Intervencion urgente ta rekeri. Pasonan 1-2 i 19-23 ta kritiko — redefini bo vision i rediseña bo oferta.",
            6: "Akshon audas ta nesario. Replanificacion kumpleto di 26 paso rekomendá. Kuminsa for di Paso 1.",
            7: "Mantené e impulso. Pasonan 19-26 ta aplikabel — konsolida innovacionnan di diseño i ehekutá bo estrategia di relansamento.",
        },
        "questions": [
            ("Pakiko?",    "Pasonan 1-2",   "Mision i Vision"),
            ("Kende?",     "Pasonan 3-6",   "Stakeholdernan"),
            ("Kiko?",      "Pasonan 7-14",  "Analisis i Konteksto"),
            ("Kora?",      "Paso 15",       "Historia i Cronograma"),
            ("Unda?",      "Pasonan 16-18", "Lokacion i Akes"),
            ("Kon?",       "Pasonan 19-23", "Diseño i Faisabilidad"),
            ("Ehekutá!",   "Pasonan 24-26", "Marketing i Lansamento"),
        ],
    },
}

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
    "economic": 0.12,    "social": 0.10,
    "environmental": 0.10, "housing_labor": 0.09,
    "climate": 0.09,     "cultural": 0.09,
    "accessibility": 0.08, "digital": 0.07,
    "governance": 0.08,
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

# ── Language selector ─────────────────────

lang_choice = st.sidebar.selectbox(
    "🌐 Language / Idioma / Taal / Idioma",
    ["English", "Español", "Nederlands", "Papiamento"],
    index=0,
)
T = TRANSLATIONS[lang_choice]

# ── Header ────────────────────────────────

col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image(
        "https://viamoon.com/viamoon-logo.png",
        width=180,
    )
with col_title:
    st.title("🌙 PlanningMind")
    st.subheader(T["subtitle"])
    st.markdown(f"**{T['by']} · [viamoon.com](https://viamoon.com)**")

st.markdown(T["framework_desc"])
st.markdown(f"*{T['copyright']}*")
st.divider()

# ── URL params ────────────────────────────

params = st.query_params
prefill_dest = params.get("destination", "")
prefill_country = params.get("country", "")

if prefill_dest:
    st.success(
        f"{T['welcome']} **{prefill_dest}**{T['welcome2']}"
    )

# ── Inputs ────────────────────────────────

col1, col2 = st.columns(2)
with col1:
    destination = st.text_input(
        T["dest_label"],
        value=prefill_dest,
        placeholder=T["dest_placeholder"],
    )
with col2:
    country = st.text_input(
        T["country_label"],
        value=prefill_country,
        placeholder=T["country_placeholder"],
    )

st.markdown(T["score_title"])
st.caption(T["score_caption"])

# ── Sliders ───────────────────────────────

scores = {}
col_a, col_b = st.columns(2)

# ── Dimension help text ───────────────────
DIM_HELP = {
    "destination": (
        "Score the overall development stage and "
        "physical readiness of the destination. "
        "Consider: lifecycle stage (exploration to "
        "rejuvenation), quality of roads, airports "
        "and utilities, diversity of accommodation, "
        "condition of core attractions, and "
        "transportation connectivity. "
        "Low = underdeveloped or deteriorating. "
        "High = well-developed, diverse, connected."
    ),
    "marketing": (
        "Score how effectively the destination "
        "attracts and retains the right visitors. "
        "Consider: visitor growth trend (last 3 "
        "years), percentage of repeat visitors, "
        "average length of stay, visitor "
        "satisfaction scores, and the strength "
        "and clarity of the destination brand. "
        "Low = declining visitors, weak brand. "
        "High = growing, loyal, satisfied visitors."
    ),
    "economic": (
        "Score the economic health and fairness "
        "of tourism's contribution. Consider: "
        "tourism share of local GDP and jobs, "
        "how much revenue stays local vs leaks "
        "to foreign companies, local ownership "
        "of tourism businesses, and diversity "
        "of the tourism economy beyond hotels "
        "and restaurants. "
        "Low = high leakage, low local benefit. "
        "High = strong local economic participation."
    ),
    "social": (
        "Score the relationship between tourism "
        "and the local community. Consider: "
        "resident attitudes toward tourism "
        "(welcoming to hostile), crime rates "
        "linked to tourism, displacement of "
        "local residents from their neighborhoods, "
        "and whether locals participate in "
        "tourism planning decisions. "
        "Low = community hostility, displacement. "
        "High = community support and participation."
    ),
    "environmental": (
        "Score the ecological condition of the "
        "destination. Consider: pressure on "
        "biodiversity from visitor activity, "
        "water and air pollution in tourism "
        "zones, waste management capacity vs "
        "peak visitor load, integrity of "
        "protected areas, and investment in "
        "environmental management. "
        "Low = severe environmental degradation. "
        "High = well-protected natural environment."
    ),
    "housing_labor": (
        "Score whether local people can afford "
        "to live and work in the destination. "
        "Consider: ratio of housing costs to "
        "local wages, proportion of housing "
        "converted to short-term tourist rentals, "
        "availability of affordable worker "
        "housing, and whether the tourism "
        "workforce is stable or constantly "
        "leaving. "
        "Low = workers cannot afford to live "
        "locally, chronic staffing crisis. "
        "High = affordable, stable workforce."
    ),
    "climate": (
        "Score the destination's readiness for "
        "climate change and resource pressures. "
        "Consider: vulnerability to sea level "
        "rise, hurricanes, drought or flooding, "
        "security of freshwater supply, "
        "reliability of energy systems, "
        "emergency preparedness, dependence "
        "on a single tourist season, and "
        "carbon footprint per visitor. "
        "Low = highly vulnerable, unprepared. "
        "High = resilient, diverse, prepared."
    ),
    "cultural": (
        "Score the health of local culture and "
        "language in the context of tourism. "
        "Consider: vitality of local languages "
        "(are children still learning them?), "
        "continuity of traditional practices "
        "and crafts, whether cultural events "
        "serve locals or only tourists, and "
        "the integrity of heritage sites. "
        "Low = language dying, culture staged "
        "only for tourists, heritage eroding. "
        "High = living culture, genuine "
        "heritage, thriving local identity."
    ),
    "accessibility": (
        "Score how accessible the destination "
        "is to all types of visitors. Consider: "
        "physical accessibility for visitors "
        "with mobility, sensory or cognitive "
        "disabilities, economic accessibility "
        "(can visitors of different income "
        "levels afford to visit?), digital "
        "accessibility of tourism platforms, "
        "and availability of information in "
        "multiple languages. "
        "Low = excludes many visitor groups. "
        "High = welcoming and accessible to all."
    ),
    "digital": (
        "Score the destination's digital health "
        "and online reputation. Consider: overall "
        "sentiment of online reviews (TripAdvisor, "
        "Google, social media), whether reviews "
        "are improving or declining, dependence "
        "on a small number of booking platforms, "
        "and the destination's capacity to "
        "respond effectively to reputation crises. "
        "Low = poor reviews, high platform "
        "dependency, no crisis capacity. "
        "High = strong positive reputation, "
        "diversified digital channels."
    ),
    "governance": (
        "Score the institutional capacity to "
        "plan and manage tourism effectively. "
        "Consider: coordination between "
        "government agencies responsible for "
        "tourism, whether planning rules are "
        "actually enforced, stability of "
        "funding for destination management, "
        "meaningful inclusion of communities "
        "in decisions, and the ability of "
        "institutions to adapt quickly to "
        "changing conditions. "
        "Low = fragmented agencies, weak "
        "enforcement, no community voice. "
        "High = coherent policy, strong "
        "institutions, community-driven planning."
    ),
}

# ── Expandable scoring guide ──────────────
with st.expander("📖 Scoring Guide — what does each dimension mean?"):
    for dim, label in T["dim_labels"].items():
        st.markdown(f"**{label}**")
        st.caption(DIM_HELP[dim])
        st.markdown("---")

# ── Sliders with tooltips ─────────────────
col_a, col_b = st.columns(2)

with col_a:
    scores["destination"] = st.slider(
        T["dim_labels"]["destination"],
        0, 100, 50, 5,
        help=DIM_HELP["destination"]
    )
    scores["marketing"] = st.slider(
        T["dim_labels"]["marketing"],
        0, 100, 50, 5,
        help=DIM_HELP["marketing"]
    )
    scores["economic"] = st.slider(
        T["dim_labels"]["economic"],
        0, 100, 50, 5,
        help=DIM_HELP["economic"]
    )
    scores["social"] = st.slider(
        T["dim_labels"]["social"],
        0, 100, 50, 5,
        help=DIM_HELP["social"]
    )
    scores["environmental"] = st.slider(
        T["dim_labels"]["environmental"],
        0, 100, 50, 5,
        help=DIM_HELP["environmental"]
    )
    scores["housing_labor"] = st.slider(
        T["dim_labels"]["housing_labor"],
        0, 100, 50, 5,
        help=DIM_HELP["housing_labor"]
    )

with col_b:
    scores["climate"] = st.slider(
        T["dim_labels"]["climate"],
        0, 100, 50, 5,
        help=DIM_HELP["climate"]
    )
    scores["cultural"] = st.slider(
        T["dim_labels"]["cultural"],
        0, 100, 50, 5,
        help=DIM_HELP["cultural"]
    )
    scores["accessibility"] = st.slider(
        T["dim_labels"]["accessibility"],
        0, 100, 50, 5,
        help=DIM_HELP["accessibility"]
    )
    scores["digital"] = st.slider(
        T["dim_labels"]["digital"],
        0, 100, 50, 5,
        help=DIM_HELP["digital"]
    )
    scores["governance"] = st.slider(
        T["dim_labels"]["governance"],
        0, 100, 50, 5,
        help=DIM_HELP["governance"]
    )

st.divider()

# ── Analyze ───────────────────────────────

if st.button(T["analyze_btn"], type="primary", use_container_width=True):
    if not destination or not country:
        st.error(T["error_msg"])
    else:
        dhi = round(sum(scores[k] * WEIGHTS[k] for k in WEIGHTS), 1)
        dhi_label = (
            T["healthy"] if dhi >= 65
            else T["attention"] if dhi >= 40
            else T["critical"]
        )
        stage_num = get_stage(dhi)
        stage_name, stage_desc = T["stages"][stage_num]
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
            st.toast(T["saved_ok"], icon="🌙")
        else:
            st.toast(T["saved_fail"])

        st.markdown(f"{T['results_title']} {destination}, {country}")

        tab1, tab2, tab3, tab4 = st.tabs([
            T["tab_health"],
            T["tab_stage"],
            T["tab_blueprint"],
            T["tab_action"],
        ])

        with tab1:
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.metric(T["dhi_label"], f"{dhi}/100", dhi_label)
            with col_m2:
                st.metric(T["stage_label"], f"Stage {stage_num}", stage_name)
            st.progress(dhi / 100)
            st.markdown(T["dim_scores"])
            for dim, label in T["dim_labels"].items():
                score = scores[dim]
                icon = "🟢" if score >= 65 else "🟡" if score >= 40 else "🔴"
                c1, c2 = st.columns([5, 1])
                with c1:
                    st.progress(score / 100, text=label)
                with c2:
                    st.markdown(f"{icon} **{score}**")
            st.caption(
                "Lasten Destination Intelligence Framework (LDIF) · "
                "© 2026 Dr. Earney F. Lasten, Ph.D."
            )

        with tab2:
            st.markdown(f"### Stage {stage_num}: **{stage_name}**")
            st.info(stage_desc)
            st.markdown(T["stage_means"])
            st.write(T["interventions"][stage_num])
            st.markdown(T["all_stages"])
            for num, (name, _) in T["stages"].items():
                if num == stage_num:
                    st.markdown(f"**▶ Stage {num}: {name}** {T['your_dest']}")
                else:
                    st.markdown(f"Stage {num}: {name}")
            st.caption(
                "Lasten Destination Intelligence Framework (LDIF) · "
                "© 2026 Dr. Earney F. Lasten, Ph.D."
            )

        with tab3:
            st.markdown(f"{T['blueprint_title']} {destination}")
            st.markdown(T["blueprint_desc"])
            st.info(T["ready_cta"])
            if urgent_steps:
                st.markdown(T["urgent"])
                for s in urgent_steps:
                    col_step, col_link = st.columns([6, 1])
                    with col_step:
                        st.markdown(f"**Step {s}** — {BLUEPRINT_STEPS[s]}")
                    with col_link:
                        st.markdown(f"[{T['open']}](https://viamoon.com/flowchart)")
            else:
                st.success(T["no_urgent"])
            if important_steps:
                st.markdown(T["important"])
                for s in important_steps:
                    col_step, col_link = st.columns([6, 1])
                    with col_step:
                        st.markdown(f"Step {s} — {BLUEPRINT_STEPS[s]}")
                    with col_link:
                        st.markdown(f"[{T['open']}](https://viamoon.com/flowchart)")
            st.markdown(T["seven_q"])
            for q, steps, desc in T["questions"]:
                st.markdown(f"**{q}** · {steps} · {desc}")
            st.caption(
                "26-step Planning Blueprint Process · "
                "© 2026 Dr. Earney F. Lasten, Ph.D."
            )

        with tab4:
            st.markdown(f"{T['action_title']} {destination}")
            critical = [(k, v) for k, v in scores.items() if v < 40]
            critical.sort(key=lambda x: x[1])
            if critical:
                st.markdown(T["critical_dims"])
                for dim, score in critical[:3]:
                    st.error(
                        f"🔴 **{T['dim_labels'][dim]}** — "
                        f"scored {score}/100 {T['requires']}"
                    )
            else:
                st.success(T["no_critical"])
            st.markdown(T["next_steps"])
            st.markdown(T["step1"])
            st.markdown(T["step2"])
            st.markdown(T["step3"])
            st.markdown(T["step4"])
            st.markdown(T["step5"])
            st.divider()
            st.caption(
                "PlanningMind · Lasten Destination Intelligence Framework (LDIF) · "
                "26-step Planning Blueprint Process · "
                "© 2026 Dr. Earney F. Lasten, Ph.D. · "
                "VIAMOON Consultancy (Aruba) · VIAMOON SAS (Colombia) · "
                "viamoon.com"
            )
