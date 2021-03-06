#include <cmath>
#include <sstream>
#include <stdarg.h>
#include "menuManager.h"


MenuManager::~MenuManager() { 
  SDL_FreeSurface(backSurface);
  SDL_FreeSurface(screen);
}

MenuManager::MenuManager() :
  env( SDL_putenv(const_cast<char*>("SDL_VIDEO_CENTERED=center")) ),
  screen( IOManager::getInstance().getScreen() ),
  io(IOManager::getInstance()),
  bakColor(),
  backSurface( io.loadAndSet(Gamedata::getInstance()->getXmlStr("backgroundmenuSpriteFile"), true) ),
  viewport(Viewport::getInstance()),
  menu(),
  numberOfStars(Gamedata::getInstance()->getXmlInt("gamemaxBullet")),
  levels(Gamedata::getInstance()->getXmlInt("gamedefaultLevel")),
  music(true),
  cheat(false)
{ 
  bakColor.r = Gamedata::getInstance()->getXmlInt("backgroundRed");
  bakColor.g = Gamedata::getInstance()->getXmlInt("backgroundGreen");
  bakColor.b = Gamedata::getInstance()->getXmlInt("backgroundBlue");
  atexit(SDL_Quit); 
}

void MenuManager::drawBackground() const {
  //SDL_FillRect( screen, NULL, 
    //SDL_MapRGB(screen->format, bakColor.r, bakColor.g, bakColor.b) );
  SDL_Rect dest = {0, 0, 0, 0};
  SDL_BlitSurface( backSurface, NULL, screen, &dest );
}

void MenuManager::getPlayerName() {
  //IOManager& io = IOManager::getInstance().getInstance();
  SDL_Event event;
  bool done = false;
  bool nameDone = false;
  const string msg("Enemy Bullet # : ");
  while ( not done ) {
    Uint8 *keystate = SDL_GetKeyState(NULL);
    if ( SDL_PollEvent(&event) )
    switch (event.type) {
      case SDL_KEYDOWN: {
        if (keystate[SDLK_ESCAPE] || keystate[SDLK_q]) {
          done = true;
          break;
        }
        if (keystate[SDLK_RETURN]) {
          nameDone = true;
        }
        io.buildString(event);
      }
    }
    drawBackground();
    io.printStringAfterMessage(msg, 240, 120);
    if ( nameDone ) {
      io.printStringAfterMessage("Okay -- you're gonna get ", 20, 150);
      std::string number = io.getString();
      std::stringstream strm;
      strm << number;
      strm >> numberOfStars;
      SDL_Delay(250);
      done = true;
    }
    SDL_Flip(screen);
  }
}

void MenuManager::getLevel() {
  //IOManager& io = IOManager::getInstance().getInstance();
  SDL_Event event;
  bool done = false;
  bool nameDone = false;
  const string msg("Choose Levels :");
  while ( not done ) {
    Uint8 *keystate = SDL_GetKeyState(NULL);
    if ( SDL_PollEvent(&event) )
    switch (event.type) {
      case SDL_KEYDOWN: {
        if (keystate[SDLK_ESCAPE] || keystate[SDLK_q]) {
          done = true;
          break;
        }
        if (keystate[SDLK_RETURN]) {
          nameDone = true;
        }
        io.buildString(event);
      }
    }
    drawBackground();
    io.printStringAfterMessage("Choose Levels(1/2/3) : ", 220, 120);
    if ( nameDone ) {
      io.printStringAfterMessage("Okay -- you're gonna get ", 20, 150);
      std::string number1 = io.getString();
      std::stringstream strm;
      strm << number1;
      strm >> levels;
      SDL_Delay(250);
      done = true;
    }
    SDL_Flip(screen);
  }
}


void MenuManager::getCheatInfo()
{
  IOManager& io = IOManager::getInstance().getInstance();
  SDL_Event event;
  bool done = false;
  while ( not done ) {
    Uint8 *keystate = SDL_GetKeyState(NULL);
    if ( SDL_PollEvent(&event) )
    switch (event.type) {
      case SDL_KEYDOWN: {
        if (keystate[SDLK_ESCAPE] || keystate[SDLK_q]) {
          done = true;
          break;
        }
        io.buildString(event);
      }
    }
    drawBackground();
    string msg="Cheat is : ";
    io.printStringAfterMessage(msg, 240, 120);
    string ch= cheat? "Enabled" : "Disabled";
    io.printStringAfterMessage(ch, 320, 120);
    SDL_Flip(screen);
  }
}

