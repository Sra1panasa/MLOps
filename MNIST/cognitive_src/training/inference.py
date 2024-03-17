import requests

if __name__ == "__main__":
    try:
        print('Sending request...')
        url = 'http://localhost:8000/predict'  # Ensure this matches your FastAPI endpoint exactly
        files = {'file': open('D:/Sravan/assignments/Kognitive/data/image.jpg', 'rb')}
        response = requests.post(url, files=files)
        print('Response:', response.json())
    except Exception as e:
        print('An error occurred:', str(e))
