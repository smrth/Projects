#include <SDL.h>
#include <iostream>
#include <string>
#include "viewport.h"
using std::cout; using std::endl; 
using std::string;

#include "ioManager.h"
#include "menu.h"

class MenuManager {
public:
  MenuManager ();
  ~MenuManager ();
  bool play();
  int getNumberOfStars() const { return numberOfStars; }
  bool getMusic() const { return music; }
  bool getCheat() const { return cheat; }
  int getLevelno() const { return levels; }

private:
  bool env;

  SDL_Surface *screen;
  IOManager &io;
  SDL_Color bakColor;
  SDL_Surface *backSurface;
  Viewport &viewport;
  Menu menu;
  int numberOfStars;
  int levels;
  bool music;
  bool cheat;

  void drawBackground() const;
  MenuManager(const MenuManager&);
  MenuManager& operator=(const MenuManager&);
  void getPlayerName();
  void getLevel();
  void getCheatInfo();
  void getMusicInfo();
  void getHelp();
};
