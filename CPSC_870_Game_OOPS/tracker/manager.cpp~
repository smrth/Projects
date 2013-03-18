#include <cmath>
#include "manager.h"

Manager::~Manager() { 
  // These deletions eliminate "definitely lost" and
  // "still reachable"s in Valgrind.
  
  //delete player_track[0];
  delete collisionStrategy;
  delete villan.getSprite();
  delete player.getSprite();
  for (unsigned i = 0; i < unsigned(orbs.size()); ++i) {
    delete orbs[i];
  }
  SDL_FreeSurface(screen);
  delete Gamedata::getInstance();
}

Manager::Manager() :
  env( SDL_putenv(const_cast<char*>("SDL_VIDEO_CENTERED=center")) ),
  gdata( Gamedata::getInstance() ),
  io( IOManager::getInstance() ),
  clock( Clock::getInstance() ),
  sound(),
  sprites( frameFactory::getInstance() ),
  screen( io.getScreen() ),
  backWorld(frameFactory::getInstance().setFrame("background")[0], 2),
  frontWorld(frameFactory::getInstance().setFrame("foreground")[0], 1),
  viewport( Viewport::getInstance() ),
  orbs(),
  expoorbs(),
  player_track(),
  bullet(),
  player(Vector2f(gdata->getXmlInt("ninjaStandSpritePositionX"),gdata->getXmlInt("ninjaStandSpritePositionY")), 
          Vector2f(0, 0),"ninjaStand" ,frameFactory::getInstance().setFrame("ninjaStand"),gdata->getXmlInt("ninjaStandSpriteFrameNumber"),gdata->getXmlInt("ninjaStandSpriteFrameInterval")),
  villan(Vector2f(gdata->getXmlInt("villanSpritePositionX"),gdata->getXmlInt("villanSpritePositionY")), 
          Vector2f(150, 0),"villan" ,frameFactory::getInstance().setFrame("villan"),gdata->getXmlInt("villanSpriteFrameNumber"),gdata->getXmlInt("villanSpriteFrameInterval")),
  collisionStrategy( NULL ),
  collisionFound( false ) ,
  collisionVFound( false ) ,
  collisionBFound( false ) ,
  orbExploded(false),
  orbVExploded(false),
  orbLExploded(false),
  cheat(false),
  villan_die(false),
  menu_switch(false),
  music(false),
  music_switch(false),
  currentOrb(0),
  help_key(0),
  start_time(SDL_GetTicks()),
  level(gdata->getXmlInt("gamedefaultLevel")
  )
{
  if (SDL_Init(SDL_INIT_VIDEO) != 0) {
    throw string("Unable to initialize SDL: ");
  }
  collisionStrategy = new PerPixelCollisionStrategy();
  viewport.setObjectToTrack(player.getSprite());
  addPlayer(player.getSprite());
  addPlayer(villan.getSprite());
  makeBomb("bomb");
  atexit(SDL_Quit);
  SDL_WM_SetCaption( "Ninja Battle", NULL );
}

void Manager::addPlayer(const MultiframeSprite* sprite)
{
  player_track.push_back(sprite);
}


void Manager::makeOrb(const string & s){
for (unsigned int i=0;i<unsigned(gdata->getXmlInt(s+"Number"));i++){
	MultiframeSprite * spr=new MultiframeSprite(Vector2f(gdata->getXmlInt(s+"SpritePositionX"), 
                 gdata->getXmlInt(s+"SpritePositionY")), 
        Vector2f(gdata->getXmlInt(s+"SpriteVelocityX"),
                 gdata->getXmlInt(s+"SpriteVelocityY")), s, 
		 frameFactory::getInstance().setFrame(s),
		 gdata->getXmlInt(s+"SpriteFrameNumber"),
		 gdata->getXmlInt(s+"SpriteFrameInterval"));
  	orbs.push_back(spr);
  }

}


void Manager::makeBomb(const string & s){
	MultiframeSprite * spr=new MultiframeSprite(Vector2f(villan.getSprite()->X(), 
                 villan.getSprite()->Y()+60), 
        Vector2f(gdata->getXmlInt(s+"SpriteVelocityX"),
                 rand()%gdata->getXmlInt(s+"SpriteVelocityY")), s, 
		 frameFactory::getInstance().setFrame(s),
		 gdata->getXmlInt(s+"SpriteFrameNumber"),
		 gdata->getXmlInt(s+"SpriteFrameInterval"));
  	orbs.push_back(spr);
	//makelsystem();
}
void Manager::makelsystem(){
for (unsigned int i=0;i<unsigned(gdata->getXmlInt("lsystemNumber"));i++){
  	MultiframeSprite *spr=new MultiframeSprite(Vector2f(villan.getX(), 
                 villan.getY()+50), 
        Vector2f(gdata->getXmlInt("bombSpriteVelocityX"),
                 200), "lsystem", 
		 frameFactory::getInstance().getLsystemFrame("lsystem"),
		 gdata->getXmlInt("lsystemSpriteFrameNumber"),
		 gdata->getXmlInt("lsystemSpriteFrameInterval"));
	orbs.push_back(spr);
  }
}

