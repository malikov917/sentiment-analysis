1. build an image:
> docker build -t sentiment .
2. run docker:
> docker run -d --name sentiment_container -p 5013:5013 sentiment
3. test request:
> curl -X POST http://localhost:5013/analyze -H "Content-Type: application/json" -d '{"text": "Ich liebe diese App!!"}'