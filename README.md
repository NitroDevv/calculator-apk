# Kalkulyator Mobil Ilovasi (APK)

Ushbu loyiha Python va Flet yordamida yaratilgan. Uni Android (APK) formatiga o'tkazish uchun eng oson yo'l - GitHub Actions dan foydalanish.

## 1-qadam: GitHub ga yuklash
Ushbu papkadagi barcha fayllarni GitHub repozitoriysiga yuklang.

## 2-qadam: Build (Yig'ish)
GitHub Actions avtomatik ravishda ishga tushishi va APK faylini yaratishi uchun `.github/workflows/build.yml` fayli kerak bo'ladi (men buni tayyorlab beraman).

## Agar kompyuteringizda qilmoqchi bo'lsangiz:
Sizga quyidagilar kerak bo'ladi:
1. Python 3.8+
2. Flutter SDK
3. Android SDK (Android Studio orqali)

Bular o'rnatilgan bo'lsa, terminalda quyidagi buyruqni bering:
```bash
flet build apk
```
Lekin eng osoni - GitHub Actions.
