#include "player.h"



void Player::right() { 
  if ( playerSprite->X()) {
    //frameFactory::getInstance().setSurface("ninja","ninja_move");
    playerSprite->velocityX(250);
    playerSprite->setnumberofFrame(7);
  }
} 
void Player::left()  { 
  if ( playerSprite->X()) {
    //frameFactory::getInstance().setSurface("ninja","ninja_move");
    playerSprite->velocityX(-250);
    playerSprite->setnumberofFrame(7);
  }
} 
void Player::up()    { 
  if ( playerSprite->Y()) {
    //frameFactory::getInstance().setSurface("ninja","ninja_move");
    playerSprite->velocityY(-250);
    playerSprite->setnumberofFrame(7);
  }
} 
void Player::down()  { 
  if ( playerSprite->Y()<(Gamedata::getInstance()->getXmlInt("viewHeight")-150)) {
    //frameFactory::getInstance().setSurface("ninja","ninja_move");
    playerSprite->velocityY(250);
    playerSprite->setnumberofFrame(7);
  }
} 
