import wolfaramalpha

input = raw_input("Question: ")
app_id = "85VWLY-LPA5VG4P7Q"
client = wolfarmalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer