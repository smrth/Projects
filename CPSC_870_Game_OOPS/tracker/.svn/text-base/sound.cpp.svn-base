#include <ctime>
#include "sound.h"
using std::string;


SDLSound::~SDLSound() {
  std::cout << "Cleaning up sounds ..." << std::endl;
  std::clock_t start = std::clock();
  Mix_HaltMusic();
  Mix_FreeMusic(music);
  for (unsigned int i = 0; i < sounded.size(); ++i) {
    Mix_FreeChunk(sounded[i]);
  }
  Mix_CloseAudio();
  std::clock_t duration = std::clock() - start;
  std::cout << "Clean up took " << duration << " ticks\n";
}

SDLSound::SDLSound() : 
  gdata( Gamedata::getInstance() ),
  volume(SDL_MIX_MAXVOLUME/4), 
  currentSound(-1), 
  music(NULL),
  audioRate(gdata->getXmlInt("musicaudioRate")), 
  audioChannels(gdata->getXmlInt("musicaudioChannels")), 
  audioBuffers(gdata->getXmlInt("musicaudioBuffers")),
  sounded(),
  channels()
{
  if(Mix_OpenAudio(audioRate, MIX_DEFAULT_FORMAT, audioChannels, 
                   audioBuffers)){
    throw string("Unable to open audio!");
  }
  music = Mix_LoadMUS(gdata->getXmlStr("musicFile").c_str());
  //music = Mix_LoadMUS("sound/1dragon.mp3");
  // Need to install midi to play the following:
  //music = Mix_LoadMUS("sound/ballad2.mid");
  if (!music) throw string("Couldn't load Music")+Mix_GetError();

  startMusic();
  sounded.push_back( Mix_LoadWAV("sound/sword.wav"));
  sounded.push_back( Mix_LoadWAV("sound/explosion.wav") );
  for (unsigned int i = 0; i < sounded.size(); ++i) channels.push_back(i);
}

void SDLSound::toggleMusic() {
  if( Mix_PausedMusic() ) { 
    Mix_ResumeMusic(); 
  } 
  else { 
    Mix_PauseMusic(); 
  } 
}

void SDLSound::operator[](int index) {
  if (currentSound >= 0) Mix_HaltChannel(currentSound);
  currentSound = index;
  Mix_VolumeChunk(sounded[index], volume);
  channels[index] = 
     Mix_PlayChannel(channels[index], sounded[index], 0);
}

void SDLSound::startMusic() {
  Mix_VolumeMusic(volume);
  Mix_PlayMusic(music, -1);
}

void SDLSound::stopMusic() {
  Mix_HaltMusic();
  Mix_FreeMusic(music);
}

