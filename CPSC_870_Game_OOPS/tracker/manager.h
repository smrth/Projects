#include <SDL.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>

#include "ioManager.h"
#include "clock.h"
#include "sound.h"
#include "gamedata.h"
#include "sprite.h"
#include "world.h"
#include "viewport.h"
#include "multisprite.h"
#include "collisionStrategy.h"
#include "player.h"
#include "explodingSprite.h"
#include "bullet.h"
#include "menuManager.h"

class Manager {
public:
  Manager ();
  ~Manager ();
  void play();

private:
  const bool env;
  const Gamedata* gdata;
  const IOManager& io;
  Clock& clock;
  SDLSound sound;
  frameFactory& sprites;

  SDL_Surface *screen;
  World backWorld;
  World frontWorld;
  Viewport& viewport;
  
  std::vector<MultiframeSprite *> orbs;
  std::vector<MultiframeSprite *> expoorbs;
  std::vector<const MultiframeSprite *> player_track;
  std::vector<Bullet *> bullet;


  Player player;
  Player villan;
  CollisionStrategy *collisionStrategy;
  bool collisionFound;
  bool collisionVFound;
  bool collisionBFound;
  bool orbExploded;
  bool orbVExploded;
  bool orbLExploded;
  bool cheat;
  bool villan_die;
  bool menu_switch;
  bool music;
  bool music_switch;
  
  unsigned currentOrb;
  unsigned help_key;
  unsigned start_time;
  int level;
  

  void makeOrb(const string &);
  void addPlayer(const MultiframeSprite*);
  void makelsystem();
  void makeBomb(const string &);
  void makebullet();
  
  void draw() const;
  void update(Uint32);
  void checkForCollisionsVBP();
  void checkForCollisionsPBVB();
  void checkForCollisionsPBV();
  Manager(const Manager&);
  Manager& operator=(const Manager&);
  void explodecheck();
  void explodeVcheck();
  void shootvillan();
};
