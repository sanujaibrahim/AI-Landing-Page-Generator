import streamlit as st
import streamlit.components.v1 as components
import html
import re


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Website Builder",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# STREAMLIT CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 25px;
}

.stButton > button {
    border-radius: 10px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 AI Website Builder</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Describe your idea and create a complete website</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# INPUT
# =========================================================

prompt = st.text_area(
    "✨ What website do you want to create?",
    placeholder=(
        "Example: Create a modern portfolio website for a data science student "
        "with projects, skills and contact section."
    ),
    height=130
)


col1, col2 = st.columns(2)

with col1:
    style = st.selectbox(
        "🎨 Choose design style",
        [
            "Modern",
            "Minimal",
            "Professional",
            "Creative",
            "Dark"
        ]
    )

with col2:
    website_type = st.selectbox(
        "🌐 Website type",
        [
            "Automatic",
            "Portfolio",
            "Business",
            "Restaurant",
            "Fitness",
            "Education",
            "E-commerce",
            "Technology"
        ]
    )


generate = st.button(
    "🚀 Create My Website",
    use_container_width=True
)


# =========================================================
# WEBSITE CONTENT GENERATOR
# =========================================================

def create_content(prompt, website_type):

    text = prompt.lower()

    # Automatic detection
    if website_type == "Automatic":

        if any(x in text for x in [
            "portfolio", "student", "developer",
            "resume", "personal"
        ]):
            website_type = "Portfolio"

        elif any(x in text for x in [
            "restaurant", "cafe", "food"
        ]):
            website_type = "Restaurant"

        elif any(x in text for x in [
            "fitness", "gym", "workout"
        ]):
            website_type = "Fitness"

        elif any(x in text for x in [
            "course", "school", "college",
            "education", "learning"
        ]):
            website_type = "Education"

        elif any(x in text for x in [
            "shop", "store", "ecommerce",
            "fashion", "products"
        ]):
            website_type = "E-commerce"

        elif any(x in text for x in [
            "ai", "technology", "software",
            "saas", "app"
        ]):
            website_type = "Technology"

        else:
            website_type = "Business"

    # -----------------------------------------------------
    # PORTFOLIO
    # -----------------------------------------------------

    if website_type == "Portfolio":

        content = {
            "brand": "MY PORTFOLIO",
            "hero_title": "Turning Ideas Into Digital Experiences",
            "hero_text": (
                "I'm a passionate data science student creating "
                "modern, useful and intelligent digital solutions."
            ),
            "button": "View My Work",
            "features": [
                ("📊", "Data Science", "Transform data into meaningful insights."),
                ("💻", "Development", "Build practical and responsive applications."),
                ("🤖", "Artificial Intelligence", "Create intelligent solutions using AI and machine learning.")
            ],
            "about_title": "About Me",
            "about_text": (
                "I enjoy solving real-world problems using technology, "
                "data and creative thinking. My goal is to build solutions "
                "that are simple, useful and impactful."
            )
        }

    # -----------------------------------------------------
    # FITNESS
    # -----------------------------------------------------

    elif website_type == "Fitness":

        content = {
            "brand": "FITNESS+",
            "hero_title": "Your Fitness Journey Starts Here",
            "hero_text": (
                "Train smarter, stay motivated and achieve your fitness "
                "goals with a personalized experience."
            ),
            "button": "Start Your Journey",
            "features": [
                ("💪", "Workout Plans", "Personalized workout routines for every fitness level."),
                ("📊", "Track Progress", "Monitor your workouts and improvements."),
                ("🔥", "Stay Motivated", "Build consistency and reach your goals.")
            ],
            "about_title": "Train Smarter",
            "about_text": (
                "Our fitness experience combines simple workout planning, "
                "progress tracking and motivation to help you stay consistent."
            )
        }

    # -----------------------------------------------------
    # RESTAURANT
    # -----------------------------------------------------

    elif website_type == "Restaurant":

        content = {
            "brand": "TASTE",
            "hero_title": "Good Food. Great Moments.",
            "hero_text": (
                "Discover delicious food, fresh ingredients and "
                "memorable dining experiences."
            ),
            "button": "Explore Menu",
            "features": [
                ("🍽️", "Fresh Food", "Prepared with quality ingredients."),
                ("👨‍🍳", "Expert Chefs", "Creative dishes prepared by experienced chefs."),
                ("⭐", "Great Experience", "A dining experience worth remembering.")
            ],
            "about_title": "Made With Passion",
            "about_text": (
                "We believe great food brings people together. "
                "Every dish is prepared with care, creativity and fresh ingredients."
            )
        }

    # -----------------------------------------------------
    # EDUCATION
    # -----------------------------------------------------

    elif website_type == "Education":

        content = {
            "brand": "LEARNX",
            "hero_title": "Learn Today. Lead Tomorrow.",
            "hero_text": (
                "Build practical skills with modern courses designed "
                "for students and professionals."
            ),
            "button": "Start Learning",
            "features": [
                ("📚", "Expert Courses", "Learn from structured and practical content."),
                ("🎓", "Learn Anywhere", "Access your learning experience from anywhere."),
                ("🏆", "Build Skills", "Develop skills that support your career.")
            ],
            "about_title": "Learning Made Simple",
            "about_text": (
                "Our platform focuses on practical learning, "
                "easy-to-understand resources and career-ready skills."
            )
        }

    # -----------------------------------------------------
    # E-COMMERCE
    # -----------------------------------------------------

    elif website_type == "E-commerce":

        content = {
            "brand": "NOVA",
            "hero_title": "Discover Products You'll Love",
            "hero_text": (
                "Shop quality products with a simple, modern and "
                "convenient online experience."
            ),
            "button": "Shop Now",
            "features": [
                ("🛍️", "Quality Products", "Products selected with care."),
                ("💰", "Great Prices", "Get excellent value for your money."),
                ("🚚", "Fast Delivery", "Get your orders delivered quickly.")
            ],
            "about_title": "Shopping Made Simple",
            "about_text": (
                "Discover products, explore new collections and "
                "enjoy a smooth shopping experience."
            )
        }

    # -----------------------------------------------------
    # TECHNOLOGY
    # -----------------------------------------------------

    elif website_type == "Technology":

        content = {
            "brand": "NEXORA",
            "hero_title": "Technology That Moves You Forward",
            "hero_text": (
                "Build smarter products, automate workflows and "
                "turn ideas into powerful digital experiences."
            ),
            "button": "Explore Technology",
            "features": [
                ("🤖", "Smart Solutions", "Use modern technology to solve real problems."),
                ("⚡", "Fast Performance", "Build fast and reliable digital experiences."),
                ("📈", "Grow Faster", "Technology designed to support your growth.")
            ],
            "about_title": "Built For The Future",
            "about_text": (
                "We combine technology, creativity and intelligent "
                "solutions to build better digital experiences."
            )
        }

    # -----------------------------------------------------
    # BUSINESS
    # -----------------------------------------------------

    else:

        content = {
            "brand": "NOVA BUSINESS",
            "hero_title": "Build Something People Remember",
            "hero_text": (
                "Modern digital solutions designed to help your "
                "business grow and connect with your customers."
            ),
            "button": "Get Started",
            "features": [
                ("🚀", "Grow Faster", "Build a stronger digital presence."),
                ("💡", "Smart Solutions", "Simple solutions for real business problems."),
                ("📈", "Better Results", "Use technology to improve your business.")
            ],
            "about_title": "Why Choose Us?",
            "about_text": (
                "We create modern digital experiences focused on "
                "simplicity, performance and customer satisfaction."
            )
        }

    return content


# =========================================================
# WEBSITE GENERATOR
# =========================================================

def generate_website(content, style):

    brand = html.escape(content["brand"])
    title = html.escape(content["hero_title"])
    hero_text = html.escape(content["hero_text"])
    button = html.escape(content["button"])
    about_title = html.escape(content["about_title"])
    about_text = html.escape(content["about_text"])

    # -----------------------------------------------------
    # STYLE SETTINGS
    # -----------------------------------------------------

    if style == "Dark":

        background = "#080808"
        section = "#111111"
        text_color = "#ffffff"
        secondary = "#aaaaaa"
        accent = "#8b5cf6"
        card = "#181818"

    elif style == "Creative":

        background = "#fff7ed"
        section = "#ffffff"
        text_color = "#171717"
        secondary = "#666666"
        accent = "#f97316"
        card = "#ffffff"

    elif style == "Professional":

        background = "#f4f7fb"
        section = "#ffffff"
        text_color = "#172033"
        secondary = "#64748b"
        accent = "#2563eb"
        card = "#ffffff"

    elif style == "Minimal":

        background = "#ffffff"
        section = "#fafafa"
        text_color = "#111111"
        secondary = "#666666"
        accent = "#111111"
        card = "#ffffff"

    else:

        background = "#f5f7ff"
        section = "#ffffff"
        text_color = "#111827"
        secondary = "#64748b"
        accent = "#6366f1"
        card = "#ffffff"

    # -----------------------------------------------------
    # FEATURES
    # -----------------------------------------------------

    feature_html = ""

    for icon, feature_title, feature_description in content["features"]:

        feature_html += f"""
        <div class="feature-card">

            <div class="feature-icon">
                {html.escape(icon)}
            </div>

            <h3>
                {html.escape(feature_title)}
            </h3>

            <p>
                {html.escape(feature_description)}
            </p>

        </div>
        """

    # -----------------------------------------------------
    # COMPLETE WEBSITE
    # -----------------------------------------------------

    website = f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<style>

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}}

