# DuoChatApp

A Python application to replicate the functioning of a chat applications throgh the use of interconnected sockets to form a server - client system. The application also houses a database-like object (a CSV file) to store messages when either the Server or the Client is offline, which is then read throguh when the server/client comes back online

## Features

- Very lightweight application using Sockets to replicate the functioning of a 2-person chat system without a middleman.
- Uses a CSV file to store messages, which are read through when the other user comes back online. They are used and manipulated as pandas Series and DataFrame objects.
- Carries a basic CLI accessed through `\<command>` - As of now there are 5 such commands.
- Carries a tool to plot a self-updating graph of the computer's runtiime properties (RAM and CPU usage).
