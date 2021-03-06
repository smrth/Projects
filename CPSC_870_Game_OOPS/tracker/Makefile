
ifeq ("$(shell whoami)", "zozo")
  CXX = clang++
else
  CXX = g++
endif
CXX_LINK = g++

# Warnings frequently signal eventual errors:
CXXFLAGS=`sdl-config --cflags` -g -W -Wall -Weffc++ -Wextra -pedantic -O0
LDFLAGS = `sdl-config --libs` -lSDL_ttf -lSDL_image -lSDL_mixer -lexpat

OBJS = \
	main.o \
	viewport.o \
	world.o \
	manager.o \
	menu.o \
	menuManager.o \
	gamedata.o \
        framefactory.o \
	parseXML.o \
	parseLsysXML.o \
	aaline.o \
	lsystem.o \
	clock.o \
	vector2f.o \
	sprite.o \
	explodingSprite.o \
	chunk.o \
	player.o \
	collisionStrategy.o \
	frame.o \
	sound.o\
	ioManager.o \
        multisprite.o 

EXEC = run

# $< refers to the first dependency
%.o: %.cpp
	$(CXX_LINK) $(CXXFLAGS) -c $< -o $@

# $@ refers to the target
$(EXEC): $(OBJS)
	g++ $(CXXFLAGS) -o $@ $(OBJS) $(LDFLAGS)

main.o: main.cpp
manager.o: manager.cpp manager.h gamedata.h ioManager.h sprite.h clock.h multisprite.h sound.h player.h collisionStrategy.h bullet.h
ioManager.o: ioManager.cpp ioManager.h
viewport.o: viewport.cpp viewport.h
world.o: world.cpp world.h
parseXML.o: parseXML.cpp parseXML.h
parseLsysXML.o: parseLsysXML.cpp parseLsysXML.h
framefactory.o: framefactory.cpp framefactory.h ioManager.o gamedata.h sprite.h lsystem.h
aaline.o: aaline.cpp aaline.h
lsystem.o: lsystem.cpp lsystem.h ioManager.h parseLsysXML.h
gamedata.o: gamedata.cpp gamedata.h parseXML.h
clock.o: clock.cpp clock.h
sound.o: sound.cpp sound.h
vector2f.o: vector2f.cpp vector2f.h
frame.o: frame.cpp frame.h
sprite.o: sprite.cpp sprite.h drawable.h frame.h
explodingSprite.o: explodingSprite.cpp explodingSprite.h chunk.h multisprite.h
chunk.o: chunk.cpp chunk.h sprite.h gamedata.h
player.o: player.cpp player.h sprite.h framefactory.h
frame.o: frame.cpp frame.h ioManager.h
multisprite.o: multisprite.cpp multisprite.h gamedata.h
menuManager.o: menuManager.cpp menuManager.h
menu.o: menu.cpp menu.h frame.h

clean:
	rm -rf $(OBJS)
	rm -rf $(EXEC)