body {{
    font-family: Arial, Helvetica, sans-serif;
    background: {background};
    color: {text_color};
    line-height: 1.6;
}}

nav {{
    position: sticky;
    top: 0;
    z-index: 1000;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 8%;
    background: {section};
    border-bottom: 1px solid rgba(0,0,0,0.08);
}}

.logo {{
    font-size: 22px;
    font-weight: 800;
}}

.nav-links {{
    display: flex;
    gap: 30px;
    list-style: none;
}}

.nav-links a {{
    text-decoration: none;
    color: {text_color};
    font-weight: 600;
}}

.nav-links a:hover {{
    color: {accent};
}}

.menu {{
    display: none;
    font-size: 25px;
    cursor: pointer;
}}

.hero {{
    min-height: 720px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 80px 20px;

    background:
        radial-gradient(
            circle at top right,
            {accent}30,
            transparent 40%
        );
}}

.hero-content {{
    max-width: 900px;
    animation: fadeUp 1s ease;
}}

.badge {{
    display: inline-block;
    padding: 8px 16px;
    border-radius: 30px;
    background: {accent}20;
    color: {accent};
    font-weight: 700;
    margin-bottom: 25px;
}}

.hero h1 {{
    font-size: clamp(45px, 7vw, 82px);
    line-height: 1.05;
    margin-bottom: 25px;
}}

