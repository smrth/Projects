#include <cmath>
#include "sprite.h"
#include "multisprite.h"
#include <vector>

class CollisionStrategy {
public:
  virtual bool execute(const MultiframeSprite&, const MultiframeSprite&) const = 0;
  virtual void draw() const = 0;
  virtual ~CollisionStrategy() {}
};

class RectangularCollisionStrategy : public CollisionStrategy {
public:
  RectangularCollisionStrategy() {}
  virtual bool execute(const MultiframeSprite&, const MultiframeSprite&) const;
  virtual void draw() const;
};

class MidPointCollisionStrategy : public CollisionStrategy {
public:
  MidPointCollisionStrategy() {}
  virtual bool execute(const MultiframeSprite&, const MultiframeSprite&) const;
  virtual void draw() const;
  float distance(float, float, float, float) const;
};

class PerPixelCollisionStrategy : public CollisionStrategy {
public:
  PerPixelCollisionStrategy() {}
  virtual bool execute(const MultiframeSprite&, const MultiframeSprite&) const;
  virtual void draw() const;
};