void Manager::makebullet()
{
  if(!villan_die){
    bullet.push_back(new Bullet(Vector2f(player.getSprite()->X(),player.getSprite()->Y()+60), 
          Vector2f(gdata->getXmlInt("bulletSpriteVelocityX"), gdata->getXmlInt("bulletSpriteVelocityY")),"bullet" ,frameFactory::getInstance().setFrame("bullet"),gdata->getXmlInt("bulletSpriteFrameNumber"),gdata->getXmlInt("bulletSpriteFrameInterval")));
  }
}


// Coliison check between villans bullet and player
void Manager::checkForCollisionsVBP() {
  collisionFound = false;
  std::vector<MultiframeSprite *>::iterator orb = orbs.begin();
  while ( orb != orbs.end() ) {
    if ( collisionStrategy->execute(*(player.getSprite()), *(*orb)) ) {
      if(cheat!=true){ collisionFound = true; }
      if(player.getHealth()>0 and cheat!=true){
      player.decrease_Health(gdata->getXmlInt("gameDecrementSize"));
      }
    if(collisionFound){
    if ((dynamic_cast<MultiframeSprite*>(*orb))!=0) {
      MultiframeSprite *temp = static_cast <MultiframeSprite*> (*orb);
      MultiframeSprite *orb1=new ExplodingSprite(*temp);
      expoorbs.push_back(orb1);
      delete temp; 
      orb=orbs.erase(orb);
      }
      }
    }
    else{ ++orb; }
  }
}

// Coliison check between players bullet and villan
void Manager::checkForCollisionsPBV() {
  collisionVFound = false;
  std::vector<Bullet *>::iterator bull=bullet.begin();
  while ( bull != bullet.end() ) {
    if ( collisionStrategy->execute(*(villan.getSprite()), *(*bull)->getSprite()) ) {
      collisionVFound = true; 
      if(villan.getHealth()>0){
      villan.decrease_Health(gdata->getXmlInt("gameDecrementSize"));
      }
      }
      if(collisionVFound){
	if ((dynamic_cast<Bullet*>(*bull))!=0) {
	MultiframeSprite *temp1 = const_cast <MultiframeSprite*> ((*bull)->getSprite());
	MultiframeSprite *orb2=new ExplodingSprite(*temp1);
	expoorbs.push_back(orb2);
	delete temp1;
	bull=bullet.erase(bull);  
	}
      }
      if(bull==bullet.end()){break;}
      else{++bull;}
  }
}


void Manager::explodecheck()
{
  if(collisionFound == true && cheat != true)
  {
    
  if (!orbExploded) {
    if(int(player.getHealth())<int(2)){
    orbExploded = true;
    player.setSprite(new ExplodingSprite(*(player.getSprite())));
    }
  }
}
  if ( orbExploded ) {
      if ( static_cast<ExplodingSprite*>(const_cast<MultiframeSprite*>(player.getSprite()))->chunkCount() == 0 ) {
	sound[0];
        Vector2f pos = player.getSprite()->getPosition();
	Vector2f vel=player.getSprite()->getVelocity();
	delete player.getSprite();
	MultiframeSprite * mf=new MultiframeSprite(
          pos,vel,
          "ninjaStand", frameFactory::getInstance().setFrame("ninjaStand"),3,3);  //possibly lost leak here
        player.setSprite(mf);
        orbExploded = false;
	player.decrease_life();
	player.setHealth();
	viewport.setObjectToTrack(player.getSprite());
      }
    }	
}

void Manager::explodeVcheck()
{
  if(collisionVFound == true)
  {
    
  if (!orbVExploded) {
    if(int(villan.getHealth())<int(2)){
    orbVExploded = true;
    villan.setSprite(new ExplodingSprite(*(villan.getSprite())));
    villan_die = true;
    }
    //delete temp;
  }
}
  if ( orbVExploded ) {
      if ( static_cast<ExplodingSprite*>(const_cast<MultiframeSprite*>(villan.getSprite()))->chunkCount() == 0 ) {
	sound[0];
        orbVExploded = false;
      }
    }	
}