.hero p {{
    max-width: 700px;
    margin: auto;
    font-size: 20px;
    color: {secondary};
}}

.buttons {{
    margin-top: 35px;
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
}}

.btn {{
    display: inline-block;
    padding: 15px 28px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: 700;
    transition: 0.3s;
}}

.primary {{
    background: {accent};
    color: white;
}}

.primary:hover {{
    transform: translateY(-3px);
    opacity: 0.9;
}}

.secondary {{
    border: 1px solid {accent};
    color: {accent};
}}

.secondary:hover {{
    background: {accent};
    color: white;
}}

section {{
    padding: 100px 8%;
}}

.section-title {{
    text-align: center;
    max-width: 700px;
    margin: auto auto 55px;
}}

.section-title h2 {{
    font-size: 42px;
    margin-bottom: 15px;
}}

.section-title p {{
    color: {secondary};
}}

.features {{
    background: {section};
}}

.feature-grid {{
    max-width: 1200px;
    margin: auto;
    display: grid;
    grid-template-columns:
        repeat(auto-fit, minmax(250px, 1fr));
    gap: 25px;
}}

.feature-card {{
    background: {card};
    padding: 35px;
    border-radius: 20px;
    border: 1px solid rgba(0,0,0,0.07);
    transition: 0.3s;
}}

.feature-card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.08);
}}

.feature-icon {{
    font-size: 45px;
    margin-bottom: 20px;
}}

.feature-card h3 {{
    font-size: 22px;
    margin-bottom: 10px;
}}

.feature-card p {{
    color: {secondary};
}}

.about {{
    max-width: 1100px;
    margin: auto;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 70px;
    align-items: center;
}}

.about-box {{
    padding: 45px;
    border-radius: 25px;
    background:
        linear-gradient(
            135deg,
            {accent}20,
            transparent
        );
}}

.about-box h2 {{
    font-size: 45px;
    margin-bottom: 20px;
}}

.about-box p {{
    color: {secondary};
    font-size: 18px;
}}

.stats {{
    display: grid;
    grid-template-columns:
        repeat(2, 1fr);
    gap: 20px;
}}

.stat {{
    padding: 30px;
    background: {section};
    border-radius: 18px;
    text-align: center;
}}

.stat strong {{
    display: block;
    font-size: 35px;
    color: {accent};
}}

.cta-section {{
    text-align: center;
    background:
        linear-gradient(
            135deg,
            {accent},
            {accent}cc
        );
    color: white;
}}

.cta-section h2 {{
    font-size: 48px;
    margin-bottom: 20px;
}}

.cta-section p {{
    max-width: 650px;
    margin: auto;
    opacity: 0.9;
}}

.cta-white {{
    display: inline-block;
    margin-top: 30px;
    padding: 15px 30px;
    background: white;
    color: {accent};
    border-radius: 10px;
    text-decoration: none;
    font-weight: 700;
}}

.contact {{
    max-width: 800px;
    margin: auto;
}}

.contact-form {{
    display: grid;
    gap: 18px;
}}

.contact-form input,
.contact-form textarea {{
    width: 100%;
    padding: 16px;
    border-radius: 10px;
    border: 1px solid #ddd;
    font-size: 16px;
}}

.contact-form textarea {{
    min-height: 150px;
}}

