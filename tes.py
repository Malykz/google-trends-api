from google_trends.GoogleTrends import GoogleTrends
import json
import requests

from user_agent import generate_user_agent

def generate_navigator():
    return {
        "User-Agent": generate_user_agent(),
    }
if __name__ == "__main__":
    gt = GoogleTrends(geo="ID")  # ID = Indonesia
    trending_data = gt.result

    if trending_data:
        for trend in trending_data:
            print(f"Judul: {trend['title']}")
            print(f"Wilayah: {trend['region']}")
            print(f"Kategori: {trend['category']}")
            print(f"Volume Pencarian: {trend['searchVolume']}")
            print(f"Detail Breakdown: {trend['breakdown']}")
            print("-" * 30)
    else:
        print("Gagal mengambil data trending.")
