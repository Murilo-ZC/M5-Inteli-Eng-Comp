import qrcode
import json

# Pega todas as instâncias do banco
with open('registros.json', 'r') as file:
    db = json.load(file)
    for entry in db["data"]:
        # Cria um QRCode com o nome e o email
        img = qrcode.make(f'{entry["itemId"]}')
        img.save(f"qrcodes/{entry['itemId']}.png")
# img = qrcode.make('Some data here')
# type(img)  # qrcode.image.pil.PilImage
# img.save("qrcodes/some_file.png")