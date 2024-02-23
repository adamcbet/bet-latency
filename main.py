import iperf3


def latency():
    client = iperf3.Client()
    client.server_hostname = "https://elasticsearch-poc-elastic.apps.ocp.betsolutions.net"
    client.port = 443
    client.json_output = True
    results = client.run()


if __name__ == "__main__":
    latency()
