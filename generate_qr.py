import qrcode

def generate_qr(transaction_hash):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(transaction_hash)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    filename = f"qr_{transaction_hash[:8]}.png"
    img.save(filename)
    print(f"QR Code saved as {filename}")
    return filename
