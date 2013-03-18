#ifndef MULTISPRITE__H
#define MULTISPRITE__H

#include <string>
#include <iostream>
#include <vector>
using std::string;

#include "drawable.h"
#include "frame.h"
#include "gamedata.h"

class MultiframeSprite : public Drawable {
public:
  MultiframeSprite(const Vector2f& pos, const Vector2f& vel,
         const string& n, const std::vector<Frame*>& fms,const int frameNumber,const int frameInterval);
  MultiframeSprite(const MultiframeSprite& s);
  
  const string& getName() const { return name; }
  void setName(const string& n) { name = n; }
  
  const unsigned& getcurrentFrame() const{ return currentFrame; }
  void setcurrentFrame(const unsigned& c){ currentFrame=c; }
  
  const unsigned& getnumberofFrame() const{ return numberOfFrames; }
  void setnumberofFrame(const unsigned& no){ numberOfFrames=no; }
  
  const unsigned& getframeInterval() const{ return frameInterval; }
  void setframeInterval(const unsigned& fi){ frameInterval=fi; }
  
  const float& getdt() const{ return dt; }
  void setdt(const float& d){ dt=d; }
 
 const std::vector<Frame *> getMFrame() const{ return frames; }
  const Frame * getFrame() const{ return frames[currentFrame]; }
  void setFrame(const std::vector<Frame *>& f){ frames=f; }

  virtual void draw() const;
  virtual void update(Uint32 ticks);
  unsigned getPixel(Uint32, Uint32) const;

  Vector2f getCenter() const { 
    return Vector2f( X()+frames[currentFrame]->getWidth()/2, Y()+frames[currentFrame]->getHeight()/2 );
  }

  MultiframeSprite& operator=(const MultiframeSprite& rhs);

private:
  const Gamedata* gdata;  
  string name;
  std::vector<Frame *> frames;
  float dt;
  unsigned currentFrame;
  unsigned numberOfFrames;
  unsigned frameInterval;
  void advanceFrame(Uint32 ticks);
  int getDistance(const MultiframeSprite*) const;
};
#endif
