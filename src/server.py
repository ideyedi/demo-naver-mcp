from mcp.server.fastmcp import FastMCP
import httpx

# Create an MCP server
mcp = FastMCP("ideyedi mcp demo", "0.1.0")

api_headers = {
    "X-Naver-Client-Id": "gq696efE6pfkVAv7kVOF",
    "X-Naver-Client-Secret": "O8jeleExQd",
}
API_ENDPOINT = "https://openapi.naver.com/v1"

@mcp.tool()
def search_shop(
        query: str,
        display: int = 10,
        start: int = 1,
        sort: str = "sim",
        filter: str = None,
        exclude: str = None,
):
    """
    Args:
        query (str): The query to search for.
        display (int, optional): The number of items to display. Defaults to 10.
        start (int, optional): The start index for the search. Defaults to 1.
        sort (str, optional): The sorting method. Defaults to "sim". ordering price 'asc' or 'desc'.
        filter (str, optional): The filter for the search. Defaults to None.
        exclude (str, optional): The exclude filter for the search. Defaults to None.
    """
    with httpx.Client() as client:
        response = client.get(
            f"{API_ENDPOINT}/search/shop.json",
            params={
                "query": query,
                "display": display,
                "start": start,
                "sort": sort,
                "filter": filter,
                "exclude": exclude,
            },
            headers=api_headers,
        )
        #print(sort)
        response.raise_for_status()  # Raise an error for bad responses

        return response.text


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
