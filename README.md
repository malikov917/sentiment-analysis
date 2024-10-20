1. run docker
docker run -p 5013:5013 py1
2. test request
curl -X POST http://localhost:5013/analyze -H "Content-Type: application/json" -d '{"text": "Ich liebe diese App!!"}'