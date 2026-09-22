import sys
import qrcode
import qrcode.image.svg

def create_qr(url, filename):
    factory = qrcode.image.svg.SvgPathImage

    img = qrcode.make(
        url,
        image_factory=factory
    )

    img.save(filename)

def main():
    url = sys.argv[1]
    filename = sys.argv[2]

    create_qr(url, filename)
    print(f"Saved QR code as {filename}")


main()