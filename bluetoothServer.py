import bluetooth

name = "bt_server"
target_name = "test"
uuid="f0d60c98-748e-4179-a962-d3111033c098"

def runServer():
        serverSocket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        port=bluetooth.PORT_ANY
        serverSocket.bind(("", port))
        print("Listnening for connections on port: ", port)
        serverSocket.listen(1)
        port=serverSocket.getsockname()[1]

        bluetooth.advertise_service( serverSocket, "SampleServer",
                                     service_id=uuid,
                                     service_classes=[uuid,bluetooth.SERIAL_PORT_CLASS],
                                     )
        inputSocket, address = serverSocket.accept()
        print("Help")
        print("Got connection with", address)
        data=inputSocket.recv(1024)
        print("received [%s] \n" %data)
        inputSocket.close()
        serverSocket.close()

runServer()
