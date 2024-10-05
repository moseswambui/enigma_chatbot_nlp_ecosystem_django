import tensorflow as tf
from tensorflow.keras import layers, models


def create_model():
    # Define a Sequential model
    model = models.Sequential([
        layers.Input(shape=(28, 28)), # iNPUT LAYER
        layers.Flatten(),# Flatten the input
        layers.Dense(128, activation="relu"), # Hidden layer
        layers.Dense(10, activation="softmax")# Output layer (10 classes)
    ])

    # Compile the model
    model.compile(optimizers="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    # Save the model architecture (before training)
    model.save("models/chatbot_model.keras", save_format="keras")
    print("Model Architecture saved.")

if __name__=="__main__":
    create_model()