# sistema-inventario
Sistema web para la gestión de inventarios de un comercio electrónico.


Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~
$ git clone https://github.com/1MariaJose3/sistema-inventario.git
Cloning into 'sistema-inventario'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (4/4), done.

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~
$ cd sistema-inventario

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~/sistema-inventario (main)
$ git branch
* main

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~/sistema-inventario (main)
$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/feature/registro-productos
  remotes/origin/main

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~/sistema-inventario (main)
$ git switch feature/registro-productos
Switched to a new branch 'feature/registro-productos'
branch 'feature/registro-productos' set up to track 'origin/feature/registro-productos'.

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~/sistema-inventario (feature/registro-productos)
$ git branch
* feature/registro-productos
  main

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~/sistema-inventario (feature/registro-productos)
$ git status
On branch feature/registro-productos
Your branch is up to date with 'origin/feature/registro-productos'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        src/

nothing added to commit but untracked files present (use "git add" to track)

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~/sistema-inventario (feature/registro-productos)
$ git add .

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~/sistema-inventario (feature/registro-productos)
$ git commit -m "Agregar clase Producto"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'Dev2026Iot7@DESKTOP-DQNCRN5.(none)')

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~/sistema-inventario (feature/registro-productos)
$ git push origin feature/registro-productos
Everything up-to-date

Dev2026Iot7@DESKTOP-DQNCRN5 MINGW64 ~/sistema-inventario (feature/registro-productos)
$
