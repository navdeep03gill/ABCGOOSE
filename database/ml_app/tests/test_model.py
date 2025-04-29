from database.ml_app.tests.model_inference import predict

def test_get():
    data = {
        'word1': "absolute",
        'word2': "downright"
    } 
    test_result = predict(data['word1'], data['word2'])
    print(test_result)

if __name__ == "__main__":
    test_get()
    
