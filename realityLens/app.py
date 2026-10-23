
import streamlit as st
import pandas as pd
from collections import Counter
from datetime import date
import json
import urllib.request
import urllib.error

# =========================================================
# FACT CHECK ✓ WITH REALITYLENSAI
# Andhra Pradesh hotels, restaurants & residential projects
# =========================================================

st.set_page_config(
    page_title="FACT CHECK | RealityLensAI",
    page_icon="✓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- PROFESSIONAL LIGHT THEME --------------------

st.markdown("""
<style>
/* ===== GLOBAL LIGHT THEME ===== */
:root {
    color-scheme: light !important;
}

html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stHeader"],
[data-testid="stBottom"],
[data-testid="stVerticalBlock"],
[data-testid="stHorizontalBlock"] {
    background-color: #F4F8F6 !important;
    color: #20332C !important;
}

/* Main page */
[data-testid="stMainBlockContainer"] {
    padding-top: 1.5rem !important;
}

/* All ordinary text */
.stApp, .stApp p, .stApp span,
.stApp label, .stApp li, .stApp small,
.stApp strong, .stApp div,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {
    color: #20332C;
}

/* Headings */
h1, h2, h3, h4, h5, h6,
.stApp h1, .stApp h2, .stApp h3 {
    color: #153F32 !important;
    font-weight: 750 !important;
}

/* Inputs, dropdowns and selected values */
.stApp input, .stApp textarea,
.stApp select,
[data-baseweb="select"],
[data-baseweb="select"] *,
[data-baseweb="input"],
[data-baseweb="input"] *,
[data-baseweb="textarea"],
[data-baseweb="textarea"] *,
[data-baseweb="tag"] {
    background-color: #FFFFFF !important;
    color: #20332C !important;
    -webkit-text-fill-color: #20332C !important;
    border-color: #B8CEC3 !important;
}

/* Dropdown popup options */
[data-baseweb="popover"],
[data-baseweb="popover"] *,
[role="listbox"],
[role="option"] {
    color: #20332C !important;
}

[role="option"] {
    background-color: #FFFFFF !important;
}

[role="option"]:hover {
    background-color: #E2F1E9 !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background-color: #E8F1EC !important;
    border-radius: 12px !important;
    gap: 6px !important;
}

.stTabs [data-baseweb="tab"] {
    background-color: transparent !important;
    color: #29483A !important;
    border-radius: 8px !important;
}

.stTabs [data-baseweb="tab"] *,
.stTabs button p {
    color: #29483A !important;
    -webkit-text-fill-color: #29483A !important;
}

.stTabs [aria-selected="true"] {
    background-color: #FFFFFF !important;
    border-bottom: 3px solid #25845B !important;
}

.stTabs [aria-selected="true"] *,
.stTabs [aria-selected="true"] p {
    color: #146B46 !important;
    -webkit-text-fill-color: #146B46 !important;
    font-weight: 700 !important;
}

/* Buttons */
.stApp .stButton > button,
.stApp button[kind="primary"],
.stApp button[kind="secondary"],
.stApp [data-testid="stDownloadButton"] button {
    background-color: #E1F0E7 !important;
    color: #164B35 !important;
    border: 1px solid #91BDA5 !important;
    border-radius: 9px !important;
    font-weight: 650 !important;
}

.stApp .stButton > button *,
.stApp button[kind="primary"] *,
.stApp button[kind="secondary"] *,
.stApp [data-testid="stDownloadButton"] button * {
    color: #164B35 !important;
    -webkit-text-fill-color: #164B35 !important;
}

.stApp .stButton > button:hover,
.stApp [data-testid="stDownloadButton"] button:hover {
    background-color: #CDE7D7 !important;
    border-color: #25845B !important;
}

/* Cards and bordered sections */
[data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stExpander"],
[data-testid="stMetric"],
[data-testid="stAlert"],
.stApp [data-testid="stDataFrame"],
.stApp [data-testid="stTable"] {
    background-color: #FFFFFF !important;
    border-color: #D4E3DA !important;
    border-radius: 12px !important;
    color: #20332C !important;
}

/* Metrics */
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] *,
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] *,
[data-testid="stMetricDelta"],
[data-testid="stMetricDelta"] * {
    color: #20332C !important;
    -webkit-text-fill-color: #20332C !important;
}

/* Tables */
.stApp table {
    background-color: #FFFFFF !important;
    color: #20332C !important;
    border-collapse: collapse !important;
}

.stApp th {
    background-color: #E4F0E8 !important;
    color: #153F32 !important;
    font-weight: 700 !important;
}

.stApp td {
    background-color: #FFFFFF !important;
    color: #20332C !important;
}

.stApp th, .stApp td {
    border-color: #D4E3DA !important;
}

/* Expanders */
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary * {
    color: #20332C !important;
}

/* Sidebar */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div {
    background-color: #EAF3ED !important;
}

[data-testid="stSidebar"] *,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #20332C !important;
}

/* Links */
.stApp a {
    color: #176D4A !important;
    text-decoration: underline;
}

/* Checkbox and radio labels */
.stApp [data-testid="stCheckbox"] *,
.stApp [data-testid="stRadio"] * {
    color: #20332C !important;
}

/* Progress bars and sliders */
.stApp [data-testid="stProgress"] > div {
    background-color: #DCE9E0 !important;
}

.stApp [data-testid="stProgress"] [role="progressbar"] {
    background-color: #25845B !important;
}

/* Captions and help text */
.stApp .stCaption,
.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stCaptionContainer"] * {
    color: #526A5E !important;
}

/* Keep text readable when disabled */
.stApp input:disabled,
.stApp textarea:disabled {
    color: #526A5E !important;
    -webkit-text-fill-color: #526A5E !important;
    opacity: 1 !important;
}

/* Hide Streamlit's default top decoration */
[data-testid="stDecoration"] {
    background-image: none !important;
    background-color: #F4F8F6 !important;
}

/* Consistent clean page finish */
hr {
    border-color: #D4E3DA !important;
}

/* Centered, professional prototype title */
.hero {
    background: linear-gradient(135deg, #E4F2E9 0%, #FFFFFF 52%, #E8F1FA 100%);
    border: 1px solid #BFD8C9;
    border-radius: 18px;
    padding: 30px 24px 24px;
    margin: 0 auto 24px auto;
    text-align: center;
    box-shadow: 0 8px 24px rgba(25, 65, 47, 0.08);
}
.hero-title {
    color: #123B2C !important;
    font-size: clamp(2rem, 4vw, 3.1rem);
    line-height: 1.15;
    font-weight: 900;
    letter-spacing: 0.5px;
    text-align: center;
}
.hero-subtitle {
    color: #1B5B41 !important;
    font-size: clamp(1.1rem, 2vw, 1.55rem);
    font-weight: 800;
    letter-spacing: 2px;
    text-align: center;
    margin-top: 7px;
}
.hero-caption {
    color: #334D41 !important;
    font-size: 1rem;
    font-weight: 550;
    text-align: center;
    margin-top: 13px;
}

/* Strong, high-contrast analysis headings and perspective expanders */
.stApp h1, .stApp h2, .stApp h3, .stApp h4 {
    color: #123B2C !important;
    font-weight: 850 !important;
}
[data-testid="stExpander"] {
    border: 1px solid #BFD8C9 !important;
    background: #FFFFFF !important;
    overflow: hidden;
}
[data-testid="stExpander"] summary {
    background: #E4F2E9 !important;
    padding: 12px 14px !important;
    border-radius: 10px !important;
    color: #123B2C !important;
    font-weight: 800 !important;
}
[data-testid="stExpander"] summary span,
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary div,
[data-testid="stExpander"] summary svg {
    color: #123B2C !important;
    fill: #123B2C !important;
    -webkit-text-fill-color: #123B2C !important;
    font-weight: 800 !important;
}
[data-testid="stExpander"] summary:hover {
    background: #D4E9DC !important;
}
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    padding-bottom: 6px;
    border-bottom: 1px solid #D4E3DA;
}
</style>
""", unsafe_allow_html=True)

# -------------------- PLACE CATALOGUE --------------------
# IMPORTANT: Review text is illustrative demo text, not real reviews.
# Verify current project details with official sources.

places = {
    "Novotel Visakhapatnam Varun Beach": {
        "category": "Hotel",
        "city": "Visakhapatnam",
        "price": "Premium",
        "source": "https://all.accor.com/",
        "description": "Seafront hotel in Visakhapatnam.",
        "reviews": [
            ("Family", "Breakfast queues felt long during peak hours.", 3),
            ("Professional", "The stay felt expensive for the overall value.", 3),
            ("Student", "Wi-Fi speed could be more consistent.", 3),
            ("Family", "Check-in took longer than expected.", 3),
        ],
    },
    "The Park Visakhapatnam": {
        "category": "Hotel",
        "city": "Visakhapatnam",
        "price": "Premium",
        "source": "https://www.theparkhotels.com/",
        "description": "Beachside hotel in Visakhapatnam.",
        "reviews": [
            ("Family", "Some facilities seemed due for maintenance.", 3),
            ("Professional", "The restaurant bill was higher than expected.", 3),
            ("Student", "Some areas felt crowded in the evening.", 3),
            ("Family", "Response time for a request could improve.", 3),
        ],
    },
    "Vivanta Vijayawada, MG Road": {
        "category": "Hotel",
        "city": "Vijayawada",
        "price": "Premium",
        "source": "https://www.vivantahotels.com/",
        "description": "Hotel located on MG Road, Vijayawada.",
        "reviews": [
            ("Professional", "The stay was expensive for a short business trip.", 3),
            ("Family", "Waiting time increased at breakfast.", 3),
            ("Student", "Extra charges should be explained more clearly.", 3),
            ("Family", "Parking guidance could be clearer at busy times.", 3),
        ],
    },
    "Fortune Select Grand Ridge": {
        "category": "Hotel",
        "city": "Tirupati",
        "price": "Premium",
        "source": "https://www.fortunehotels.in/",
        "description": "Hotel option in Tirupati.",
        "reviews": [
            ("Family", "Check-in waiting time was longer than expected.", 3),
            ("Senior traveller", "Directions to facilities could be clearer.", 3),
            ("Professional", "Some menu items seemed overpriced.", 3),
            ("Family", "The dining area became crowded.", 3),
        ],
    },
    "Subbayya Gari Hotel, Vijayawada": {
        "category": "Restaurant",
        "city": "Vijayawada",
        "price": "Mid-range",
        "source": "https://www.google.com/search?q=Subbayya+Gari+Hotel+Vijayawada",
        "description": "Andhra-style meals restaurant listing.",
        "reviews": [
            ("Family", "The dining area felt crowded at lunch.", 3),
            ("Student", "The price felt high for my budget.", 3),
            ("Professional", "Getting the bill took extra time.", 3),
            ("Family", "Seating could be better organised.", 3),
        ],
    },
    "Rayalaseema Ruchulu, Vijayawada": {
        "category": "Restaurant",
        "city": "Vijayawada",
        "price": "Mid-range",
        "source": "https://www.google.com/search?q=Rayalaseema+Ruchulu+Vijayawada",
        "description": "Andhra cuisine restaurant listing.",
        "reviews": [
            ("Student", "Some dishes were too expensive for a student budget.", 3),
            ("Family", "Waiting time increased at dinner.", 3),
            ("Professional", "Allergen details could be clearer on the menu.", 3),
            ("Family", "Service slowed when the restaurant was crowded.", 3),
        ],
    },
    "Dharani Restaurant, Visakhapatnam": {
        "category": "Restaurant",
        "city": "Visakhapatnam",
        "price": "Mid-range",
        "source": "https://www.google.com/search?q=Dharani+Restaurant+Visakhapatnam",
        "description": "Vegetarian dining option listing in Visakhapatnam.",
        "reviews": [
            ("Family", "The queue was long at peak time.", 3),
            ("Student", "Portion sizes could be clearer on the menu.", 3),
            ("Professional", "Service was slower than expected.", 3),
            ("Family", "The waiting area felt crowded.", 3),
        ],
    },
    "MK One, Yendada, Visakhapatnam": {
        "category": "Apartment / House",
        "city": "Visakhapatnam",
        "price": "Check with developer",
        "source": "https://mkone.in/",
        "description": "Residential project listing. Verify current availability, approvals, possession terms and pricing.",
        "reviews": [
            ("Homebuyer", "Confirm the handover timeline in writing.", 3),
            ("Family", "Check traffic and travel times during a site visit.", 3),
            ("Professional", "Request a breakdown of maintenance and recurring costs.", 3),
            ("Homebuyer", "Inspect construction progress and verify the approved plan.", 2),
        ],
    },
    "MVV GV The Grand, Visakhapatnam": {
        "category": "Apartment / House",
        "city": "Visakhapatnam",
        "price": "Check with developer",
        "source": "https://mvvgvthegrand.in/",
        "description": "Residential project listing. Independently check its current status, approvals and possession terms.",
        "reviews": [
            ("Homebuyer", "Monthly maintenance and utility costs need confirmation.", 3),
            ("Family", "Visit the site to assess road access and nearby services.", 3),
            ("Professional", "Check the carpet area and possession terms in the agreement.", 2),
            ("Homebuyer", "Verify the latest construction update and RERA details.", 3),
        ],
    },
    "Celest Apartments, Visakhapatnam": {
        "category": "Apartment / House",
        "city": "Visakhapatnam",
        "price": "Check current listing",
        "source": "https://apartments.thecelest.com/",
        "description": "Apartment project listing. Confirm inventory, pricing and approvals directly.",
        "reviews": [
            ("Homebuyer", "Confirm the final price including registration and parking.", 3),
            ("Family", "Check lifts, water supply and parking during a site visit.", 3),
            ("Professional", "Request approved plans and written possession terms.", 2),
            ("Homebuyer", "Inspect the amenities instead of relying only on brochures.", 3),
        ],
    },
    "Olympia, Poranki, Vijayawada": {
        "category": "Apartment / House",
        "city": "Vijayawada",
        "price": "Check with developer",
        "source": "https://vasishtainfra.com/olympia-copy/",
        "description": "Residential project listing in the Vijayawada area. Verify current status and registration.",
        "reviews": [
            ("Homebuyer", "Confirm the carpet area and all additional charges.", 3),
            ("Family", "Check commute time and road access during peak hours.", 3),
            ("Professional", "Review completion dates and delay clauses.", 2),
            ("Homebuyer", "Verify project registration and construction progress.", 3),
        ],
    },
    "INS Kurusura Submarine Museum, Visakhapatnam": {
        "category": "Museum",
        "city": "Visakhapatnam",
        "price": "Check current entry fee",
        "source": "https://www.incredibleindia.gov.in/",
        "description": "Submarine museum attraction on the Visakhapatnam coast. Confirm opening hours, access and current ticket details before visiting.",
        "reviews": [
            ("Family", "The submarine display was memorable for our family.", 5),
            ("Student", "The exhibits were interesting, but crowding made some areas difficult to view.", 3),
            ("Senior traveller", "More seating and clearer visitor guidance would help.", 2),
            ("Student", "The visit was educational and worth the time.", 4),
        ],
    },
    "Amaravati Archaeological Museum, Amaravati": {
        "category": "Museum",
        "city": "Amaravati",
        "price": "Check current entry fee",
        "source": "https://asi.nic.in/",
        "description": "Museum associated with the archaeological heritage of Amaravati. Verify current access and exhibits with official sources.",
        "reviews": [
            ("Student", "The historical displays helped me understand the site better.", 5),
            ("Family", "Signboards could be easier to follow throughout the visit.", 3),
            ("Professional", "I wanted more detailed explanations beside some exhibits.", 3),
            ("Senior traveller", "The visit was calm and informative.", 4),
        ],
    },
    "Indira Gandhi Zoological Park, Visakhapatnam": {
        "category": "Park",
        "city": "Visakhapatnam",
        "price": "Check current entry fee",
        "source": "https://www.incredibleindia.gov.in/",
        "description": "Large zoological park in Visakhapatnam. Confirm opening hours, animal-viewing conditions and visitor rules before travelling.",
        "reviews": [
            ("Family", "The children enjoyed the long walk and seeing the animals.", 5),
            ("Student", "Some animal enclosures were not easy to see during our visit.", 3),
            ("Senior traveller", "More shaded resting places would make the visit easier.", 2),
            ("Family", "The outing was enjoyable and gave us plenty to explore.", 4),
        ],
    },
    "Kailasagiri, Visakhapatnam": {
        "category": "Park",
        "city": "Visakhapatnam",
        "price": "Check current entry/transport fee",
        "source": "https://www.incredibleindia.gov.in/",
        "description": "Hilltop public recreation destination with views over Visakhapatnam. Check current transport options, fees and weather conditions.",
        "reviews": [
            ("Family", "The views were beautiful and the children enjoyed the outing.", 5),
            ("Student", "It became crowded near popular viewpoints.", 3),
            ("Senior traveller", "Clearer directions and more benches would be useful.", 2),
            ("Professional", "The visit was relaxing and convenient for a short break.", 4),
        ],
    },
}

# -------------------- ANALYSIS RULES --------------------

# Keep place lists in a consistent category -> city -> name order.
places = dict(sorted(
    places.items(),
    key=lambda pair: (pair[1]["category"], pair[1]["city"], pair[0].casefold())
))

# Add clearly labelled illustrative positive examples so the prototype can
# demonstrate both positive and negative perspectives for every selected place.
# These are synthetic demo examples, not genuine public reviews.
for _place_name, _place in places.items():
    _cat = _place["category"]
    if _cat == "Hotel":
        _positive = [
            ("Family", "The room was clean and the staff helped us promptly.", 5),
            ("Professional", "Check-in was smooth and the location was convenient.", 4),
        ]
    elif _cat == "Restaurant":
        _positive = [
            ("Family", "The food was tasty and the staff were welcoming.", 5),
            ("Student", "The meal was satisfying and service was quick.", 4),
        ]
    elif _cat == "Apartment / House":
        _positive = [
            ("Homebuyer", "The layout looked practical during the illustrative site visit.", 4),
            ("Family", "The location seemed convenient for nearby daily needs.", 4),
        ]
    elif _cat == "Museum":
        _positive = [
            ("Student", "The exhibits made the history easier to understand.", 5),
            ("Family", "The visit was informative and enjoyable.", 4),
        ]
    elif _cat == "Park":
        _positive = [
            ("Family", "The outdoor visit was enjoyable and scenic.", 5),
            ("Student", "The place was pleasant to explore with friends.", 4),
        ]
    else:
        _positive = [
            ("Family", "The place was enjoyable and facilities were easy to access.", 5),
            ("Student", "The visit was pleasant and the area was easy to explore.", 4),
        ]
    _place["reviews"] = list(_place["reviews"]) + _positive

ISSUE_RULES = {
    "Price / Value": [
        "expensive", "overpriced", "costly", "price felt high",
        "higher than expected", "extra charges", "additional charges",
        "maintenance costs", "too expensive", "final price",
    ],
    "Service / Waiting": [
        "slow", "waiting time", "queue", "queues", "took extra time",
        "check-in", "response time", "service slowed",
    ],
    "Maintenance / Facilities": [
        "maintenance", "facilities", "amenities", "water supply",
        "parking", "wifi", "wi-fi", "construction progress",
    ],
    "Crowding / Access": [
        "crowded", "crowding", "traffic", "road access",
        "waiting area", "seating", "commute time", "directions",
        "signboards", "view", "viewpoint", "enclosure", "shaded",
    ],
    "Transparency / Due Diligence": [
        "confirm", "verify", "clearer", "in writing", "approved plan",
        "possession", "rera", "agreement", "registration",
        "carpet area", "brochures",
    ],
}

IMPROVEMENTS = {
    "Price / Value": (
        "Provide a transparent price breakdown, disclose extra charges, "
        "and clearly explain what is included."
    ),
    "Service / Waiting": (
        "Monitor peak-hour waiting times, improve staff coordination, "
        "and provide a clear complaint-resolution process."
    ),
    "Maintenance / Facilities": (
        "Use regular inspection checklists, record repair work, "
        "and publish accurate facility information."
    ),
    "Crowding / Access": (
        "Improve queue and seating management and provide realistic "
        "information about access and peak times."
    ),
    "Transparency / Due Diligence": (
        "Provide dated written information and let customers or homebuyers "
        "verify important claims through official sources."
    ),
}

def analyze_reviews(reviews):
    findings = []
    counts = Counter()

    for perspective, text, rating in reviews:
        lowered = text.lower()
        issues = [
            issue for issue, keywords in ISSUE_RULES.items()
            if any(word in lowered for word in keywords)
        ]

        if rating <= 2 and not issues:
            issues = ["General dissatisfaction"]

        if issues:
            findings.append({
                "Perspective": perspective,
                "Rating": rating,
                "Review": text,
                "Issues": issues,
            })
            counts.update(issues)

    average = (
        sum(item[2] for item in reviews) / len(reviews)
        if reviews else 0
    )

    return {
        "findings": findings,
        "counts": counts,
        "average": average,
        "total": len(reviews),
    }

def demo_score(place, analysis):
    # Demonstration formula only; not a real-world verified score.
    score = 70 + (analysis["average"] - 3) * 8
    score -= min(15, len(analysis["findings"]) * 1.5)
    if place["category"] == "Apartment / House":
        score -= 3
    return max(0, min(100, round(score)))

def label(name):
    item = places[name]
    return f"{name}  |  {item['category']}  |  {item['city']}"

# -------------------- HEADER --------------------
st.markdown("""
<div class="hero">
    <div class="hero-title">FACT CHECK ✓</div>
    <div class="hero-subtitle">WITH REALITYLENS AI</div>
    <div class="hero-caption">Place Reviews · Claim Verification · Evidence Signals · Trust Score</div>
</div>
""", unsafe_allow_html=True)

st.warning(
    "DEMO DATA NOTICE: The reviews shown here are illustrative examples created "
    "to demonstrate the analysis. They are not genuine customer reviews, live ratings, "
    "or verified allegations. The analysis does not independently authenticate evidence."
)

# -------------------- SIDEBAR FILTERS --------------------
st.sidebar.title("Explore Andhra Pradesh Places")
st.sidebar.caption("Hotels • Restaurants • Houses • Museums • Parks")

category = st.sidebar.selectbox(
    "Category",
    ["All categories", "Hotel", "Restaurant", "Apartment / House", "Museum", "Park"],
)
city_options = ["All cities"] + sorted({p["city"] for p in places.values()})
city = st.sidebar.selectbox("City", city_options)

filtered_places = [
    name for name, item in places.items()
    if (category == "All categories" or item["category"] == category)
    and (city == "All cities" or item["city"] == city)
]
st.sidebar.caption(f"{len(filtered_places)} listings in this demo catalogue")
st.sidebar.markdown("---")
st.sidebar.caption("Always verify current details through official sources.")
st.sidebar.markdown("---")
st.sidebar.markdown("**Optional LLM review assistant**")
llm_api_key = st.sidebar.text_input(
    "OpenAI API key (optional)",
    type="password",
    help="Only used when you press the LLM analysis button. It is not saved by this app.",
    key="llm_api_key_input",
)
st.sidebar.caption("Without an API key, the prototype still runs its local review rules.")

# -------------------- NAVIGATION --------------------
explore_tab, report_tab, compare_tab, saved_tab, submit_tab, feed_tab, about_tab = st.tabs([
    "Explore Places",
    "Reviews & Reality Report",
    "Compare",
    "Saved",
    "Submit a Claim",
    "Ranked Feed",
    "About",
])

# -------------------- EXPLORE --------------------
with explore_tab:
    st.subheader("Explore selected places in Andhra Pradesh")
    st.write(
        "Browse hotels, restaurants and residential projects. "
        "Choose a listing to view its analysis."
    )

    if filtered_places:
        columns = st.columns(3)
        for index, name in enumerate(filtered_places):
            item = places[name]
            with columns[index % 3]:
                st.markdown('<div class="place-card">', unsafe_allow_html=True)
                st.markdown(f"### {name}")
                st.markdown(f"**Category:** {item['category']}")
                st.markdown(f"**City:** {item['city']}")
                st.markdown(f"**Price range:** {item['price']}")
                st.write(item["description"])
                st.markdown("</div>", unsafe_allow_html=True)

                st.link_button(
                    "Open reference website",
                    item["source"],
                    use_container_width=True,
                )
                if st.button("Analyze this place", key=f"pick_{name}"):
                    st.session_state["report_place_select"] = name
                    st.toast("Place selected. Open Reviews & Reality Report.")
    else:
        st.info("No places match those filters.")

    st.caption(
        "A listing or external link is not an endorsement. Confirm current details independently."
    )

# -------------------- REPORT --------------------
with report_tab:
    st.subheader("Reviews & Reality Report")

    all_names = list(places.keys())
    default_name = st.session_state.get("report_place_select", st.session_state.get("report_place", all_names[0]))
    if default_name not in places:
        default_name = all_names[0]

    selected = st.selectbox(
        "Select a place to analyze",
        all_names,
        index=all_names.index(default_name),
        format_func=label,
        key="report_place_select",
    )

    place = places[selected]
    analysis = analyze_reviews(place["reviews"])
    score = demo_score(place, analysis)

    st.markdown(f"## {selected}")
    st.write(place["description"])

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Demo score", f"{score}/100")
    m2.metric("Review examples", analysis["total"])
    m3.metric("Flagged examples", len(analysis["findings"]))
    m4.metric("Issue categories", len(analysis["counts"]))

    st.caption(
        "This score is generated by a simple demonstration formula. "
        "It is not a verified quality rating or a trained ML prediction."
    )

    # Perspective and sentiment are shown as review outputs; the five TruthLens
    # measures below follow the uploaded pitch deck: Authenticity, Credibility,
    # Trust, Confidence Score (0-100), and Rank.
    def review_sentiment(review_row):
        perspective, review_text, rating = review_row
        if rating >= 4:
            return "Positive"
        if rating <= 2:
            return "Negative"
        return "Mixed / Neutral"

    sentiment_rows = []
    for _perspective, _review_text, _rating in place["reviews"]:
        _matches = [
            issue for issue, keywords in ISSUE_RULES.items()
            if any(word in _review_text.lower() for word in keywords)
        ]
        sentiment_rows.append({
            "Perspective": _perspective,
            "Sentiment": review_sentiment((_perspective, _review_text, _rating)),
            "Rating": _rating,
            "Review": _review_text,
            "Topic detected": ", ".join(_matches) if _matches else "General experience",
            "Evidence status": "Not independently verified",
        })
    sentiment_df = pd.DataFrame(sentiment_rows)

    st.markdown("## Review signals by person perspective")
    st.caption("See the positive, negative and mixed experiences that feed into the analysis. Demo examples only.")
    sentiment_counts = sentiment_df["Sentiment"].value_counts()
    q1, q2, q3 = st.columns(3)
    q1.metric("Positive reviews", int(sentiment_counts.get("Positive", 0)))
    q2.metric("Negative reviews", int(sentiment_counts.get("Negative", 0)))
    q3.metric("Mixed / neutral", int(sentiment_counts.get("Mixed / Neutral", 0)))
    st.dataframe(
        sentiment_df[["Perspective", "Sentiment", "Rating", "Review", "Topic detected"]],
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("## TruthLens: Five Trust Measures")
    st.caption("Outputs are based on this prototype's illustrative review data and heuristic rules. They are not verified real-world findings.")

    # Conservative demo-only indicators. Authenticity cannot be confirmed without
    # original evidence; credibility is a heuristic signal, not a source certification.
    ratings = [r[2] for r in place["reviews"]]
    avg_rating = (sum(ratings) / len(ratings)) if ratings else 0
    n_reviews = len(place["reviews"])
    matched_issue_count = len(analysis["findings"])
    authenticity = max(20, min(95, 48 + (sum(1 for r in place["reviews"] if len(r[1]) > 20) * 3) - min(20, matched_issue_count)))
    credibility = max(20, min(95, round(35 + avg_rating * 10 + min(10, n_reviews))))
    verified_backing = 0  # no verified-user connector in this demo
    trust = max(10, min(95, round((authenticity * 0.35) + (credibility * 0.35) + (verified_backing * 0.30))))
    confidence_score = max(0, min(100, round((authenticity * 0.30) + (credibility * 0.35) + (trust * 0.35))))

    if confidence_score >= 75 and matched_issue_count <= max(1, n_reviews // 3):
        verdict = "Genuine-like signal"
    elif authenticity < 40 or matched_issue_count >= max(5, n_reviews // 2):
        verdict = "Suspicious signal"
    elif avg_rating < 2.8:
        verdict = "Potentially misleading / needs review"
    else:
        verdict = "Unverified"

    # Rank is within the current demo catalogue and should never be read as an
    # official or live ranking.
    ranking_values = []
    for _name, _item in places.items():
        _a = analyze_reviews(_item["reviews"])
        _avg = _a["average"]
        _score = round(max(0, min(100, 30 + (_avg * 10) - min(20, len(_a["findings"]) * 1.5))))
        ranking_values.append((_name, _score))
    ranking_values.sort(key=lambda x: x[1], reverse=True)
    demo_rank = next((i for i, (nm, _) in enumerate(ranking_values, start=1) if nm == selected), None)

    score_cols = st.columns(5)
    score_cols[0].metric("Authenticity", f"{authenticity}/100")
    score_cols[1].metric("Credibility", f"{credibility}/100")
    score_cols[2].metric("Trust", f"{trust}/100")
    score_cols[3].metric("Confidence score", f"{confidence_score}/100")
    score_cols[4].metric("Demo rank", f"#{demo_rank}" if demo_rank else "—")
    st.markdown(f"### Provisional verdict: **{verdict}**")
    st.progress(confidence_score / 100)
    st.caption(
        "Authenticity and credibility are heuristic demo signals. No verified identity, receipt/photo OCR, "
        "independent source checks, or verified-crowd votes are connected in this version. "
        "Therefore the verdict remains provisional and all claims require human review."
    )

    with st.expander("1. Authenticity — review/evidence integrity signals", expanded=True):
        st.metric("Demo authenticity indicator", f"{authenticity}/100")
        st.dataframe(
            sentiment_df[["Perspective", "Rating", "Review", "Evidence status"]],
            use_container_width=True, hide_index=True,
        )
        st.write("Evidence to collect: original photo or receipt, date/time, source URL, metadata and an unedited copy. This prototype does not perform image forensics or prove a review is authentic.")

    with st.expander("2. Credibility — source reliability signals", expanded=True):
        st.metric("Demo credibility indicator", f"{credibility}/100")
        st.dataframe(
            sentiment_df[["Perspective", "Sentiment", "Rating", "Review"]],
            use_container_width=True, hide_index=True,
        )
        st.write("Source checks to record: who published the claim, whether the visit/transaction is supported, whether the source is independent, and whether the date/context matches. Source credibility is not verified automatically.")

    with st.expander("3. Trust — independent backing", expanded=True):
        st.metric("Verified independent backing", "0 connected votes")
        st.write("The pitch deck proposes verified visitors/customers and trust-weighted votes. No OTP/device verification or verified-user voting service is connected in this prototype, so this measure is intentionally not presented as confirmed crowd support.")
        st.dataframe(
            sentiment_df[["Perspective", "Sentiment", "Review", "Evidence status"]],
            use_container_width=True, hide_index=True,
        )

    with st.expander("4. Confidence Score — 0 to 100", expanded=True):
        st.metric("Provisional confidence score", f"{confidence_score}/100")
        st.write(f"**Current provisional verdict:** {verdict}")
        st.write("The score combines the demo authenticity, credibility and trust indicators. It is a prototype calculation, not a calibrated probability that a claim is true.")
        st.dataframe(
            pd.DataFrame([{
                "Measure": "Authenticity", "Score": authenticity,
            }, {
                "Measure": "Credibility", "Score": credibility,
            }, {
                "Measure": "Trust", "Score": trust,
            }, {
                "Measure": "Combined confidence score", "Score": confidence_score,
            }]),
            use_container_width=True, hide_index=True,
        )

    with st.expander("5. Rank — comparison with similar selected places", expanded=True):
        st.metric("Demo catalogue rank", f"#{demo_rank} of {len(ranking_values)}")
        rank_df = pd.DataFrame([
            {"Rank": i, "Place": nm, "Demo score": sc}
            for i, (nm, sc) in enumerate(ranking_values, start=1)
        ])
        st.dataframe(rank_df, use_container_width=True, hide_index=True)
        st.caption("Ranks are calculated from illustrative examples in this local catalogue only—not live reviews, verified facts, or an official recommendation.")

    st.markdown("## Claim → Evidence → Verdict")
    with st.form("claim_check_form"):
        claim_text = st.text_area(
            "Paste a claim or review about this place",
            placeholder="Example: The visitor area was closed on the date of my visit.",
        )
        evidence_text = st.text_area(
            "Evidence or source details (optional)",
            placeholder="Add an official URL, receipt details, photo/date description, document reference, or say what evidence is missing.",
        )
        claim_submitted = st.form_submit_button("Check claim")
    if claim_submitted:
        if not claim_text.strip():
            st.warning("Enter a claim first.")
        else:
            claim_lower = claim_text.lower()
            claim_hits = [topic for topic, words in ISSUE_RULES.items() if any(w in claim_lower for w in words)]
            st.markdown("### Extracted checkable claim")
            st.write(claim_text.strip())
            st.markdown("### Initial claim assessment")
            if evidence_text.strip():
                st.info("UNVERIFIED — evidence details supplied, but this prototype has not authenticated them or checked independent sources.")
            else:
                st.warning("UNVERIFIED — no supporting evidence details supplied yet.")
            st.write("**Possible topics detected:** " + (", ".join(claim_hits) if claim_hits else "No specific topic matched by the demo rules"))
            st.write("**Next checks:** validate source credibility, evidence date and authenticity; compare with independent sources; seek verified visitor/customer confirmation; escalate serious or disputed cases for human review.")
            st.caption("The app does not automatically declare a claim genuine, suspicious or misleading from text alone.")

    st.markdown("## Negative Review Intelligence")

    if not analysis["findings"]:
        st.success(
            "No examples matched the current rules. This does not prove that "
            "there are no negative reviews."
        )
    else:
        a, b, c = st.columns(3)
        a.metric("Flagged examples", len(analysis["findings"]))
        b.metric(
            "Perspectives",
            len({x["Perspective"] for x in analysis["findings"]}),
        )
        c.metric("Issue types", len(analysis["counts"]))

        st.markdown("### Recurring issue categories")
        issue_table = pd.DataFrame([
            {"Issue": issue, "Mentions": count}
            for issue, count in analysis["counts"].most_common()
        ])
        st.dataframe(issue_table, use_container_width=True, hide_index=True)

        st.markdown("### Findings by perspective")
        perspectives = sorted({
            item["Perspective"] for item in analysis["findings"]
        })

        for perspective in perspectives:
            group = [
                item for item in analysis["findings"]
                if item["Perspective"] == perspective
            ]

            with st.expander(
                f"{perspective} — {len(group)} flagged example(s)",
                expanded=True,
            ):
                for number, item in enumerate(group, start=1):
                    st.markdown(
                        f"**Example {number} · Rating: {item['Rating']}/5**"
                    )
                    st.write(item["Review"])
                    st.write("**Detected topics:** " + ", ".join(item["Issues"]))

                    for issue in item["Issues"]:
                        suggestion = IMPROVEMENTS.get(
                            issue,
                            "Review the complaint and investigate before taking action.",
                        )
                        st.info(f"**Suggested action — {issue}:** {suggestion}")

                    evidence = st.text_area(
                        "Required evidence / source details",
                        key=f"evidence_{selected}_{perspective}_{number}",
                        placeholder=(
                            "Enter a source name, document date, receipt details, "
                            "official URL, or description of relevant evidence."
                        ),
                    )

                    evidence_key = f"{selected}|{perspective}|{number}"
                    if not evidence.strip():
                        st.warning("Evidence required: add a source, dated record, URL, receipt, photo/document description, or write what evidence still needs to be collected. This finding cannot be marked ready yet.")
                    else:
                        st.success("Evidence note recorded for human verification — not independently authenticated.")
                        st.caption(
                            "Next check: source credibility, date, authenticity, context, "
                            "and whether the evidence directly supports or contradicts the review claim."
                        )
                        st.session_state.setdefault("evidence_notes", {})[evidence_key] = evidence.strip()
                    st.divider()

        st.markdown("### Improvement priorities")
        for issue, count in analysis["counts"].most_common(3):
            st.markdown(
                f"- **{issue} ({count} mention(s)):** "
                f"{IMPROVEMENTS.get(issue, 'Investigate the complaint and document corrective action.')}"
            )

    # Machine-learning topic grouping (TF-IDF + KMeans) when scikit-learn is installed.
    st.markdown("## AI / ML Review Intelligence")
    st.caption("Local ML groups similar review wording; the rule-based issue detector above flags specific complaint topics. Both are decision-support signals, not verified facts.")
    review_texts = [row[1] for row in place["reviews"]]
    if len(review_texts) >= 3:
        try:
            from sklearn.feature_extraction.text import TfidfVectorizer
            from sklearn.cluster import KMeans
            vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
            matrix = vectorizer.fit_transform(review_texts)
            cluster_count = min(3, len(review_texts))
            model = KMeans(n_clusters=cluster_count, random_state=42, n_init=10)
            cluster_ids = model.fit_predict(matrix)
            cluster_df = pd.DataFrame({
                "ML topic group": [f"Group {int(cid) + 1}" for cid in cluster_ids],
                "Perspective": [row[0] for row in place["reviews"]],
                "Review example": review_texts,
            }).sort_values(["ML topic group", "Perspective"])
            st.dataframe(cluster_df, use_container_width=True, hide_index=True)
            st.caption("Model: TF-IDF text features + KMeans clustering. These are automatically grouped text patterns, not trained truth labels.")
        except ImportError:
            st.info("Optional ML package missing. Install it with: python -m pip install scikit-learn")
        except ValueError as exc:
            st.info(f"ML grouping could not run on this small sample: {exc}")

    st.markdown("## LLM-assisted improvement suggestions")
    st.write("An LLM can draft practical improvements from the currently selected place's flagged examples. Evidence and recommendations still need human verification.")
    if st.button("Generate improvement plan with LLM", key="llm_improvement_plan"):
        if not llm_api_key.strip():
            st.warning("Enter your OpenAI API key in the sidebar first. You can still use the local analysis without it.")
        else:
            flagged_payload = [
                {"perspective": x["Perspective"], "rating": x["Rating"], "review_example": x["Review"], "issues": x["Issues"]}
                for x in analysis["findings"]
            ]
            prompt = (
                "You are a careful customer-experience improvement assistant. Analyze these illustrative review examples for "
                + selected + ". Identify recurring negative experiences, separate evidence from assumptions, and propose a concise prioritized action plan. "
                "Do not claim these are real reviews or state allegations as facts. Mention what evidence should be collected. Data: "
                + json.dumps(flagged_payload, ensure_ascii=False)
            )
            request_body = json.dumps({
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "Be evidence-aware, concise, and explicit about uncertainty."},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.2,
            }).encode("utf-8")
            req = urllib.request.Request(
                "https://api.openai.com/v1/chat/completions",
                data=request_body,
                headers={"Authorization": "Bearer " + llm_api_key.strip(), "Content-Type": "application/json"},
                method="POST",
            )
            try:
                with urllib.request.urlopen(req, timeout=45) as response:
                    result_json = json.loads(response.read().decode("utf-8"))
                llm_text = result_json["choices"][0]["message"]["content"]
                st.markdown("### Suggested action plan")
                st.write(llm_text)
                st.caption("Generated by gpt-4o-mini using demo review examples. Check all recommendations and gather real evidence before acting.")
            except urllib.error.HTTPError as exc:
                st.error(f"LLM request failed (HTTP {exc.code}). Check API key, API access and billing, then try again.")
            except Exception as exc:
                st.error(f"Could not reach the LLM service: {exc}")

    st.markdown("## Review examples used in this demo")
    review_df = pd.DataFrame([
        {
            "Perspective": perspective,
            "Rating": rating,
            "Review text": text,
            "Data status": "Illustrative demo text",
        }
        for perspective, text, rating in place["reviews"]
    ])
    st.dataframe(review_df, use_container_width=True, hide_index=True)

    st.download_button(
        "Download review examples as CSV",
        data=review_df.to_csv(index=False).encode("utf-8"),
        file_name="realitylens_demo_reviews.csv",
        mime="text/csv",
    )

# -------------------- COMPARE --------------------
with compare_tab:
    st.subheader("Compare places")

    compare_names = st.multiselect(
        "Choose places to compare",
        all_names if "all_names" in globals() else list(places.keys()),
        default=list(places.keys())[:2],
        format_func=label,
    )

    if compare_names:
        rows = []
        for name in compare_names:
            item = places[name]
            result = analyze_reviews(item["reviews"])
            most_common = (
                result["counts"].most_common(1)[0][0]
                if result["counts"] else "No match"
            )
            rows.append({
                "Place": name,
                "Category": item["category"],
                "City": item["city"],
                "Price": item["price"],
                "Demo score /100": demo_score(item, result),
                "Review examples": result["total"],
                "Flagged examples": len(result["findings"]),
                "Most common issue": most_common,
            })

        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        st.caption(
            "This comparison uses demo examples only; it is not a ranking of actual places."
        )
    else:
        st.info("Select at least one place to compare.")

# -------------------- SAVED --------------------
with saved_tab:
    st.subheader("Saved places")
    save_name = st.selectbox(
        "Choose a place",
        list(places.keys()),
        format_func=label,
        key="save_name",
    )

    if st.button("Save place"):
        saved = st.session_state.get("saved_places", [])
        if save_name not in saved:
            saved.append(save_name)
        st.session_state["saved_places"] = saved
        st.success("Place saved for this session.")

    saved = st.session_state.get("saved_places", [])
    if saved:
        for name in saved:
            st.markdown(f"- **{name}** — {places[name]['category']}, {places[name]['city']}")
    else:
        st.info("No saved places yet. Saved items last for this session.")

# -------------------- SUBMIT CLAIM --------------------
with submit_tab:
    st.subheader("Submit a claim about a selected place")
    st.write("Phase 1 focuses on customer/visitor claims about hotels, restaurants, residential projects, museums and parks.")
    with st.form("submit_claim_tab_form"):
        submit_place = st.selectbox("Place", list(places.keys()), format_func=label, key="submit_claim_place")
        submit_claim = st.text_area("Paste any review, post or claim", placeholder="Describe one checkable statement about the place.")
        submit_proof = st.text_area("Add proof or source details", placeholder="Official URL, receipt/document details, photo and visit date, or other source information.")
        submit_button = st.form_submit_button("Extract claim and assess")
    if submit_button:
        if not submit_claim.strip():
            st.warning("Please enter a claim or review.")
        else:
            lowered = submit_claim.lower()
            matched_topics = [topic for topic, words in ISSUE_RULES.items() if any(word in lowered for word in words)]
            st.markdown("### 1. Input")
            st.write(f"**Place:** {submit_place}")
            st.write(submit_claim.strip())
            st.markdown("### 2. Extract")
            st.write("**Candidate claim:** " + submit_claim.strip())
            st.write("**Topics detected:** " + (", ".join(matched_topics) if matched_topics else "No rule-based topic match"))
            st.markdown("### 3. Verify")
            if submit_proof.strip():
                st.write("**Evidence supplied:** " + submit_proof.strip())
                st.warning("Evidence provided but not independently authenticated.")
            else:
                st.warning("No evidence supplied yet. Add an independent source, dated record, receipt, photo/document or verified visitor confirmation.")
            st.markdown("### 4. Verdict")
            st.info("UNVERIFIED — a human must review evidence and independent sources before assigning a final verdict.")
            st.markdown("### 5. Share")
            verdict_card = (
                f"TRUTHLENS — PROVISIONAL CLAIM CARD\nPlace: {submit_place}\n"
                f"Claim: {submit_claim.strip()}\nStatus: UNVERIFIED\n"
                "Note: Evidence has not been independently authenticated."
            )
            st.code(verdict_card)
            st.download_button("Download provisional verdict card", verdict_card, file_name="truthlens_verdict_card.txt", mime="text/plain")

# -------------------- RANKED FEED --------------------
with feed_tab:
    st.subheader("Ranked feed — claims and selected places")
    st.caption("Illustrative catalogue ranking, not a ranking of real-time public opinion.")
    feed_rows = []
    for _name, _item in places.items():
        _analysis = analyze_reviews(_item["reviews"])
        _score = round(max(0, min(100, 30 + (_analysis["average"] * 10) - min(20, len(_analysis["findings"]) * 1.5))))
        _verdict = "Unverified"
        if _score >= 70 and len(_analysis["findings"]) <= 3:
            _verdict = "Genuine-like signal (demo)"
        elif len(_analysis["findings"]) >= 6:
            _verdict = "Suspicious signal (demo)"
        feed_rows.append({
            "Place": _name,
            "Category": _item["category"],
            "City": _item["city"],
            "Demo score": _score,
            "Sample reviews": _analysis["total"],
            "Flagged examples": len(_analysis["findings"]),
            "Status": _verdict,
        })
    feed_df = pd.DataFrame(feed_rows).sort_values(["Demo score", "Place"], ascending=[False, True])
    feed_df.insert(0, "Rank", range(1, len(feed_df) + 1))
    st.dataframe(feed_df, use_container_width=True, hide_index=True)
    st.caption("The deck's final verdict options are Genuine, Suspicious, Misleading and Unverified. Here they are represented only as provisional demo signals; verified verdicts require evidence and human review.")

# -------------------- ABOUT --------------------
with about_tab:
    st.subheader("About TruthLens / RealityLensAI")
    st.write(
        "A fact-check layer for claims about selected places—not another review platform. "
        "Reviews are raw input; the prototype organises claims, highlights evidence gaps, "
        "compares perspectives and displays a provisional Trust Score."
    )

    st.markdown("### Core workflow")
    st.markdown("""
    1. **Input:** paste a review, post or claim and optionally add proof.
    2. **Extract:** identify a checkable claim and likely topic.
    3. **Verify:** review evidence, source reliability, independent signals and verified-user confirmation.
    4. **Verdict:** Genuine, Suspicious, Misleading or Unverified—final decisions require evidence and human review.
    5. **Share:** download a provisional verdict card.
    """)

    st.markdown("### Five TrustLens measures")
    st.markdown("""
    - **Authenticity:** whether content or evidence appears genuine.
    - **Credibility:** whether the source is reliable.
    - **Trust:** whether independent sources and verified visitors/customers support the claim.
    - **Confidence Score (0–100):** one weighted, explainable confidence indicator.
    - **Rank:** position among similar claims/places in the demo catalogue.
    """)

    st.markdown("### Intelligence under the hood — planned / prototype components")
    st.markdown("""
    - **Graph and anomaly ML:** detect suspicious account clusters and possible review rings.
    - **Vision and OCR:** inspect receipts, photos, reused images and available metadata.
    - **LLM with retrieval-augmented generation (RAG):** extract claims and compare them with source material.
    - **Time-series analysis:** flag sudden bursts and coordinated posting times.
    - **Ensemble scoring:** combine signals into one explainable confidence score.
    - **Human in the loop:** review edge cases, appeals and serious verdicts; use reviewed cases to improve the system.
    """)

    st.markdown("### Anti-faking controls — planned")
    st.markdown("""
    - Verified identity through OTP/device checks and one person per account.
    - Proof of experience so verified customers/visitors have stronger voting weight.
    - Image authenticity checks using metadata and edit/reuse detection.
    - Vote-ring defence that discounts coordinated accounts.
    - Trust-weighted votes where accurate contributions earn influence.
    - Human review and appeal for serious or disputed verdicts.
    """)

    st.markdown("### Participation and business value — planned")
    st.markdown("""
    - Low-friction participation through one-tap, voice, WhatsApp and regional-language flows.
    - Privacy-aware participation: anonymous to the business, verified by the service.
    - Status updates when a business responds or fixes an issue.
    - Recognition through badges and trust levels, not cash for claims.
    - Businesses could check suspicious claims, appeal a verdict and earn a fact-verified badge when evidence supports it.
    """)

    st.markdown("### Roadmap and success metrics")
    st.markdown("""
    - **Week 1:** choose one niche and city, define verdict labels.
    - **Week 2:** build submit, verdict and ranked-feed screens with claim scoring.
    - **Week 3:** add crowd voting and trust scores.
    - **Week 4:** test with 20–50 real users.
    - **Phase 2:** public issues, location and authority routing.
    - **Success metrics:** verdict accuracy, share of users who vote, verdict cards shared, and repeat usage.
    """)

    st.markdown("### Current prototype limitations")
    st.markdown("""
    - Catalogue review text is illustrative, not genuine customer/visitor feedback.
    - No OTP identity verification, verified-user voting, image-forensics service, live source retrieval or authority-routing integration is connected.
    - The numeric measures and ranking are heuristic demo outputs, not trained or calibrated truth probabilities.
    - Official source links are reference starting points; they do not verify individual claims.
    """)

    st.markdown("### Selected-place categories")
    st.write("Hotels • Restaurants • Apartments / Houses • Museums • Parks")
