echo on

XCOPY  E:\switch\support_repository\SeedSearcher\SeedSearcher\bin\Release\x64 E:\switch\support_repository\seed_release\SeedSearcher三合一\ /S/A/Y



del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher三合一\*.exp
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher三合一\*.pdb
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher三合一\*.ipdb
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher三合一\*.xml
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher三合一\*.config
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher三合一\*.lib
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher三合一\*.iobj
del /a /f /s /q  E:\switch\support_repository\seed_release\SeedSearcher三合一\*.obj


pause