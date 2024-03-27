const config = {method:'GET',headers:{accept:'application/javascript'}}

fetch('https://api.tomorrow.io/v4/weather/realtime?location=chennai&apikey=aHTCo2frOUcpyNSXOxPNd8iPXz222BeZ',config)
.then(res => res.text())
.then(res => document.write(res))
.catch(err => console.err(err))