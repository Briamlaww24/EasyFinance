#!/bin/bash


cp -r ../EasyFinance/ ~/.local/share/EasyFinance/


cat > ~/.local/share/EasyFinance/launch.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
./Interfaz.bin
EOF
chmod +x ~/.local/share/EasyFinance/launch.sh


cat > ~/.local/share/applications/EasyFinance.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=EasyFinance
Comment=Gestor de finanzas de tu tienda online
Exec=$HOME/.local/share/EasyFinance/launch.sh
Icon=$HOME/.local/share/EasyFinance/icono.png
Terminal=false
Categories=Utility;Office;
Keywords=EasyFinance;Finanzas;lanzador;
EOF

chmod +x ~/.local/share/applications/EasyFinance.desktop
update-desktop-database ~/.local/share/applications/

echo "EasyFinance Instalado Correctamente"   


