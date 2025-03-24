# Droid's Toolbox
Droid has a toolbox app that he uses sometimes. I heard he is hiding something in it, go check it out!

Note: This challenge requires an Android device, running Android 8.0 Oreo and above, that passes Google Play Integrity API checks.

## Summary
- **Author:** czlucius
- **Category:** reversing
- **Difficulty:** impossible
- **Finals:** True
- **Tags:** mobile

## Hints
- `Decompile the APK. You can try jadx, or dex2jar+procyon` (100 points)
- `The flag is encrypted with 2048-bit RSA. The private key is stored in Android Keystore.` (50 points)
- `Android's keystore is built to be secure, don't try to extract any keys from a modern device; it probably won't work` (150 points)
- `Have you thought of the application signature? ` (200 points)

## Files
- [app-release.apk](<dist/app-release.apk>)
- [server-source.zip](<dist/server-source.zip>)

## Flags
- `YBN24{4PP_S19NATUR3S_4R3_1MP0RT4NT}` (static, case-insensitive)

## Services
| [`server`](<service/server>) | None | internal |
