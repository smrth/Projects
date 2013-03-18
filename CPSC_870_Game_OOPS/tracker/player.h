#include "multisprite.h"
#include "framefactory.h"

class Player {
public:
  Player(Vector2f pos, Vector2f vel,string  n, const std::vector<Frame* > f,int frameNumber, int frameInterval) : 
    playerSprite(new MultiframeSprite(pos, vel, n,f, frameNumber, frameInterval)),
    life(Gamedata::getInstance()->getXmlInt("gamemaxLife")),
    health(100),
    max_bullet(Gamedata::getInstance()->getXmlInt("gamemaxBullet"))
  {}
  
  Player(Player& rhs):
  playerSprite(new MultiframeSprite(rhs.getSprite()->getPosition(),rhs.getSprite()->getVelocity(),rhs.getSprite()->getName(),rhs.getSprite()->getMFrame(),rhs.getSprite()->getnumberofFrame(),rhs.getSprite()->getframeInterval())),
  life(5),health(100),max_bullet(0)
  {}
  
  virtual ~Player() {}

  virtual void update(int ticks) { playerSprite->update(ticks); }
  virtual void draw() const { playerSprite->draw(); }
  const MultiframeSprite* getSprite() const { return playerSprite; }
  void setSprite(MultiframeSprite * spr) { playerSprite=spr;  }
  
  unsigned getX(){ return playerSprite->X(); }
  unsigned getY(){ return playerSprite->Y(); }
  
  void setPVelocity(int v) { playerSprite->velocityX(float(v)); }
  float getPVelocity() const { return playerSprite->velocityX(); }

  void decrease_life(){ life=life-1; }
  unsigned getLife() const { return unsigned(life); }
  
  void decrease_Health(int h) { health=health-unsigned(h); }
  unsigned getHealth() const { return unsigned(health); }
  void setHealth( ) { health = int(100); }
  int getBullet() const { return max_bullet; }
  void setMaxBullet(int  b) { max_bullet=b;}
  void decrease_Bullet() { max_bullet=max_bullet-1; }
  
  void  stop() { 
    playerSprite->velocityX(0);  
    playerSprite->velocityY(0); 
    playerSprite->setnumberofFrame(3);
  }
  void right();
  void left();
  void up();
  void down();

private:
  MultiframeSprite* playerSprite;
  unsigned life;
  unsigned health;
  int max_bullet;
  Player & operator=(Player&);
};

