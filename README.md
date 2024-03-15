
## Industry Track
## Authors

- [Amitabh Sarkar](https://github.com/Amitabhsar)
- Student No. 2307322


# A Distributed Chat Room System in Python

In this project I have implemented a distributed Chat Room where three essential elements—the Broker, Server, and Clients—cooperate to offer a smooth real-time messaging experience. The Broker oversees the dissemination of messages by serving as a central hub. Incoming messages are queued and then distributed to connected clients, guaranteeing a steady stream of communication. The server, which is essential for creating client connections, watches for incoming requests and handles each client in its own thread for reliable concurrent processing. Clients register with the Broker upon connection in order to receive messages. Using an intuitive graphical user interface, the Clients establish a connection with the Server and exchange messages. After passing via the Server to the Broker, these messages are then broadcast to all of the clients that are currently in use.




## System Architecture

The interaction between the Broker, Server, and Client components in my distributed chat room system is shown in the following diagram.

![App Screenshot](https://i.imgur.com/jgXHUTg.png)

* Broker :  The central component of the message distribution system is the Broker. It serves as a go-between, controlling the communication between clients. It keeps track of listeners, or clients, who have subscribed to receive messages, as well as a queue for incoming messages. To make sure that every client receives the broadcasted messages, the Broker receives a message, adds it to the queue, and then distributes it to all active listeners.

* Server : The creation and maintenance of client connections is the server's main responsibility. It keeps an ear out for new connections from clients and helps them communicate with the broker. The Server starts a specific thread for managing a client's communication as soon as it connects. Messages from the client are received in this thread and forwarded to the broker.

* Client : Clients communicate via a graphical user interface (GUI) created with Tkinter. A client connects to the server first and sends its username, which serves as a unique identifier. After establishing a successful connection, the client and server can exchange messages. Additionally, the client is always on the lookout for new messages from the server. These messages are shown in the client's GUI after being received from the Broker (through the Server).
## Key Characteristics
* Concurrency : The system allows for the simultaneous interaction of multiple clients. Both the broker and the server can manage many connections and messages at once thanks to threading. Due to the management of each client connection in a separate thread, client requests and message distribution can be processed in parallel.

* Transparency : There is a degree of transparency in the system, especially in terms of location. Clients only require the host address and port number; they are not required to know the server or broker's exact location. The intricacy of message distribution and routeing is concealed from users.

* Fault Tolerance : Basic fault tolerance mechanisms are present in the system. When a client disconnects, for example, the server notices it and takes it off the broker's listener list.

* Scalability: The architecture permits scalability. By changing LISTENER_LIMIT, the broker is potentially able to handle more listeners and the server may be able to accept more connections.

* Responsiveness: The system is responsive because it distributes messages in real-time and uses a GUI client. Instant feedback and updates are provided to clients, which is essential for chat application.
## Built With (Functionalities and Implementation)

In my project, I have employed a classic client-server architecture using Python, a flexible and popular programming language that was chosen for its ease of use and robust libraries. A broker, a server, and several clients make up the system's three primary parts. Each one of these parts has a specific function in enabling real-time communication. 

Message distribution to all connected clients is the responsibility of the Broker, which is implemented as a central message queue. Python's 'queue.Queue' is used for managing messages, and this ensures thread-safe operations.  Flexible management of active users is made possible by the dynamic addition or removal of listeners, or clients, from the Broker's list. The 'threading' module in Python allows the Broker to disperse messages continuously without interfering with other processes.

Between clients and the Broker, the Server serves as a middleman. It is intended to manage several client connections at once, with each client being handled in its own thread. Python's threading feature enables this concurrency, enabling the effective simultaneous processing of client requests. The TCP socket that the server is listening on was selected because it is dependable for error-checked and order-preserving transmission, which is essential for a chat programme. The server forwards messages received from clients to the broker so that they can be distributed.

Tkinter is a standard Python library used to create lightweight and responsive applications. It is used in the design of clients' graphical user interfaces (GUIs). Every client connects to the server through TCP and exchanges messages using encoded strings. Users can send and view messages in real time through the client's graphical user interface. Every client maintains a listening thread for message reception, which keeps the GUI responsive while it awaits incoming messages.
## Getting Started

Before proceeding, ensure you have Python installed on your computer. Save the already provided Python scripts (xinbroker.py, rvxnserver.py, and rvxnclient.py) in a folder on your computer. Let's call this folder 'chatroom'.

* Run the Broker : Open a terminal or command prompt. Navigate to the 'chatroom' directory, and run the broker script:

```bash
  python xinbroker.py
```
* Run the Server: Open a new terminal or command prompt window. Navigate to the 'chatroom' directory, and run the server script:

```bash
  python rvxnserver.py
```
* Run the Client(s) : Open a new terminal or command prompt for each client. Navigate to the 'chatroom' directory, and run the client script:

```bash
  python rvxnclient.py
```
Use the GUI to connect to the server and chat.

* Using the Application : 

In the client GUI, enter a username and click "Connect". Once connected, type your message and click "Send" to communicate with other connected clients.

And that's it! The chat room project ought to be operational on your local machine at this point. Every client you launch and establish a connection with can chat with other clients on the same server.
## Results of the tests

#### Connecting to Server(Before and After) : ####
The following screenshots show the user interface of connecting to server:

![App Screenshot](https://i.imgur.com/rXi1GTs.jpeg) 
![App Screenshot](https://i.imgur.com/sK21rl9.jpeg) 

The following screenshots show the user interface of sending texts between the clients: 

![App Screenshot](https://i.imgur.com/0e2mkDL.jpeg) 
![App Screenshot](https://i.imgur.com/mYnHvhz.jpeg) 

The following screenshot shows the smooth communication between the clients:

![App Screenshot](https://i.imgur.com/wBs2TD0.jpeg) 

**Evaluation** : For the evaluation phase, I have created two scripts, and the scripts are useful tools for evaluating the system's performance in different load scenarios. These scripts' primary goal is to replicate various intensities and levels of complexity of real-world usage scenarios, giving users a thorough grasp of the system's capabilities and behaviour. 

* Scenario 1 : The evaluation of the system under a moderate load is the main goal of Scenario 1 (Small Case). This model mimics a realistic situation in which several clients (five in this example) send 200 messages each, each of a reasonable size (10,000–20,000 bytes). 

Evaluated Result is attached below :

![App Screenshot](https://i.imgur.com/U8mJzJP.jpeg)

**Performance** : The test results show a high efficiency and throughput. For most of the messages, the entry "0.0000 seconds" indicates that the system is processing them almost instantly. On occasion, though, messages can take 0.0156 or 0.0157 seconds to process.

* Scenario 2 : Scenario 2 (Large Case), on the other hand, is designed to evaluate the robustness and scalability of the system. It increases the quantity and size of messages sent, allowing up to 300 messages per client, each containing 30,000–50,000 bytes. This scenario tests the limits of the system's capacity by simulating a high-load scenario. Seeing how the system handles more network traffic, more processing demands, and more demanding concurrent operations is the aim here.

Evaluated Result is attached below :

![App Screenshot](https://i.imgur.com/iQFIGxW.jpeg)

**Performance** :

* Transmission Speed: The "0.0000 seconds" time stamp indicates that the majority of messages were sent almost instantly. This implies a very high transmission speed, suggesting a high-performance system environment or effective network communication.

* Variability in Message Size: Messages with varying sizes (30,000 and 50,000 bytes) were reliably transmitted at rapid speeds. This shows that there is little to no performance impact when handling different payload sizes by the system.

* Messages are sent by a number of clients (TestClient0, TestClient1, etc.) with consistent performance across them. All of these clients appear to have consistently good performance, which suggests a load that is evenly distributed and effective simultaneous request processing.

## Acknowledgements

 - [Simple TCP Chat Room in python](https://www.youtube.com/watch?v=3UOyky9sEQY&list=LL&index=10)
 - [How to make a chat application in Python](https://thepythoncode.com/article/make-a-chat-room-application-in-python?utm_content=cmp-true)
 - [How To Create A Real Time Chat App In Python Using Socket Programming](https://www.youtube.com/watch?v=cV-syT1fO2c&list=LL&index=7)

