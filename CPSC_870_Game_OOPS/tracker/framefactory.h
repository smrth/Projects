#include <SDL.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>

#include "ioManager.h"
#include "gamedata.h"
#include "sprite.h"
#include "lsystem.h"

class frameFactory{
public:
 frameFactory();
 frameFactory(const frameFactory&);
  ~frameFactory();
  static frameFactory& getInstance();
  void setSurface(const string& s, const string& filename);
  SDL_Surface * getSurface(const string & );
  std::vector<Frame* >& setFrame(const string& s, unsigned start=0,unsigned end=0);
  
  LSystem* getLsystem(const string& name );
  std::vector<Frame*> getLsystemFrame(const std::string& name);
  

private:

  const Gamedata* gdata;
  const IOManager& io;

  std::map<string,SDL_Surface * > surfaceMap;
  std::vector<Frame*> spriteFrame;  
  std::map<string,std::vector<Frame*> > frameMap;
  std::map<std::string, std::vector<Frame*> > lsysFrames;
  std::map<std::string, LSystem*> lsystems;
  frameFactory& operator=(const frameFactory&);
};
