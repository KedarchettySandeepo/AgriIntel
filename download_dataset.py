from pathlib import Path
import requests
import zipfile

BASE = Path(__file__).resolve().parent
DATASET = BASE / "dataset"
RAW = DATASET / "raw"
ZIP_FILE = RAW / "plantvillage.zip"
EXTRACTED = RAW / "extracted"

# Dataset download URL
URL = "https://huggingface.co/datasets/mohanty/PlantVillage/resolve/main/data.zip"

print("Project:", BASE)
print("Dataset:", DATASET)

# Create folders
RAW.mkdir(parents=True, exist_ok=True)
EXTRACTED.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# DOWNLOAD DATASET
# --------------------------------------------------

if not ZIP_FILE.exists():

    print()
    print("Downloading PlantVillage dataset...")
    print("This may take some time because the dataset is large.")
    print()

    response = requests.get(
        URL,
        stream=True,
        timeout=60
    )

    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    downloaded = 0

    with open(ZIP_FILE, "wb") as file:

        for chunk in response.iter_content(chunk_size=1024 * 1024):

            if chunk:
                file.write(chunk)
                downloaded += len(chunk)

                if total_size:
                    percent = downloaded * 100 / total_size
                    print(
                        f"\rDownloaded: {percent:.1f}%",
                        end=""
                    )

    print()
    print("Download completed.")

else:

    print()
    print("Dataset ZIP already exists.")
    print("Skipping download.")

# --------------------------------------------------
# EXTRACT DATASET
# --------------------------------------------------

if not any(EXTRACTED.iterdir()):

    print()
    print("Extracting dataset...")

    with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(EXTRACTED)

    print("Extraction completed.")

else:

    print()
    print("Dataset is already extracted.")

# --------------------------------------------------
# CREATE YOLO FOLDERS
# --------------------------------------------------

for split in ["train", "val", "test"]:

    (DATASET / split / "images").mkdir(
        parents=True,
        exist_ok=True
    )

    (DATASET / split / "labels").mkdir(
        parents=True,
        exist_ok=True
    )

print()
print("Dataset preparation completed.")

print()
print("Extracted dataset location:")
print(EXTRACTED)

print()
print("Next step:")
print("We will inspect the extracted folders.")
print("Then we will convert the dataset into YOLO format.")