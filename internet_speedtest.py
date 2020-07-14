from speedtest import Speedtest
import numba

st = Speedtest()

print("Download :", st.download())
print("Upload :", st.upload())

st.get_servers([])
print("Ping :", st.results.ping)