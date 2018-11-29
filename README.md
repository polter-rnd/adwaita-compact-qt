adwaita-compact-qt
==========

A native style to bend Qt4 and Qt5 applications to look like they belong into GNOME Shell with [Adwaita Compact](https://github.com/polter-rnd/adwaita-compact) theme.<br />
Look how default Adwaita and Adwaita Compact differ: [before](/screenshots/before.png) and [after](/screenshots/after.png).

## Widget examples

![Widgets](/screenshots/widgets.png)

## How to compile

The project uses the standard CMake buildsystem.

So for example, the whole compilation process could look like this:

```
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
make
make install
```

## Usage

After install, you'll be able to either set the theme as your default via your DE's tools (like `systemsettings` or `qt-config`) or start your qt applications with the `-style adwaita` parameter.
