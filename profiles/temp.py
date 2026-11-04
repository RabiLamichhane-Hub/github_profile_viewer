
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

WIDTH = 900
HEIGHT = 550

BACKGROUND = "#E8EDF3"
NAVY = "#102A43"
GOLD = "#C9A44C"


def load_font(size, bold=False):
    font_name = "arialbd.ttf" if bold else "arial.ttf"
    font_path = Path("C:/Windows/Fonts") / font_name

    try:
        return ImageFont.truetype(str(font_path), size)
    except OSError:
        return ImageFont.load_default(size=size)


def fit_text(draw, text, font, max_width):
    text = str(text or "Not provided")

    while text and draw.textbbox(
        (0, 0), text + "...", font=font
    )[2] > max_width:
        text = text[:-1]

    return text + "..." if len(text) < len(str(text)) else text


def render_and_return_image(username, name, bio, public_repos, followers):

    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)

    # Main passport card
    draw.rounded_rectangle(
        (55, 35, 845, 515),
        radius=18,
        fill="#FFFFFF",
        outline=GOLD,
        width=4
    )

    # Header
    draw.rounded_rectangle(
        (55, 35, 845, 145),
        radius=18,
        fill=NAVY
    )

    draw.rectangle(
        (55, 115, 845, 145),
        fill=NAVY
    )

    # Header text
    draw.text(
        (90, 55),
        "GITHUB PROFILE",
        fill=GOLD,
        font=load_font(28, True)
    )

    draw.text(
        (90, 100),
        "DIGITAL IDENTITY CARD",
        fill="#FFFFFF",
        font=load_font(13, True)
    )

    # Passport photo frame
    draw.rectangle(
        (95, 185, 305, 405),
        fill="#E8EDF3",
        outline=GOLD,
        width=3
    )

    # Avatar background
    draw.ellipse(
        (135, 215, 265, 345),
        fill=NAVY
    )

    # Initials
    initials = "".join(
        part[0] for part in str(name or username).split()[:2]
    ).upper()

    font = load_font(43, True)
    bbox = draw.textbbox((0, 0), initials, font=font)

    x = 200 - (bbox[2] - bbox[0]) // 2
    y = 280 - (bbox[3] - bbox[1]) // 2 - bbox[1]

    draw.text(
        (x, y),
        initials,
        fill="#FFFFFF",
        font=font
    )

    draw.text(
        (120, 365),
        "PROFILE PHOTO",
        fill=NAVY,
        font=load_font(13, True)
    )

    # Information section
    info_x = 355

    draw.text(
        (info_x, 185),
        "USERNAME",
        fill="#64748B",
        font=load_font(12, True)
    )

    draw.text(
        (info_x, 205),
        fit_text(draw, "@" + username, load_font(22, True), 420),
        fill=NAVY,
        font=load_font(22, True)
    )

    draw.text(
        (info_x, 250),
        "FULL NAME",
        fill="#64748B",
        font=load_font(12, True)
    )

    draw.text(
        (info_x, 270),
        fit_text(draw, name, load_font(20, True), 420),
        fill="#1E293B",
        font=load_font(20, True)
    )

    draw.text(
        (info_x, 315),
        "BIO / DESCRIPTION",
        fill="#64748B",
        font=load_font(12, True)
    )

    draw.text(
        (info_x, 337),
        fit_text(draw, bio, load_font(16), 420),
        fill="#334155",
        font=load_font(16)
    )

    # Divider
    draw.line(
        (90, 430, 810, 430),
        fill="#CBD5E1",
        width=2
    )

    # Statistics
    stats = [
        ("PUBLIC REPOSITORIES", public_repos),
        ("FOLLOWERS", followers)
    ]

    positions = [110, 475]

    for i, (label, value) in enumerate(stats):

        sx = positions[i]

        draw.text(
            (sx, 450),
            label,
            fill="#64748B",
            font=load_font(12, True)
        )

        draw.text(
            (sx, 475),
            str(value),
            fill=NAVY,
            font=load_font(23, True)
        )

    # Footer
    draw.text(
        (650, 480),
        "GITHUB ID",
        fill=GOLD,
        font=load_font(13, True)
    )

    return image


# Generate passport-style profile
image = render_and_return_image(
    "rabi",
    "The Rabi",
    "Welcome to my GitHub profile!",
    10,
    6767
)

# Save image
image.save("output.png")

print("Passport-style profile saved as output.png")
