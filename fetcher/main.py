from lib import api_client


def call_board_api():
    from pprint import pprint
    from models.board import ClientInfo, GetBoardBody, BoardRequestBody

    client_info = ClientInfo(CLIENT_ID="hello", CLIENT_KEY="World")
    get_board_body = GetBoardBody(ID="board123", PAGE=1)
    board_request_body = BoardRequestBody.create_board_request_body(
        client_info, get_board_body
    )

    pprint(board_request_body.json())


def main():
    call_board_api()


if __name__ == "__main__":
    main()