.contact-form button {{
    padding: 16px;
    border: none;
    border-radius: 10px;
    background: {accent};
    color: white;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
}}

footer {{
    padding: 35px 8%;
    text-align: center;
    background: #090909;
    color: #aaa;
}}

@keyframes fadeUp {{

    from {{
        opacity: 0;
        transform: translateY(30px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}

}}

@media(max-width: 768px) {{

    nav {{
        padding: 18px 5%;
    }}

    .nav-links {{
        display: none;
        position: absolute;
        top: 70px;
        left: 0;
        right: 0;
        background: {section};
        flex-direction: column;
        padding: 25px;
        text-align: center;
    }}

    .nav-links.active {{
        display: flex;
    }}

    .menu {{
        display: block;
    }}

    .hero {{
        min-height: 650px;
    }}

    section {{
        padding: 70px 5%;
    }}

    .about {{
        grid-template-columns: 1fr;
    }}

    .stats {{
        grid-template-columns: 1fr 1fr;
    }}

}}

</style>

</head>

<body>


<!-- NAVBAR -->

<nav>

<div class="logo">
{brand}
</div>

<div class="menu" onclick="toggleMenu()">
☰
</div>

<ul class="nav-links" id="navLinks">

<li>
<a href="#home">Home</a>
</li>

<li>
<a href="#features">Features</a>
</li>

<li>
<a href="#about">About</a>
</li>

<li>
<a href="#contact">Contact</a>
</li>

</ul>

</nav>


<!-- HERO -->

<section class="hero" id="home">

<div class="hero-content">

<div class="badge">
✨ Welcome
</div>

<h1>
{title}
</h1>

<p>
{hero_text}
</p>

<div class="buttons">

<a href="#features" class="btn primary">
{button}
</a>

<a href="#about" class="btn secondary">
Learn More
</a>

</div>

</div>

</section>


<!-- FEATURES -->

<section class="features" id="features">

<div class="section-title">

<h2>
Everything You Need
</h2>

<p>
Simple, powerful and designed for a better experience.
</p>

</div>

<div class="feature-grid">

{feature_html}

</div>

</section>


<!-- ABOUT -->

<section id="about">

<div class="about">

<div class="about-box">

<h2>
{about_title}
</h2>

<p>
{about_text}
</p>

</div>

<div class="stats">

<div class="stat">

<strong>
10K+
</strong>

Users

</div>

<div class="stat">

<strong>
99%
</strong>

Satisfaction

</div>

<div class="stat">

<strong>
24/7
</strong>

Support

</div>

<div class="stat">

<strong>
100%
</strong>

Commitment

</div>

</div>

</div>

</section>


<!-- CTA -->

<section class="cta-section">

<h2>
Ready to Get Started?
</h2>

<p>
Take the next step and experience a better digital journey.
</p>

<a href="#contact" class="cta-white">
Get Started
</a>

</section>


<!-- CONTACT -->

<section id="contact">

<div class="section-title">

<h2>
Let's Connect
</h2>

<p>
Have a question? Send us a message.
</p>

</div>

<div class="contact">

<form class="contact-form"
onsubmit="submitForm(event)">

<input
type="text"
placeholder="Your Name"
required
>

<input
type="email"
placeholder="Your Email"
required
>

<textarea
placeholder="Your Message"
required
></textarea>

<button type="submit">
Send Message
</button>

</form>

</div>

</section>


<!-- FOOTER -->

<footer>

<p>
© 2026 {brand}. All rights reserved.
</p>

</footer>


<script>

function toggleMenu() {{

    document
        .getElementById("navLinks")
        .classList.toggle("active");

}}

function submitForm(event) {{

    event.preventDefault();

    alert(
        "Thank you! Your message has been submitted."
    );

}}

</script>


</body>

</html>
"""

    return website


# =========================================================
# GENERATE
# =========================================================

if generate:

    if not prompt.strip():

        st.warning(
            "⚠️ Please describe the website you want to create."
        )

    else:

        content = create_content(
            prompt,
            website_type
        )

        generated_html = generate_website(
            content,
            style
        )

        st.success(
            "🎉 Your website has been created!"
        )

        st.divider()

        # =================================================
        # LIVE WEBSITE
        # =================================================

        st.subheader("🌐 Live Website")

        components.html(
            generated_html,
            height=900,
            scrolling=True
        )

        # =================================================
        # DOWNLOAD
        # =================================================

        st.divider()

        st.subheader(
            "📥 Download Your Website"
        )

        st.download_button(
            label="⬇️ Download Complete Website",
            data=generated_html,
            file_name="my_ai_website.html",
            mime="text/html",
            use_container_width=True
        )

        st.success(
            "Your HTML website is ready. "
            "Download it and open the file in Chrome."
        )