# INSAVentil
Calculates statistics based on the choices of students for majors at INSA LYON.

The app is actually a script called every x seconds checking for new info from the website, and printing out a new graph if it's the case.

The graph is then sent to a server (server/) which automatically updates a database and displays the latest graph.

The result can be seen at the following link : http://cles-facil.fr/insa/ventil.php

# Stack
Beautiful client written in Python (with love <3).
Minimalistic server written in PHP (chosen for its simplicity, and because I only have a LAMP server) using MySQL.
