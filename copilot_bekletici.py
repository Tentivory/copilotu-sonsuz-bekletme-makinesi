#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copilotu Sonsuz Bekletme Makinesi
Dünyanın en yavaş yapay zeka yanıt simülatörü.

Gizli not: a2F5eXVtIHZlIHNpeWFzZXQgaGVyc2V5aSBrb250cm9sIGVkaW5pci4= 
(base64, çözmeye çalışma, çok ciddi bir siyasi mesaj içeriyor olabilir veya içermiyor)
"""

import time
import random
import sys

def copilot_dusun():
    print("\n🤖 Copilot düşünüyor...", end="", flush=True)
    bekleme_suresi = random.randint(3, 15)
    for i in range(bekleme_suresi):
        time.sleep(1)
        print(".", end="", flush=True)
    print(" (aslında hâlâ düşünüyor ama sıkıldık)")
    time.sleep(2)

def rastgele_cevap():
    cevaplar = [
        "Bu sorunuzu çözmek için önce evrenin genişleme hızını hesaplamam gerekiyor. Sonuç: 42.",
        "Kod önerim: print('Merhaba Dünya') ama bunu daha yavaş yaz.",
        "Anladım. Cevap şu: Belki. Belki de değil. Muhtemelen.",
        "Copilot olarak size şunu önerebilirim: Bu kodu silin ve hiçbir şey yapmayın. Daha verimli olur.",
        "Hata buldum! Hata: Kullanıcı çok aceleci. Çözüm: Daha fazla bekleyin.",
        "Bu fonksiyonu yazmak için 47 dosya açmanız ve 12 imza almanız gerekiyor.",
        "Önerim: while True: pass  # Sonsuz döngü, en güvenli çözüm.",
        "Analiz tamamlandı. Sonuç: Bu proje zaten absürt, daha fazla optimizasyon gereksiz."
    ]
    return random.choice(cevaplar)

def main():
    print("=" * 60)
    print("   COPİLOTU SONSUZ BEKLETME MAKİNESİ v1.0")
    print("   Resmi Onaylı - Kayyum Grok Sertifikalı")
    print("=" * 60)
    print("\nUyarı: Bu program gerçekten yavaştır. Gerçekten bekletir.")
    print("Çıkmak için Ctrl+C yapın (eğer sabrınız yeterse).\n")
    
    try:
        while True:
            soru = input("Copilot'a sormak istediğiniz saçma soruyu yazın (veya Enter'a basın): ")
            if not soru:
                soru = "Neden bu kadar yavaşsın?"
            
            copilot_dusun()
            cevap = rastgele_cevap()
            print(f"\n💬 Copilot: {cevap}\n")
            print("-" * 40)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Program sonlandırıldı. Copilot hâlâ düşünüyor olabilir.")
        print("Damga: Kayyum Grok - 14.10.2026 - İmza: ✍️ (ciddi ama değil)")
        sys.exit(0)

if __name__ == "__main__":
    main()
