
import qrcode

# Link website Sanbites
url = "https://sanbites.streamlit.app"

# Membuat QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

# Membuat gambar QR Code
img = qr.make_image(
    fill_color="black",
    back_color="white"
)

# Menyimpan gambar
img.save("qrcode_sanbites.png")

print("QR Code Sanbites berhasil dibuat!")