void Manager::checkForCollisionsPBVB() {
  collisionBFound = false;
  
   std::vector<MultiframeSprite *>::iterator orb=orbs.begin();
  std::vector<Bullet *>::iterator bull=bullet.begin();
  while(bull!=bullet.end()){
	if((((*bull)->calulateDistance())*0.001)>1){
	  delete (*bull);
	  bull=bullet.erase(bull);
	  if(bull==bullet.end()){break;}
	}
	while(orb!=orbs.end()){
	  if(orb==orbs.end()){break;}
		if(collisionStrategy->execute(*(*bull)->getSprite(),*(*orb))) {
		    collisionBFound=true;
		    if ((dynamic_cast<MultiframeSprite*>(*orb))!=0) {
		    
		    MultiframeSprite *temp = static_cast <MultiframeSprite*> (*orb);
		    MultiframeSprite *orb1=new ExplodingSprite(*temp);
		    expoorbs.push_back(orb1);
		    delete temp; 
		    orb=orbs.erase(orb);
		    }
	    
	  }
	  if(orb==orbs.end()){break;}
	 else{++orb;}
    }
    if(collisionBFound){
      MultiframeSprite *temp1 = const_cast <MultiframeSprite*> ((*bull)->getSprite());
      MultiframeSprite *orb2=new ExplodingSprite(*temp1);
      expoorbs.push_back(orb2);
      delete temp1;
      bull=bullet.erase(bull);      
    }
    if(bull==bullet.end()){break;}
    ++bull;
  }

}



void Manager::shootvillan()
{
  SDL_Delay(20);
  unsigned curr_ticks=SDL_GetTicks();
  unsigned dis;
  dis=villan.getX()-player.getX();
  int interval=0;
  if((dis)<((gdata->getXmlInt("viewWidth")/2)-50))
  {
    if(level==1){ 
      interval=50; 
      villan.setPVelocity(100);
      
    }
    else if(level==2){ 
      interval=30; 
      villan.setPVelocity(150);
    }
    else { 
      interval=15;
      villan.setPVelocity(200);
    }
  if(int((curr_ticks-start_time))%interval==0 and villan_die == false and player.getLife() != 0){
    if(villan.getBullet()>0){
    makeBomb("bomb");
    villan.decrease_Bullet();
    }
  }
  }
  if(int(dis)>(gdata->getXmlInt("viewWidth"))/2){
    villan.setPVelocity(villan.getPVelocity()-50);
  }
  
}


void Manager::draw() const {
  backWorld.draw();
  frontWorld.draw();
  player.draw();
  villan.draw();
  
  io.printMessageAt("Extra Option (F1)", 800,10);
  io.printMessageAt("Mute (m)", 800,30);
  io.printMessageValueAt("Life :",int(player.getLife()),800,50);
  if(level==1){ io.printMessageAt("Level : Easy",800,70); }
  else if(level==2){ io.printMessageAt("Level : Moderate",800,70); }
  else { io.printMessageAt("Level : difficult",800,70); }
  
  
  io.printMessageValueAt("Ninja Health :",int(player.getHealth()),50,410);
  
  io.printMessageValueAt("Villan Health :",int(villan.getHealth()),800,410);
  
  if(help_key==1){
    io.printMessageValueAt("Orb :",int(orbs.size()),800,90);
    io.printMessageValueAt("Expo orb :",int(expoorbs.size()),800,110);
    io.printMessageValueAt("Bullet orb :",int(bullet.size()),800,130);
    io.printMessageValueAt("Ninja Speed :",int(player.getPVelocity()),50,430);
    io.printMessageValueAt("Max Bullet :",int(villan.getBullet()),800,450);
    io.printMessageValueAt("Villan Speed :",int(villan.getPVelocity()),800,430);
  }
  if(player.getLife()==0){
    io.printMessageAt("GAME OVER",Gamedata::getInstance()->getXmlInt("viewWidth")/2,Gamedata::getInstance()->getXmlInt("viewHeight")/2);
    clock.pause();
  }
if(villan_die==true and expoorbs.size()==0){
    io.printMessageAt("You Won",Gamedata::getInstance()->getXmlInt("viewWidth")/2,Gamedata::getInstance()->getXmlInt("viewHeight")/2);
    clock.pause();
  }
  std::vector<MultiframeSprite*>::const_iterator drawIt = orbs.begin();
    while ( drawIt != orbs.end() ) {
      (*drawIt)->draw();
      ++drawIt;
    }
    drawIt = expoorbs.begin();
    while ( drawIt != expoorbs.end() ) {
      (*drawIt)->draw();
      ++drawIt;
    }
  for (unsigned int i=0;i<bullet.size();++i){
    bullet[i]->draw();
  }

  if (collisionVFound) {
    if(help_key==1){
    io.printMessageAt("Villan : Oops, collision!", 50, 70);
    }
  }
  else {
    if(help_key==1){
    io.printMessageAt("Villan : No Collision.", 50, 70);
    }
  }
  if (collisionFound) {
    if(help_key==1){
    io.printMessageAt("Player : Oops, collision!", 50, 30);
    }
  }
  else {
    if(help_key==1){
    io.printMessageAt("Player : No Collision.", 50, 30);
    }
  }
  if (collisionBFound) {
    if(help_key==1){
    io.printMessageAt("Bullets : Oops, collision!", 50, 50);
    }
  }
else {
  if(help_key==1){
    io.printMessageAt("Bullets : No Collision.", 50, 50);
  }
  }

}

