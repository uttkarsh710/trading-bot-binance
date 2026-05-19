from bot.logging_config import logger
import random
from datetime import datetime


def place_order(symbol, side, order_type, quantity, price=None):

    try:

        logger.info(
            f"Placing order | Symbol={symbol} | "
            f"Side={side} | Type={order_type} | "
            f"Qty={quantity} | Price={price}"
        )

        mock_response = {
            "orderId": random.randint(100000, 999999),
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "executedQty": quantity,
            "avgPrice": price if price else "104500",
            "time": str(datetime.now())
        }

        logger.info(f"Mock API Response: {mock_response}")

        return mock_response

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise