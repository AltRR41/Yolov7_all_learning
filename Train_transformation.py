import json
import os
import shutil

#Her şeyden önce yeni bir başlangıç için boş klasör
dataset_yol = "/content/yolov7/Duo_dataset"
os.makedirs('dataset_yol')

# COCO JSON ve Görüntü Klasörü
coco_json_path = "/content/drive/MyDrive/Bitirme 2025/Supervised Deneme/DUO/annotations/instances_train.json"
image_dir = "/content/drive/MyDrive/Bitirme 2025/Supervised Deneme/DUO/images/train"
output_dir = "/content/yolov7/Duo_dataset/train"

# Çıktı klasörlerini oluştur
os.makedirs(f"{output_dir}/images", exist_ok=True)
os.makedirs(f"{output_dir}/labels", exist_ok=True)

# COCO JSON'u oku
with open(coco_json_path, "r") as f:
    data = json.load(f)

images = {img["id"]: img for img in data["images"]}
print(f"Toplam {len(images)} görüntü işlenecek...")

# Etiketleri YOLO formatına çevir ve dosyaları kopyala
for i, (img_id, img_info) in enumerate(images.items()):
    if i >= 100:  # İlk 100 veriyle test yap (daha sonra kaldır)
        break

    img_w, img_h = img_info["width"], img_info["height"]
    label_path = os.path.join(output_dir, "labels", img_info["file_name"].replace('.jpg', '.txt'))

    # Aynı image_id'ye ait tüm anotasyonları topla
    annotations = [ann for ann in data["annotations"] if ann["image_id"] == img_id]

    with open(label_path, "w") as f:  # "a" yerine "w" ile tek seferde yaz
        for ann in annotations:
            class_id = ann["category_id"] - 1  # YOLO sınıf ID'si 0'dan başlar
            x, y, w, h = ann["bbox"]
            x_center = (x + w / 2) / img_w
            y_center = (y + h / 2) / img_h
            w /= img_w
            h /= img_h
            f.write(f"{class_id} {x_center} {y_center} {w} {h}\n")

    # Görüntüyü yeni klasöre taşı
    source_path = os.path.join(image_dir, img_info["file_name"])
    dest_path = os.path.join(output_dir, "images", img_info["file_name"])

    if os.path.exists(source_path):
        shutil.copy(source_path, dest_path)
    else:
        print(f"⚠️ Dosya bulunamadı: {source_path}")

print("✅ COCO'dan YOLO formatına dönüştürüldü ve dosyalar tek klasörde birleştirildi!")
