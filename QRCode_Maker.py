import sys
from pathlib import Path
import qrcode
import qrcode.image.svg

def create_qr(url, filepath):
    factory = qrcode.image.svg.SvgPathImage

    img = qrcode.make(
        url,
        image_factory=factory
    )

    img.save(filepath)

def main():
    url = sys.argv[1]
    filename = sys.argv[2]
    script_dir = Path(__file__).resolve().parent
    folder = script_dir / "QR Codes"
    folder.mkdir(exist_ok=True)
    filepath = folder / (filename + ".svg")

    create_qr(url, filepath)
    print(f"Saved QR code as {filepath}")


main()