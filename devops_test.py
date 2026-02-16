#Devops Envanter Listesi
env_listesi = ["Docker", "Kubernetes", "Jenkins"]

#Listeye yeni bir elema ekleyelim
env_listesi.append("Terraform")

#Bir sozluk olusturalim
user_info = {
    "name": "Developer",
    "city": "Bishkek",
    "target_city": "Istanbul"
}

print(f"{user_info['target_city']} yolculugunda kullanilacak araclar:{env_listesi}")

print("\n--- Araclar Tek Tek listeleniyor ---")
for arac in env_listesi:
    print(f"Kuruluma hazir: {arac}")

