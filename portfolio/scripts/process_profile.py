"""Remove white background from profile photo for dark-theme portfolio."""
from PIL import Image
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "profile.png"
OUT = ROOT / "assets" / "profile.png"
BACKUP = ROOT / "assets" / "profile-original.png"

def main():
    if BACKUP.exists() is False and SRC.exists():
        Image.open(SRC).save(BACKUP)

    img = Image.open(SRC if not BACKUP.exists() else BACKUP).convert("RGBA")
    arr = np.array(img, dtype=np.float32)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]

    # Distance from white; soft feather for clean edges
    white_dist = np.sqrt(
        np.maximum(0, r - 235) ** 2
        + np.maximum(0, g - 235) ** 2
        + np.maximum(0, b - 235) ** 2
    )
    alpha = np.clip(255 - white_dist * 4.5, 0, 255)

    # Preserve shirt/skin — boost opacity for non-white pixels
    not_white = (r < 230) | (g < 230) | (b < 230)
    alpha[not_white] = np.maximum(alpha[not_white], 255)

    arr[..., 3] = alpha
    result = Image.fromarray(arr.astype(np.uint8), "RGBA")

    # Tight crop with padding
    bbox = result.getbbox()
    if bbox:
        pad = 40
        x0 = max(0, bbox[0] - pad)
        y0 = max(0, bbox[1] - pad)
        x1 = min(result.width, bbox[2] + pad)
        y1 = min(result.height, bbox[3] + pad)
        result = result.crop((x0, y0, x1, y1))

    # Square canvas for circular crop
    size = max(result.size)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ox = (size - result.width) // 2
    oy = (size - result.height) // 2
    canvas.paste(result, (ox, oy), result)
    canvas.save(OUT, optimize=True)
    print(f"Saved {OUT} ({size}x{size})")

if __name__ == "__main__":
    main()
