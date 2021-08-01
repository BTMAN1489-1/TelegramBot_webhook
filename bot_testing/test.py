import unittest
from data import config
from loader import bot
import asyncio
import aiohttp


class ValidTest(unittest.TestCase):
    def test_valid_token(self):
        self.assertIsNotNone(config.API_TOKEN, "Token must not be None")  # add assertion here

    @unittest.skipUnless(config.WEBHOOK_HOST != '', "Webhook is invalid")
    def test_valid_domain(self):
        self.assertRegex(text=config.WEBHOOK_HOST, expected_regex="https://.*")


class BotTest(unittest.IsolatedAsyncioTestCase):
    async def test_bot_auth(self):
        async with aiohttp.ClientSession() as bot._session:
            self.bot_info = await bot.get_me()
        self.assertEqual(self.bot_info["username"], "my_first_developed_bot")

