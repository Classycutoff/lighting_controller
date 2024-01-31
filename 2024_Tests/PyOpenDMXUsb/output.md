D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources>dotnet new console -o TestConsoleApp

Welcome to .NET 7.0!
---------------------
SDK Version: 7.0.102

Telemetry
---------
The .NET tools collect usage data in order to help us improve your experience. It is collected by Microsoft and shared with the community. You can opt-out of telemetry by setting the DOTNET_CLI_TELEMETRY_OPTOUT environment variable to '1' or 'true' using your favorite shell.

Read more about .NET CLI Tools telemetry: https://aka.ms/dotnet-cli-telemetry

----------------
Installed an ASP.NET Core HTTPS development certificate.
To trust the certificate run 'dotnet dev-certs https --trust' (Windows and macOS only).
Learn about HTTPS: https://aka.ms/dotnet-https
----------------
Write your first app: https://aka.ms/dotnet-hello-world
Find out what's new: https://aka.ms/dotnet-whats-new
Explore documentation: https://aka.ms/dotnet-docs
Report issues and find source on GitHub: https://github.com/dotnet/core
Use 'dotnet --help' to see available commands or visit: https://aka.ms/dotnet-cli
--------------------------------------------------------------------------------------
The template "Console App" was created successfully.

Processing post-creation actions...
Restoring D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources\TestConsoleApp\TestConsoleApp.csproj:
  Determining projects to restore...
  Restored D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources\TestConsoleApp\TestConsoleApp.csproj (in 86 ms).
Restore succeeded.



D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources>dir
 Volume in drive D is Eliel_Storage
 Volume Serial Number is 5A15-E818

 Directory of D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources

31/01/2024  01.45    <DIR>          .
31/01/2024  01.45    <DIR>          ..
31/01/2024  01.33             4 778 DMXClient.py
31/01/2024  01.33            21 519 DMXServer.cs
31/01/2024  01.36               336 main.py
31/01/2024  01.45    <DIR>          TestConsoleApp
               3 File(s)         26 633 bytes
               3 Dir(s)  209 768 648 704 bytes free

D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources>

-----------------

Windows PowerShell


PS D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources> .\DMXServer.cs -n PODU
PS D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources> Code .
PS D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources> cd .\TestConsoleApp\
PS D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources\TestConsoleApp> Code .
PS D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources\TestConsoleApp> dotnet run --project TestConsoleApp
MSBUILD : error MSB1009: Project file does not exist.
Switch: TestConsoleApp

The build failed. Fix the build errors and run again.
PS D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources\TestConsoleApp> cd ..
PS D:\Opinnot\2023_Oppari\PyOpenDmxUsb-v.1.1.1-sources> dotnet run --project TestConsoleApp
Hello, World!

--------------------

