from Service.service import Service
import logging

logger = logging.getLogger(__name__)

def StartShop():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    sv = Service()
    logger.info("Starting App")
    sv.Shop()
    logger.info("Shutting Down App")


if __name__ == "__main__":
    StartShop()