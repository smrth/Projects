#include "ioManager.h"
#include "lsystemSprite.h"
#include "frameFactory.h"

LsystemSprite::LsystemSprite( const string& name ) :
  Sprite(Vector2f(Gamedata::getInstance()->getXmlInt(name+"X"), 
                  Gamedata::getInstance()->getXmlInt(name+"Y")), 
         getNewVelocity(name),
         name, 
         FrameFactory::getInstance().getLsystemFrame(name)
        ), 
  lsystem(FrameFactory::getInstance().getLsystem("lsystem"))
{ }
