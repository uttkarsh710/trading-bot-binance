import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import logger


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:

        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol     : {args.symbol.upper()}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if price:
            print(f"Price      : {price}")

        print("===================================\n")

        response = place_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("ORDER PLACED SUCCESSFULLY\n")

        print("========== ORDER RESPONSE ==========")
        print(f"Order ID       : {response.get('orderId')}")
        print(f"Status         : {response.get('status')}")
        print(f"Executed Qty   : {response.get('executedQty')}")
        print(f"Avg Price      : {response.get('avgPrice')}")
        print("====================================")

    except Exception as e:
        logger.error(str(e))
        print(f"\nERROR: {e}")


if __name__ == "__main__":
    main()