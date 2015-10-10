<h1>
Key/Value store example
</h1>
<br>
Usage:
<br>
<p>
1) In a screen/tmux instance, run storeServer.py and leave running<br>
2) Import serverClient.py in your project<br>
3) Instantiate a client object -> client = storeClient.StoreClient()<br>
4) Connect to server -> client.connect()<br>
5) Start using methods .get(key), .insert(key,value), .delete(key)<br>
</p>
