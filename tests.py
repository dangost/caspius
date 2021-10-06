from caspius import Logger, Colors


def logs_handler(message: str):
    with open("logs.txt", 'a') as fs:
        fs.write(f"\n{message}")


logger = Logger()
logger.set_handler(logs_handler)
logger.info("Service running in http://127.0.0.1:8080")
logger.warning("We got the bug!")
logger.log("User added to database")
logger.custom_log("User unauthorized", name="HTTP", color=Colors.GREEN)


