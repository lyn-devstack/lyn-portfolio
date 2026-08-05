from PIL import Image
import os

# Path to source PNG (generated earlier)
src_path = r"C:/Users/Leslie/.gemini/antigravity-ide/brain/8b7b5683-ed4c-4791-a2ef-e9843cb67d0e/portfolio_favicon_cp_1785950264441.png"
# Output .ico path (saved in project root)
out_path = os.path.join(os.path.dirname(__file__), "favicon.ico")

# Open the source image
im = Image.open(src_path)
# Ensure image is RGBA
im = im.convert("RGBA")
# Save as .ico with multiple sizes
im.save(out_path, format='ICO', sizes=[(16,16), (32,32), (48,48)])
print(f"Favicon generated at {out_path}")
