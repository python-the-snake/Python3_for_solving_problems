from speedtest import Speedtest

st = Speedtest()

print("Download :", st.download())
print("Upload :", st.upload())

st.get_servers([])
print("Ping :", st.results.ping)