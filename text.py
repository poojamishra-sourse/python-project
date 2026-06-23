# import pywhatkit as pw
# pw.start_server()


# txt="""Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
#  Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured"""
# pw.text_to_handwriting(txt,"text.png",[0,0,138])
# print("end")
from PIL import Image, ImageDraw, ImageFont
import textwrap

text = """Python is an interpreted high-level general-purpose programming language.
Python's design philosophy emphasizes code readability with its notable use
of significant indentation. Its language constructs and object-oriented
approach aim to help programmers write clear, logical code."""

# Image size create
img = Image.new('RGB', (500, 800), color="black")
draw = ImageDraw.Draw(img)

# Font load
font = ImageFont.truetype("QERoystonSuch.ttf", 20)  # font size adjust kar sakte ho

# Text wrap line handling
lines = textwrap.wrap(text, width=50)

y = 50
for line in lines:
    draw.text((50, y), line, font=font, fill=(0,255,0))  # fill = text color
    y += 40  # line spacing

img.save("handwritten_output.png")
print("Image saved ✔")