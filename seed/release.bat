echo on

XCOPY  E:\switch\support_repository\SeedSearcher\SeedSearcher\bin\Release\x64 E:\switch\support_repository\seed_release\SeedSearcher����һ\ /S/A/Y



del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher����һ\*.exp
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher����һ\*.pdb
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher����һ\*.ipdb
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher����һ\*.xml
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher����һ\*.config
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher����һ\*.lib
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher����һ\*.iobj
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher����һ\*.obj


pause