void MenuManager::getMusicInfo()
{
 IOManager& io = IOManager::getInstance().getInstance();
  SDL_Event event;
  bool done = false;
  while ( not done ) {
    Uint8 *keystate = SDL_GetKeyState(NULL);
    if ( SDL_PollEvent(&event) )
    switch (event.type) {
      case SDL_KEYDOWN: {
        if (keystate[SDLK_ESCAPE] || keystate[SDLK_q]) {
          done = true;
          break;
        }
        io.buildString(event);
      }
    }
    drawBackground();
    string msg="Music is : ";
    io.printStringAfterMessage(msg, 240, 120);
    string ch= music? "Enabled" : "Disabled";
    io.printStringAfterMessage(ch, 320, 120);
    SDL_Flip(screen);
}
}


void MenuManager::getHelp()
{
IOManager& io = IOManager::getInstance().getInstance();
  SDL_Event event;
  bool done = false;
  while ( not done ) {
    Uint8 *keystate = SDL_GetKeyState(NULL);
    if ( SDL_PollEvent(&event) )
    switch (event.type) {
      case SDL_KEYDOWN: {
        if (keystate[SDLK_ESCAPE] || keystate[SDLK_q]) {
          done = true;
          break;
        }
        io.buildString(event);
      }
    }
    drawBackground();
    string msg="Help";
    io.printStringAfterMessage(msg, 220, 120);
    string ch= "Use Arrows(Right/Left) to move Ninja(Player)";
    io.printStringAfterMessage(ch, 220, 140);
    io.printStringAfterMessage("f to Fire Bullets", 220, 160);
    io.printStringAfterMessage("Press esc to start game", 220, 190);
    SDL_Flip(screen);
}
}

bool MenuManager::play() {
  bool keyCatch = false; // To get only 1 key per keydown
  SDL_Event event;
  bool done = false;
  bool returnKey = false;

  while ( not done ) {
    viewport.update(0,0);
    drawBackground();
    menu.draw();
    SDL_Flip(screen);

    SDL_PollEvent(&event);
    if (event.type ==  SDL_QUIT) { break; }
    if(event.type == SDL_KEYDOWN) {
      switch ( event.key.keysym.sym ) {
        case SDLK_ESCAPE : { done = true; } break;
        case SDLK_q      : { done = true; }break;
        case SDLK_RETURN : {
          if ( !keyCatch ) {
            menu.lightOn();
            returnKey = true;
          }
          break;
        }
        case SDLK_DOWN   : {
          if ( !keyCatch ) {
            menu.increment();
          }
          break;
        }
        case SDLK_UP   : {
          if ( !keyCatch ) {
            menu.decrement();
          }
          break;
        }
        default          : break;
      }
      keyCatch = true;
    }
    if(event.type == SDL_KEYUP) { 
      keyCatch = false; 
      if ( returnKey ) {
        returnKey = false;
        cout << "Chosen: " << menu.getIconClicked() << endl;
        SDL_Delay(250);
        if ( menu.getIconClicked() == "Exit" ) {
          done = true;
	  return done;
	  break;
        }
        else if ( menu.getIconClicked() == "Start Game" ) {
          done = true;
	  return false;
        }
        else if ( menu.getIconClicked() == "Level" ) {
          getLevel();
	  return false;
        }
        else if ( menu.getIconClicked() == "Help" ) {
          getHelp();
	  return false;
        }
        else if ( menu.getIconClicked() == "Parameters" ) {
          getPlayerName();
	  return false;
        }
        else if ( menu.getIconClicked() == "Music On/Off" ) {
          if(music==false){music=true;}
          else{music=false;}
          getMusicInfo();
	  return false;
        }
        else if ( menu.getIconClicked() == "Cheat On/Off" ) {
          if(cheat==false){cheat=true;}
          else{cheat=false;}
          getCheatInfo();
	  return false;
        }
      }
      menu.lightOff();
    }
  }
  return done;
}
