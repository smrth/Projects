#include <SDL.h>
#include <iostream>
#include <string>
#include <vector>

#include "sprite.h"

class Factory{

public:
virtual ~Factory(){}

private:
  virtual void makeframe();

};
