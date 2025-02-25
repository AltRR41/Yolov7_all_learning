import yaml

# YOLO eğitim veri seti için örnek data.yaml içeriği
data_config = {
    'train': '/content/yolov7/Duo_dataset/train/images',  # Eğitim görüntü dizini
    'val': '/content/yolov7/Duo_dataset/test/images',      # Doğrulama (validation) görüntü dizini
    'nc': 4,
    'names': ["holothurian", "echinus", "scallop", "starfish"]
}

# data.yaml dosyasını oluşturma ve yazma
with open('/content/yolov7/Duo_dataset/data.yaml', 'w') as file:
    yaml.dump(data_config, file, default_flow_style=False, allow_unicode=True)

print("data.yaml dosyası başarıyla oluşturuldu!")
