import pickle, cv2

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

print(type(data))
print(data)
