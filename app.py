async def on_startup(dp):
    import filters
    filters.setup(dp)
    import middlewares
    middlewares.setup(dp)



if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp)
