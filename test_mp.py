import mediapipe as mp

print("Module:", mp)
print("File:", getattr(mp, "__file__", "N/A"))
print("Attributes:", dir(mp)[:20])