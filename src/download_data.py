import os

def download_titanic():
    os.makedirs("data", exist_ok=True)
    os.system("kaggle competitions download -c titanic -p data/")
    os.system("unzip -o data/titanic.zip -d data/")
    print("✔ Titanic dataset downloaded into the data/ folder.")

if __name__ == "__main__":
    download_titanic()