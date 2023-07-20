# ChessServer

## A Simple Flask Server which can provide the valid moves of the chess pieces based on the current board

## Installation:
### Repo Clone:
- Clone the repo over https.
- Navigate to `ChessServer/src`.
- Run the app.py file via:
    ```python
    python3 app.py
    ```
### Pulling the Docker Image
- This needs docker to be installed on the system.
- Pull the docker image using the command:
    ```docker
    docker pull satyendra0011/chessserver1:v1
    ```

- Run the docker image using command:
    ```docker
    docker run  -p 5000:5000 satyendra0011/chessserver1:v1
    ```

## API Usage
### Request method:
- POST
### Endpoint:
 - 127:0.0.1:5000/chess/{pieceName}
 - PieceName is the name of the chess piece whose valid moves we want to find

 ### Body:
 - A JSON Body having the below mentioned format:
    - {"positions":
    {
        "Queen": "A5",
        "Bishop": "G8",
        "Rook": "H5",
        "Knight": "G4"
    }
}

