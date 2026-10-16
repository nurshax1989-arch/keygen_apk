# AUTOCALL Keygen (Android APK)
Kompyuterdagi keygen.py bilan bir xil parol beradi. FAQAT SIZ uchun - APK ichida maxfiy kalit bor, mijozlarga bermang.

## APK olish (eng oson: GitHub, kompyuter/Linux kerak emas)
1. github.com da yangi PRIVATE repozitoriy oching va shu papkadagi hamma fayllarni (`.github` papkasi bilan) yuklang.
2. Repozitoriy > Actions > "Build APK" > Run workflow. 15-25 daqiqada tugaydi.
3. Tugagach "Artifacts" dan `AutoCallKeygen-apk` ni yuklab oling, ichidagi .apk ni telefonga o'rnating
   (Sozlamalar > "Noma'lum manbalardan o'rnatish"ga ruxsat bering).

## Linux/WSL'da o'zingiz yig'ish
    pip install buildozer "cython<3" && buildozer -v android debug      # bin/ papkada APK chiqadi
