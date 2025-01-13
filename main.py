import os
from dotenv import load_dotenv
from jira import JIRA

load_dotenv()

jira_url = os.getenv('JIRA_URL')
jira_username = os.getenv('JIRA_USERNAME')
jira_token = os.getenv('JIRA_API_TOKEN')

jira = JIRA(jira_url, basic_auth=(jira_username, jira_token))
issue_key = "ARZ-3214"

issue= jira.issue(issue_key)

#Açık 10032
#Çalışılıyor 10047
#Kapandı 10049
#Çözüldü 10048
#Talep Sahibinden Bilgi Bekleniyor 10052

try:
    if issue.fields.status.id == "10032":   #Açık
        transition_id = "171"  #Üstlen
        jira.transition_issue(issue_key, transition_id)
        print(f"{issue_key} üstlendi.")

        transition_id = "11"    #Çalışılıyor
        jira.transition_issue(issue_key, transition_id)
        print(f"{issue_key} çalışılıyor.")

        transition_id = "21"  # Çözüldü
        jira.transition_issue(issue_key, transition_id,comment="Gerekli yetkiler verilmiştir, işleminize devam edebilirsiniz.")
        print(f"{issue_key} çözüldü.")

        transition_id = "31"  # Kapatıldı
        jira.transition_issue(issue_key, transition_id)
        print(f"{issue_key} kapandı.")

    if issue.fields.status.id == "10047":   #Çalışılıyor
        transition_id = "21"    #Çözüldü
        jira.transition_issue(issue_key, transition_id,comment="Gerekli yetkiler verilmiştir, işleminize devam edebilirsiniz.")
        print(f"{issue_key} çözüldü.")
        transition_id = "31"  # Kapatıldı
        jira.transition_issue(issue_key, transition_id)
        print(f"{issue_key} kapandı.")

    if issue.fields.status.id == "10048":   #Çözüldü
        transition_id = "31"  # Kapatıldı
        jira.transition_issue(issue_key, transition_id)
        print(f"{issue_key} kapandı.")

    if issue.fields.status.id == "10052":   #Talep Sahibinden Bilgi Bekleniyor
        transition_id = "131"  # İptal Edildi
        jira.transition_issue(issue_key, transition_id,comment="Gerekli yetkiler verilmiştir, işleminize devam edebilirsiniz.")
        print(f"{issue_key} iptal edildi.")

except Exception as e:
    print(f"Hata oluştu: {e}")
