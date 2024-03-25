#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct Reminder {
  string date;
  string time;
  string name;
};

void storeReminder(Reminder reminder) {
  ofstream file("calendar.data", ios::app);
  file << reminder.date << "," << reminder.time << "," << reminder.name << endl;
  file.close();
}

vector<Reminder> getRemindersByDate(string date) {
  vector<Reminder> reminders;
  ifstream file("reminders.txt");
  string line;
  while (getline(file, line)) {
    string delimiter = ",";
    int pos = line.find(delimiter);
    string reminderDate = line.substr(0, pos);
    line.erase(0, pos + delimiter.length());
    pos = line.find(delimiter);
    string reminderTime = line.substr(0, pos);
    line.erase(0, pos + delimiter.length());
    string reminderName = line;
    if (reminderDate == date) {
      Reminder reminder;
      reminder.date = reminderDate;
      reminder.time = reminderTime;
      reminder.name = reminderName;
      reminders.push_back(reminder);
    }
  }
  file.close();
  return reminders;
}

int main() {
  // Get the event date, time, and name from the user.
  string date;
  cout << "Enter the event date (YYYY-MM-DD): ";
  cin >> date;
  string time;
  cout << "Enter the event time (HH:MM): ";
  cin >> time;
  string name;
  cout << "Enter the event name: ";
  cin >> name;

  // Create a reminder object and store it in the file.
  Reminder reminder;
  reminder.date = date;
  reminder.time = time;
  reminder.name = name;
  storeReminder(reminder);

  // Retrieve the reminders for the given date.
  vector<Reminder> reminders = getRemindersByDate(date);

  // Print the reminders.
  for (Reminder reminder : reminders) {
    cout << reminder.date << " " << reminder.time << " " << reminder.name << endl;
  }

  return 0;
}