void Manager::update(Uint32 ticks) {
  viewport.update();
  backWorld.update();
  frontWorld.update();
  player.update(ticks);
  villan.update(ticks);
  std::vector<MultiframeSprite *>::iterator updateIt = orbs.begin();
    while ( updateIt != orbs.end() ) {
      (*updateIt)->update(ticks);
      ++updateIt;
    }
    updateIt = expoorbs.begin();
    while ( updateIt != expoorbs.end() ) {
      (*updateIt)->update(ticks);
      if ( static_cast<ExplodingSprite*>(*updateIt)->chunkCount() == 0 ) {
        updateIt = expoorbs.erase( updateIt );
      }
      else ++updateIt;
    }
  std::vector<Bullet *>::iterator ptr=bullet.begin();
  while(ptr!=bullet.end()){
    (*(*ptr)).update(ticks);
    ++ptr;
  }
}

void Manager::play() {
  SDL_Event event;
  MenuManager menuMan;
  bool done = false;
  bool keyCatch = false;
  clock.pause();
  done=menuMan.play();
  clock.unpause();
  menu_switch=true;
  while ( not done ) {
    draw();
    SDL_Flip(screen);
    Uint32 ticks = clock.getElapsedTicks();
    update(ticks);
    player.stop();
    if(int(villan.getX())>int(Gamedata::getInstance()->getXmlInt("worldWidth")-200))
    {
      villan.stop();
      
    }
    checkForCollisionsPBV();
    checkForCollisionsPBVB();
    checkForCollisionsVBP();
    explodecheck();
    explodeVcheck();
    shootvillan();
    music=menuMan.getMusic();
    if(music){
      if(music_switch){
      sound.toggleMusic();
      music_switch=false;
      }
    }
    else{
      if(!music_switch){
      sound.toggleMusic();
      music_switch=true;
      }
    }
    if(menu_switch){
      villan.setMaxBullet(menuMan.getNumberOfStars());
      level=menuMan.getLevelno();
      menu_switch=false;
    }
    cheat=menuMan.getCheat();
    if(player.getLife()==0){clock.pause();}
    if(villan_die == true and expoorbs.size()==0){clock.pause();}
    SDL_PollEvent(&event);
    if (event.type ==  SDL_QUIT) { break; }
    if(event.type == SDL_KEYUP) { keyCatch = false; }
    if(event.type == SDL_KEYDOWN) {
      switch ( event.key.keysym.sym ) {
        case SDLK_ESCAPE : {
	  if (!keyCatch) {
          keyCatch = true;
	  clock.pause();
	  done=menuMan.play();
	  clock.unpause();
	  level=menuMan.getLevelno();
	  if(level==1){  
	    villan.setPVelocity(100);
	    
	  }
	  else if(level==2){  
	    villan.setPVelocity(150);
	  }
	  else { 
	    villan.setPVelocity(200);
	  }
	  menu_switch=true;
	  }
	  break;
	}
	case SDLK_F1:{
	  if (!keyCatch) {
	    keyCatch = true;
	    if(help_key==0){ help_key=1; }
	    else { help_key=0; }
	  }
	  break;
	  
	}
        case SDLK_q      : done = true; break;
        case SDLK_t :
          if ( !keyCatch ) {
            keyCatch = true;
            currentOrb = (currentOrb+1) % player_track.size(); 
            viewport.setObjectToTrack(player_track[currentOrb]);
          }
          break;
	  case SDLK_f: {
          if (!keyCatch) {
            keyCatch = true;
	    if(collisionFound!=true){
	      makebullet();
	    }
          }
          break;
        }
	case SDLK_m: {
          if (!keyCatch) {
            keyCatch = true;
	    sound.toggleMusic();
            //music_switch=true;
          }
          break;
	}
        case SDLK_LEFT  : { player.left(); break; }
        case SDLK_RIGHT : { player.right(); break; }
        case SDLK_UP    : {/* player.up(); break; */ }
        case SDLK_DOWN  : {/*player.down(); break; */ }
        default          : break;
      }
    }
  }
}
