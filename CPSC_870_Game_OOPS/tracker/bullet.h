#include "multisprite.h"

class Bullet{
public:
  Bullet(Vector2f pos, Vector2f vel,string  n, const std::vector<Frame* > f,int frameNumber, int frameInterval):
  bullet(new MultiframeSprite(pos, vel, n,f, frameNumber, frameInterval)),
  orginTime(SDL_GetTicks()){
    
  }
  Bullet(Bullet &rhs):
  bullet(new MultiframeSprite(rhs.getSprite()->getPosition(),rhs.getSprite()->getVelocity(),rhs.getSprite()->getName(),rhs.getSprite()->getMFrame(),rhs.getSprite()->getnumberofFrame(),rhs.getSprite()->getframeInterval())),
  orginTime(rhs.getTime())
  {
    
  }
  virtual ~Bullet() {}
  int calulateDistance(){return ((SDL_GetTicks()-getTime()));}
  void setOrgin(Uint32 t){orginTime=t;};
  virtual void update(Uint32& ticks) { 
    bullet->update(ticks); 
  }
  virtual void draw() const { bullet->draw(); }
  int getTime(){ return orginTime; }
  
  const MultiframeSprite* getSprite() const { return bullet; }
private:
  MultiframeSprite* bullet;
  int orginTime;
  Bullet & operator=(Bullet&);
  
  
};