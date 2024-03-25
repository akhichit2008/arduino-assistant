#include <iostream>
#include <chrono>
#include <pthread.h>
#include <thread>

using namespace std;
using namespace chrono;

void timerFunction(int duration) {
  this_thread::sleep_for(milliseconds(duration * 1000));
  cout << "Time Up!!!!" << endl;
}

int main() {
  int timerDuration;
  cout << "Enter Timer Duration: ";
  cin >> timerDuration;

  // Create a thread to run the timer function
  thread timerThread(timerFunction, timerDuration);

  // Continue program execution while the timer runs in a separate thread
  // (You could add other code to be executed here)

  // Wait for the timer thread to finish (optional)
  timerThread.join();

  return 0;
}
