def call_board_api():
    from pprint import pprint

    from fetcher.lib.reader import load_config
    from fetcher.payload.bodies.board_body import (
        BoardRequestBody,
        ClientInfo,
        GetBoardInfo,
    )
    from fetcher.payload.body import RequestBody

    config_path = "fetcher/config/board.yaml"
    config = load_config(config_path)
    pprint(config)
    # From config
    client_info = ClientInfo(**config["client"])
    get_board_body = GetBoardInfo(ID="hello", PAGE="5")
    board_request_body = RequestBody(BoardRequestBody).create_request_body(
        client_info, get_board_body
    )

    pprint(board_request_body)

    # Read config test


def main():
    call_board_api()


if __name__ == "__main__":
    main()
