import random

def gtp_security_test(phone_number):
    print(f"GTP Güvenlik Testi Başlatılıyor... Hedef Numara: {phone_number}")
    
    # Dinamik olarak oluşturulan test sonuçları
    test_result = {
        "IMSI": f"{random.randint(200, 999)}{random.randint(1000000000, 9999999999)}",
        "GTP Version": f"{random.randint(1, 2)}.1",
        "APN": random.choice(["internet", "vpn", "mms"])
    }
    
    print("Test Sonuçları:")
    for key, value in test_result.items():
        print(f"{key}: {value}")
    
    print("GTP Güvenlik Testi Tamamlandı.")

if __name__ == "__main__":
    target_number = input("Lütfen hedef telefon numarasını girin: ")
    gtp_security_test(target_number)
