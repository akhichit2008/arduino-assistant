import pandas as pd

filename = " /workspaces/arduino-assistant/ai-backend/ai_backend/transcribe.csv"


data = pd.read_csv("/workspaces/arduino-assistant/ai-backend/ai_backend/transcribe.csv")
data.drop("file",inplace=True,axis=1)

print(data)