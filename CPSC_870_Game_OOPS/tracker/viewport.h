#ifndef VIEWPORT__H
#define VIEWPORT__H
#include "sprite.h"
#include "gamedata.h"
#include "multisprite.h"

class Viewport {
public:
  static Viewport& getInstance();
  ~Viewport() { std::cout << "Blocking the view ..." << std::endl; }
  void update( const float, const float);
  void update( );

  float X() const { return position[0]; }
  void X(float x) { position[0] = x; }
  float Y() const { return position[1]; }
  void Y(float y) { position[1] = y; }

  void setObjectToTrack(const MultiframeSprite *obj);
  const MultiframeSprite* getObjectToTrack() const { return objectToTrack; } 

private:
  Gamedata* const gdata;
  Vector2f position;
  unsigned viewWidth;
  unsigned viewHeight;
  unsigned worldWidth;
  unsigned worldHeight;
  Uint16 objWidth;
  Uint16 objHeight;
  
  const MultiframeSprite* objectToTrack;

  Viewport();
  Viewport(const Viewport&);
  Viewport& operator=(const Viewport&);
};
#endif
