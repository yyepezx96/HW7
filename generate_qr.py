import qrcode
import os

def generate_qr_code(url, filename="github_qr.png", fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill=fill_color, back_color=back_color)

    os.makedirs("qr_codes", exist_ok=True)
    img.save(f"qr_codes/{filename}")
    print(f"QR code saved as qr_codes/{filename}")

# Replace with your GitHub URL
url = "https://github.com/kaw393939"
generate_qr_code(url, filename="github_qr.png", fill_color="blue", back_color="yellow")

