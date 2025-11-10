from app.config import TICKET_PRICES
from app.tools import price_function, get_ticket_price

tools = [
    {
        "name": "get_ticket_price",
        "description": "Obtiene el precio del billete a una ciudad de destino",
        "parameters": {
            "type": "object",
            "properties": {
                "destination_city": {
                    "type": "string",
                    "description": "Ciudad a la que se quiere viajar"
                }
            },
            "required": ["destination_city"]
        }
    }
]



# def get_ticket_price(destination_city):
#     print(f"Tool get_ticket_price called for {destination_city}")
#     city = destination_city.lower()
#     return TICKET_PRICES.get(city, "Unknown")