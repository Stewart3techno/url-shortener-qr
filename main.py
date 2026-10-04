import pyshorteners
import qrcode


def shorten_url(long_url):
    """Shorten long URLs using TinyURL API."""
    type_tiny = pyshorteners.Shortener()
    return type_tiny.tinyurl.short(long_url)


def generate_qr(url, output_filename="qrcode.png"):
    """Generate and save a QR code image for a URL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_filename)
    print(f"✅ QR Code saved as '{output_filename}'")


def main():
    print("=" * 45)
    print("   🚀 URL SHORTENER & QR CODE GENERATOR 🚀   ")
    print("=" * 45)

    long_url = input("Enter the long URL: ").strip()

    if not long_url:
        print("❌ Error: URL cannot be empty.")
        return

    try:
        short_url = shorten_url(long_url)
        print(f"\n✨ Shortened URL : {short_url}")

        generate_qr(short_url)

    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
