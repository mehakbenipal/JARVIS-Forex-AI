import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

def predict_next_close(close_series):
    # Step 1: Normalize the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(close_series.values.reshape(-1, 1))

    # Step 2: Create sequences
    X = []
    sequence_length = 60
    for i in range(sequence_length, len(scaled_data)):
        X.append(scaled_data[i-sequence_length:i, 0])
    X = np.array(X)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Step 3: Build LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1), name="lstm_1"))
    model.add(LSTM(units=50, name="lstm_2"))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Step 4: Train model
    model.fit(X, scaled_data[sequence_length:], epochs=5, batch_size=32, verbose=0)

    # Step 5: Predict next close
    last_60 = scaled_data[-60:].reshape(1, 60, 1)
    predicted_scaled = model.predict(last_60)
    predicted_close = scaler.inverse_transform(predicted_scaled)
    
    return round(float(predicted_close[0][0]), 5)
